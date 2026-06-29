"""
Horizon molecule temperature cutoff prediction.

Implements Schwarzschild causal sets in Eddington-Finkelstein coordinates,
computes SJ vacuum entanglement entropy across the horizon, and tests the
scaling T_cutoff(M) ~ M^{-2/3} implied by the 1/3 exponent.
"""

import numpy as np
import math
from ..core.modular import symplectic_eigenvalues, entanglement_entropy


def tortoise(r, M):
    """Schwarzschild tortoise coordinate r* = r + 2M log|r/2M - 1|."""
    return r + 2 * M * np.log(np.abs(r / (2 * M) - 1))


def null_coordinates(v, r, M):
    """Convert (v, r) to null coordinates (u, v).
    
    u = v - 2r* = v - 2r - 4M log|r/(2M) - 1|
    v = v (Eddington-Finkelstein advanced time)
    """
    u = v - 2 * r - 4 * M * np.log(np.abs(r / (2 * M) - 1))
    return u, v


class SchwarzschildCausalSet:
    """2D radial causal set in Schwarzschild spacetime.
    
    Uses Eddington-Finkelstein coordinates (v, r). The causal relation is
    determined by the null coordinates: i ≺ j iff v_j ≥ v_i and u_j ≥ u_i.
    
    Parameters
    ----------
    N : int
        Number of points.
    M : float
        Black hole mass (Planck units).
    v_max : float
        Maximum advanced time coordinate.
    r_min, r_max : float
        Radial coordinate range (must straddle 2M).
    seed : int, optional
        Random seed.
    """
    
    def __init__(self, N, M=1.0, v_max=10.0, r_min=1.5, r_max=5.0, seed=None):
        self.N = N
        self.M = M
        self.r_h = 2.0 * M  # Horizon radius
        self.v_max = v_max
        self.r_min = r_min
        self.r_max = r_max
        self.rng = np.random.default_rng(seed)
        
        self._points = None
        self._C = None
        self._Delta = None
        self._iDelta = None
        self._iDelta_evals = None
        self._iDelta_evecs = None
        self._abs_D = None
        self._W = None
        
        self._sprinkle()
        self._build_causal_matrix()
    
    def _sprinkle(self):
        """Poisson sprinkle in (v, r) with uniform density.
        
        In Eddington-Finkelstein coordinates, the 2D radial section has
        √(-g) = 1, so sprinkling is uniform in (v, r).
        """
        v = self.rng.uniform(0, self.v_max, self.N)
        r = self.rng.uniform(self.r_min, self.r_max, self.N)
        self._points = np.column_stack([v, r])
    
    def _build_causal_matrix(self):
        """Build the causal matrix using the null coordinate condition.
        
        In 2D EF coordinates: i ≺ j iff v_j ≥ v_i AND u_j ≥ u_i.
        """
        v = self._points[:, 0]
        r = self._points[:, 1]
        u, _ = null_coordinates(v, r, self.M)
        
        # i ≺ j if u_j ≥ u_i and v_j ≥ v_i
        dt_v = v[:, None] - v[None, :]  # v_j - v_i
        dt_u = u[:, None] - u[None, :]  # u_j - u_i
        
        # i ≺ j: we need difference to be ≥ 0 from i to j
        # dt[j,i] = coordinate(j) - coordinate(i), so if dt[j,i] ≥ 0 then j is to the causal future
        # The causal matrix C[i,j] = 1 if i ≺ j
        # We need: v[j] ≥ v[i] AND u[j] ≥ u[i]  (for i ≺ j)
        # That is: dt_v.T[j,i] ≥ 0 AND dt_u.T[j,i] ≥ 0? 
        # No, dt_v[i,j] = v_i - v_j. So dt_v[i,j] ≤ 0 means v_j ≥ v_i.
        # And dt_u[i,j] ≤ 0 means u_j ≥ u_i.
        
        self._C = ((dt_v <= 0) & (dt_u <= 0)).astype(np.float64)
        # Remove self-relations
        np.fill_diagonal(self._C, 0.0)
        
        self._Delta = self._C - self._C.T
    
    def diagonalize(self):
        """Eigendecompose iΔ and compute SJ covariance."""
        if self._iDelta_evecs is not None:
            return
        
        iD = 1j * self._Delta
        evals, evecs = np.linalg.eigh(iD)
        self._iDelta = iD
        self._iDelta_evals = evals
        self._iDelta_evecs = evecs
        
        self._abs_D = evecs @ np.diag(np.abs(evals)) @ evecs.conj().T
        self._W = 0.5 * self._abs_D
    
    # ── Properties ──────────────────────────────────────────────────
    
    @property
    def points(self):
        return self._points
    
    @property
    def horizon_radius(self):
        return self.r_h
    
    def interior_indices(self):
        """Indices of points inside the horizon (r < 2M)."""
        return np.where(self._points[:, 1] < self.r_h)[0]
    
    def exterior_indices(self):
        """Indices of points outside the horizon (r > 2M)."""
        return np.where(self._points[:, 1] > self.r_h)[0]
    
    # ── SJ vacuum ───────────────────────────────────────────────────
    
    def reduced_state(self, R_idx):
        """Reduced SJ covariance and symplectic form on a subset."""
        self.diagonalize()
        
        W_R = 0.5 * self._abs_D[np.ix_(R_idx, R_idx)].real
        Omega_R = self._Delta[np.ix_(R_idx, R_idx)]
        
        return W_R, Omega_R
    
    # ── Diagnostics ─────────────────────────────────────────────────
    
    def summary(self):
        """Print summary of this causal set."""
        N_int = len(self.interior_indices())
        N_ext = len(self.exterior_indices())
        n_rel = int(np.sum(self._C))
        print(f"SchwarzschildCausalSet: N={self.N}, M={self.M}, r_h={self.r_h:.2f}")
        print(f"  Interior: {N_int}, Exterior: {N_ext}")
        print(f"  Relations: {n_rel} (density={n_rel/self.N**2:.4f})")
    
    def horizon_molecules(self, delta=0.5):
        """Identify horizon molecules: causal links crossing the horizon.
        
        A horizon molecule is a pair (p, q) with p inside, q outside,
        and r_p, r_q within delta of r_h, that are causally linked.
        
        Parameters
        ----------
        delta : float
            Radial window around the horizon.
        
        Returns
        -------
        mol_pairs : ndarray (K, 2)
            Indices of molecule pairs.
        """
        v = self._points[:, 0]
        r = self._points[:, 1]
        near_horizon = np.abs(r - self.r_h) < delta
        inside = (r < self.r_h) & near_horizon
        outside = (r > self.r_h) & near_horizon
        
        in_idx = np.where(inside)[0]
        out_idx = np.where(outside)[0]
        
        pairs = []
        for i in in_idx:
            for j in out_idx:
                if self._C[i, j] or self._C[j, i]:
                    pairs.append((i, j))
        
        return np.array(pairs) if pairs else np.array([]).reshape(0, 2)
    
    def exterior_entropy(self):
        """Compute entanglement entropy of the exterior region."""
        R_idx = self.exterior_indices()
        if len(R_idx) < 5:
            return None
        
        W_R, Omega_R = self.reduced_state(R_idx)
        nu = symplectic_eigenvalues(W_R, Omega_R)
        
        if len(nu) < 2:
            return None
        
        S_total, S_modes = entanglement_entropy(nu)
        return S_total


def run_test(M_vals=None, N=200, v_max=10.0, r_min=None, r_max=None,
             n_runs=5, seed=42, constant_density=False):
    """Run the horizon molecule temperature cutoff test.
    
    Computes the SJ entanglement entropy across the horizon for
    Schwarzschild black holes at varying mass, and tests whether
    T_cutoff(M) ~ M^{-2/3}.
    
    Parameters
    ----------
    M_vals : array-like
        Black hole masses to test.
    N : int
        Base number of points (at M=1). In constant-density mode, scales
        as N * M² to keep point density fixed.
    v_max : float
        Advanced time coordinate range (scales with M in constant-N mode).
    r_min, r_max : float
        Radial range (defaults to 0.8 * r_h to 2.0 * r_h).
    n_runs : int
        Runs per mass value.
    seed : int
        Random seed.
    constant_density : bool
        If True, scale N ∝ M² to keep physical density constant (expensive
        at large M but necessary for proper area-law test).
    
    Returns
    -------
    result : dict
        M_vals, S_vals, T_eff, scaling_exponent, etc.
    """
    if M_vals is None:
        M_vals = [0.5, 1.0, 2.0, 4.0]
    
    # Reference density at M=1
    ref_N = N
    ref_v_max = v_max
    r_h_ref = 2.0
    ref_volume = ref_v_max * (r_h_ref * 2.0 - r_h_ref * 0.8)
    
    M_list = []
    S_list = []
    S_err_list = []
    N_ext_list = []
    
    for M in M_vals:
        S_runs = []
        N_ext_counts = []
        r_h = 2.0 * M
        
        # Radial range scales with horizon
        if r_min is None:
            r_min_local = r_h * 0.8
        else:
            r_min_local = r_min
        if r_max is None:
            r_max_local = r_h * 2.0
        else:
            r_max_local = r_max
        
        if constant_density:
            # Scale N to keep density fixed: N_local = N_ref * (V_local / V_ref)
            v_max_local = ref_v_max * M  # Scale coordinate time with mass
            V_local = v_max_local * (r_max_local - r_min_local)
            N_local = max(int(ref_N * V_local / ref_volume), 20)
            print(f"  M={M:.1f}: constant density mode, N={N_local}, V_local/V_ref={V_local/ref_volume:.2f}")
        else:
            v_max_local = v_max * M  # Keep fixed N, scale coordinates
            N_local = ref_N
        
        for run_i in range(n_runs):
            cs = SchwarzschildCausalSet(
                N=N_local, M=M, v_max=v_max_local,
                r_min=r_min_local, r_max=r_max_local,
                seed=seed + run_i * 100 + int(M * 10)
            )
            S = cs.exterior_entropy()
            if S is not None:
                S_runs.append(S)
                N_ext_counts.append(len(cs.exterior_indices()))
        
        if S_runs:
            M_list.append(M)
            S_list.append(np.mean(S_runs))
            S_err_list.append(np.std(S_runs))
            N_ext_list.append(np.mean(N_ext_counts))
            print(f"M={M:.1f}: S={np.mean(S_runs):.4f} ± {np.std(S_runs):.4f} "
                  f"(N_ext~{np.mean(N_ext_counts):.0f})")
        else:
            print(f"M={M:.1f}: FAILED (no valid exterior region)")
    
    # Fit scaling: S(M) vs log(M)
    if len(M_list) >= 3:
        log_M = np.log(M_list)
        log_S = np.log(S_list)
        A = np.vstack([log_M, np.ones_like(log_M)]).T
        slope, intercept = np.linalg.lstsq(A, log_S, rcond=None)[0]
        
        T_exponent = 1.0 - slope
        
        print(f"\nScaling: S ∝ M^{slope:.3f}")
        print(f"  Area law expects:   S ∝ M^2.000  (T ∝ M^{-1.000})")
        print(f"  Cutoff expects:     S ∝ M^{5/3:.3f}  (T ∝ M^{-0.667})")
        print(f"  Measured:           S ∝ M^{slope:.3f}  (T ∝ M^{T_exponent:+.3f})")
        
        if abs(slope - 2.0) < 0.2:
            print("  → Area law (Hawking radiation)")
        elif abs(slope - 5/3) < 0.2:
            print("  → Consistent with cutoff prediction")
        elif abs(slope) < 0.3:
            print("  → Fixed-N regime (entropy bounded by degrees of freedom)")
            print("  → Run with constant_density=True for physical scaling")
        else:
            print("  → Unknown scaling regime")
    else:
        slope = None
        T_exponent = None
    
    return {
        "M_vals": np.array(M_list),
        "S_vals": np.array(S_list),
        "S_err": np.array(S_err_list),
        "N_ext_avg": np.array(N_ext_list),
        "slope": slope,
        "T_exponent": T_exponent,
        "constant_density": constant_density,
    }


def plot_scaling(result):
    """ASCII visualization of the entropy-mass scaling."""
    M = result["M_vals"]
    S = result["S_vals"]
    S_err = result["S_err"]
    
    if len(M) == 0:
        print("No data to plot.")
        return
    
    print("\nEntropy vs Mass scaling:")
    print(f"{'M':>6s}  {'S':>10s}  {'±':>6s}  {'Bar':>40s}")
    max_S = max(S) if len(S) > 0 else 1
    for i in range(len(M)):
        bar_len = int(S[i] / max_S * 40) if max_S > 0 else 0
        bar = "█" * bar_len
        print(f"{M[i]:6.2f}  {S[i]:10.4f}  {S_err[i]:6.4f}  {bar}")
    
    if result.get("slope") is not None:
        print(f"\nS ∝ M^{result['slope']:.3f}")
        print(f"T ∝ M^{result['T_exponent']:+.3f}")
    
    # Theoretical curves
    print("\nExpected scalings:")
    print(f"  Hawking:   S ∝ M^2.000  (area law, T ∝ 1/M)")
    print(f"  Cutoff:    S ∝ M^{5/3:.3f}  (T ∝ M^(-2/3))")
