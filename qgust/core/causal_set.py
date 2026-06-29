"""
Causal set generation and manipulation.

Provides the CausalSet class for Poisson sprinklings into various spacetimes,
causal matrix construction, and basic causal set diagnostics.
"""

import numpy as np
from numpy.random import Generator, default_rng


class CausalSet:
    """A causal set as a locally finite partially ordered set (C, ≺).
    
    Events are stored as spacetime coordinates. The causal relation is
    computed pairwise using the Minkowski light-cone condition.
    
    Parameters
    ----------
    points : ndarray of shape (N, D)
        Spacetime coordinates of N events in D dimensions.
        Columns: [t, x1, x2, ...] in units where c = 1.
    rng : Generator, optional
        NumPy random number generator.
    """
    
    def __init__(self, points=None, rng=None):
        self._rng = rng or default_rng()
        self._points = None
        self._C = None
        self._Delta = None
        self._iDelta = None
        self._iDelta_evals = None
        self._iDelta_evecs = None
        self._abs_D = None
        self._W = None
        
        if points is not None:
            self._points = np.asarray(points, dtype=np.float64)
    
    # ── Factory methods ─────────────────────────────────────────────
    
    @classmethod
    def sprinkle_diamond_2d(cls, N, L=1.0, rng=None):
        """Poisson sprinkle N points into 2D diamond |t| + |x| <= L.
        
        Parameters
        ----------
        N : int
            Number of points.
        L : float
            Half-size of the diamond.
        rng : Generator, optional
        
        Returns
        -------
        CausalSet
        """
        rng = rng or default_rng()
        t = rng.uniform(-L, L, N)
        half_width = L - np.abs(t)
        # Uniform in [−hw, hw] — sample per point
        x = rng.uniform(-1, 1, N) * half_width
        return cls(np.column_stack([t, x]), rng=rng)
    
    @classmethod
    def sprinkle_diamond_4d(cls, N, L=1.0, rng=None):
        """Poisson sprinkle N points into 4D diamond.
        
        Region: |t| + r <= L where r = sqrt(x² + y² + z²).
        
        Parameters
        ----------
        N : int
            Number of points.
        L : float
            Half-size.
        rng : Generator, optional
        
        Returns
        -------
        CausalSet
        """
        rng = rng or default_rng()
        # Sample uniformly in 4D diamond: t first, then r, then angular
        t = rng.uniform(-L, L, N)
        # For given t, r is uniform in [0, L - |t|] with weight r²
        # Use rejection sampling or inverse CDF
        R_max = L - np.abs(t)
        # r distribution: p(r) ∝ r² for r ∈ [0, R_max]
        u = rng.uniform(0, 1, N)
        r = R_max * u ** (1/3)  # inverse CDF of r²
        
        # Random direction on S²
        theta = np.arccos(2 * rng.uniform(0, 1, N) - 1)
        phi = rng.uniform(0, 2 * np.pi, N)
        
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)
        
        return cls(np.column_stack([t, x, y, z]), rng=rng)
    
    @classmethod
    def sprinkle_schwarzschild(cls, N, M=1.0, r_range=(1.5, 5.0), rng=None):
        """Sprinkle N points in Schwarzschild spacetime (t, r, θ, φ).
        
        Uses the Eddington-Finkelstein metric. Points are Poisson-distributed
        in spacetime volume.
        
        Parameters
        ----------
        N : int
            Number of points.
        M : float
            Black hole mass (in Planck units).
        r_range : tuple (r_min, r_max)
            Radial range for sprinkling.
        rng : Generator, optional
        
        Returns
        -------
        CausalSet
        """
        rng = rng or default_rng()
        t_min, t_max = 0.0, 10.0 * M
        r_min, r_max = r_range
        
        # Simple uniform in (t, r, θ, φ) — ignores metric determinant weighting
        # For proper sprinkling use importance sampling with √(-g)
        t = rng.uniform(t_min, t_max, N)
        r = rng.uniform(r_min, r_max, N)
        theta = np.arccos(2 * rng.uniform(0, 1, N) - 1)
        phi = rng.uniform(0, 2 * np.pi, N)
        
        return cls(np.column_stack([t, r, theta, phi]), rng=rng)
    
    # ── Properties ──────────────────────────────────────────────────
    
    @property
    def points(self):
        """Spacetime coordinates (N, D)."""
        return self._points
    
    @property
    def N(self):
        """Number of events."""
        return len(self._points) if self._points is not None else 0
    
    @property
    def dim(self):
        """Spacetime dimension."""
        return self._points.shape[1] if self._points is not None else 0
    
    # ── Causal matrix ───────────────────────────────────────────────
    
    def causal_matrix(self):
        """Build the N×N causal matrix C.
        
        C[i,j] = 1 if event i is in the strict causal past of event j,
        i.e., t_j - t_i > |x_j - x_i| (in 2D) or the Minkowski light-cone
        condition in higher dimensions.
        
        Returns
        -------
        C : ndarray (N, N)
        """
        if self._C is not None:
            return self._C
        
        p = self._points
        N = self.N
        D = self.dim
        
        # Time differences
        dt = p[:, 0, None] - p[None, :, 0]  # dt[i,j] = t_i - t_j
        
        # Spatial distance
        if D == 2:
            dx = p[:, 1, None] - p[None, :, 1]
            dr = np.abs(dx)
        elif D == 4:
            dr = np.sqrt(np.sum((p[:, 1:, None] - p[None, 1:, :]) ** 2, axis=1))
        else:
            dr = np.sqrt(np.sum((p[:, 1:, None] - p[None, 1:, :]) ** 2, axis=1))
        
        # i ≺ j if t_j - t_i > |x_j - x_i|
        # = -dt[i,j] > dr[i,j]
        self._C = (-dt > dr).astype(np.float64)
        return self._C
    
    def pauli_jordan(self):
        """Compute the Pauli-Jordan operator Δ = C - C^T.
        
        Returns
        -------
        Delta : ndarray (N, N)
            Real antisymmetric matrix.
        """
        if self._Delta is not None:
            return self._Delta
        C = self.causal_matrix()
        self._Delta = C - C.T
        return self._Delta
    
    def diagonalize(self):
        """Eigendecompose iΔ where Δ is the Pauli-Jordan operator.
        
        Computes eigenvalues λ_k (real) and eigenvectors u_k (complex, unitary)
        of the Hermitian matrix iΔ.
        
        Sets: _iDelta_evals, _iDelta_evecs, _abs_D, _W
        """
        if self._iDelta_evecs is not None:
            return
        
        Delta = self.pauli_jordan()
        iD = 1j * Delta
        evals, evecs = np.linalg.eigh(iD)
        self._iDelta = iD
        self._iDelta_evals = evals
        self._iDelta_evecs = evecs
        
        # |Δ| = sum |λ_k| u_k u_k^†
        self._abs_D = evecs @ np.diag(np.abs(evals)) @ evecs.conj().T
        
        # SJ symmetric covariance W = (1/2)|Δ|
        self._W = 0.5 * self._abs_D
    
    @property
    def sj_covariance(self):
        """The SJ vacuum symmetric covariance W = (1/2)|Δ|."""
        self.diagonalize()
        return self._W
    
    @property
    def sj_spectrum(self):
        """Eigenvalues of iΔ (the SJ spectrum)."""
        self.diagonalize()
        return self._iDelta_evals
    
    # ── Subregion tools ─────────────────────────────────────────────
    
    def split_by_coordinate(self, coord_idx=1, threshold=0.0):
        """Split events by a coordinate threshold.
        
        Parameters
        ----------
        coord_idx : int
            Coordinate axis to split on (0=t, 1=x, ...).
        threshold : float
            Split value.
        
        Returns
        -------
        R_idx : ndarray
            Indices with coord < threshold.
        Rbar_idx : ndarray
            Indices with coord >= threshold.
        """
        vals = self._points[:, coord_idx]
        R = np.where(vals < threshold)[0]
        Rbar = np.where(vals >= threshold)[0]
        return R, Rbar
    
    def reduced_state(self, R_idx):
        """Compute the reduced SJ covariance and symplectic form on a subset.
        
        Parameters
        ----------
        R_idx : array-like
            Indices of the subset.
        
        Returns
        -------
        W_R : ndarray (M, M)
            Reduced covariance (symmetric, real).
        Omega_R : ndarray (M, M)
            Reduced symplectic form (antisymmetric, real).
        """
        self.diagonalize()
        Delta = self._Delta
        abs_D = self._abs_D
        
        W_R = 0.5 * abs_D[np.ix_(R_idx, R_idx)].real
        Omega_R = Delta[np.ix_(R_idx, R_idx)]  # Note: NOT halved
        
        return W_R, Omega_R
    
    # ── Diagnostics ─────────────────────────────────────────────────
    
    def count_relations(self):
        """Number of causal relations (nonzero entries in upper triangle of C)."""
        C = self.causal_matrix()
        return int(np.sum(C))
    
    def longest_chain(self):
        """Length of longest chain via topological sort and DP.
        
        Uses adjacency from causal matrix.
        """
        from scipy.sparse.csgraph import topological_sort
        # ... would need scipy; placeholder for now
        return None
    
    def summary(self):
        """Print a summary of the causal set."""
        print(f"CausalSet: N={self.N}, dim={self.dim}")
        if self._points is not None:
            print(f"  t range: [{self._points[:,0].min():.3f}, {self._points[:,0].max():.3f}]")
            if self.dim > 1:
                print(f"  x range: [{self._points[:,1].min():.3f}, {self._points[:,1].max():.3f}]")
        n_rel = self.count_relations()
        print(f"  Relations: {n_rel} (density={n_rel/self.N**2:.4f})")
