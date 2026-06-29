"""
Modular theory for causal set SJ vacua.

Computes the modular spectrum (symplectic eigenvalues of the reduced SJ state
on a subregion) and entanglement entropy, and compares against predictions from
LQG spin networks, U(1) gauge theory, and free CFT.
"""

import numpy as np
import math
from .causal_set import CausalSet


def symplectic_eigenvalues(W_R, Omega_R, rcond=1e-12):
    """Compute symplectic eigenvalues of the reduced SJ state.
    
    For a Gaussian state with covariance W_R and symplectic form Omega_R,
    the symplectic eigenvalues ν_k solve:
        det(W_R - ν_k * i*Omega_R) = 0
    
    Equivalently: eigenvalues of K = (i*Omega_R)^(-1) · W_R with ν ≥ 0.5.
    
    Parameters
    ----------
    W_R : ndarray (M, M)
        Real symmetric covariance matrix.
    Omega_R : ndarray (M, M)
        Real antisymmetric symplectic form.
    rcond : float
        Cutoff for pseudoinverse.
    
    Returns
    -------
    nu : ndarray
        Symplectic eigenvalues ν_k ≥ 0.5, sorted ascending.
    """
    iOmega = 1j * Omega_R
    iOmega_inv = np.linalg.pinv(iOmega, rcond=rcond)
    K = iOmega_inv @ W_R
    
    evals = np.linalg.eigvals(K)
    
    # Filter: positive real eigenvalues ≥ 0.5
    # ν = 0.5 exactly for the global pure state; ν > 0.5 for mixed subregions
    nu = evals.real[(np.abs(evals.imag) < 1e-8) & (evals.real > 0.45)]
    nu = np.sort(nu)
    # Clamp ν ≥ 0.5 (floating-point may give 0.499999...)
    nu = np.maximum(nu, 0.5)
    return nu


def entanglement_entropy(nu):
    """Compute von Neumann entanglement entropy from symplectic eigenvalues.
    
    For each mode with symplectic eigenvalue ν_k ≥ 0.5:
        S_k = (ν_k + 1/2) log(ν_k + 1/2) - (ν_k - 1/2) log(ν_k - 1/2)
    
    Parameters
    ----------
    nu : array-like
        Symplectic eigenvalues.
    
    Returns
    -------
    S_total : float
        Total entanglement entropy in nats.
    S_modes : ndarray
        Per-mode contributions.
    """
    nu = np.asarray(nu)
    S_modes = np.zeros_like(nu)
    for i, n in enumerate(nu):
        nup = n + 0.5
        num = abs(n - 0.5)
        if num < 1e-15:
            S_modes[i] = 0.0
        else:
            S_modes[i] = nup * math.log(nup) - num * math.log(num)
    return np.sum(S_modes), S_modes


def modular_ratio(nu):
    """Compute the modular spectrum ratio β₂/β₁.
    
    For LQG spin networks: β₂/β₁ = (3/2)^(1/3) ≈ 1.633
    For flat spectrum: β₂/β₁ = 1.0
    For U(1) gauge theory: β₂/β₁ = 2.0
    
    β_k = log((2ν_k + 1)/(2ν_k - 1))
    
    Parameters
    ----------
    nu : array-like
        Symplectic eigenvalues (should be > 0.5).
    
    Returns
    -------
    beta_ratio : float
        β₂/β₁ where β₁, β₂ are the two smallest β values.
    betas : ndarray
        All β values.
    """
    nu = np.asarray(nu)
    # Filter out ν ≈ 0.5 (pure modes) — they give β → ∞
    nu_valid = nu[nu > 0.501]
    if len(nu_valid) < 2:
        return float('nan'), np.array([])
    betas = np.array([math.log((2*n + 1)/(2*n - 1)) for n in nu_valid])
    sorted_betas = np.sort(betas)
    return sorted_betas[1] / sorted_betas[0], betas


def entropy_scaling_exponent(N_list, S_list):
    """Fit S(N) = a * log(N) + b to extract the scaling exponent.
    
    For 2D CFT with central charge c: S ~ (c/3) log(L/ε)
    Since N ∝ volume, and in 2D diamond volume ∝ L²:
        S ~ (c/6) log(N) + const
    
    Returns
    -------
    slope : float
        Fitted coefficient of log(N).
    """
    log_N = np.log(N_list)
    S = np.array(S_list)
    A = np.vstack([log_N, np.ones_like(log_N)]).T
    slope, intercept = np.linalg.lstsq(A, S, rcond=None)[0]
    return slope


def analyze_diamond(cs, R_idx, label="diamond"):
    """Full modular analysis of a causal set subregion.
    
    Parameters
    ----------
    cs : CausalSet
    R_idx : array-like
        Subregion indices.
    label : str
        Label for printing.
    
    Returns
    -------
    result : dict
        nu, S_total, beta_ratio, etc.
    """
    W_R, Omega_R = cs.reduced_state(R_idx)
    nu = symplectic_eigenvalues(W_R, Omega_R)
    
    if len(nu) < 2:
        return {"nu": nu, "S_total": 0.0, "beta_ratio": float('nan'), "n_modes": len(nu)}
    
    S_total, S_modes = entanglement_entropy(nu)
    beta_ratio, betas = modular_ratio(nu)
    
    result = {
        "nu": nu,
        "S_total": S_total,
        "S_modes": S_modes,
        "beta_ratio": beta_ratio,
        "betas": betas,
        "n_modes": len(nu),
        "nu_mean": np.mean(nu),
        "nu_std": np.std(nu),
        "R_size": len(R_idx),
    }
    
    print(f"  [{label}] R_size={len(R_idx):5d}  modes={len(nu):3d}  "
          f"S={S_total:.4f}  β₂/β₁={beta_ratio:.4f}  "
          f"ν∈[{nu.min():.4f}, {nu.max():.4f}]  ⟨ν⟩={np.mean(nu):.4f}±{np.std(nu):.4f}")
    
    return result


def region_entropy(cs, idx):
    """Convenience: entanglement entropy of a causal set subregion.
    
    Parameters
    ----------
    cs : CausalSet
    idx : array-like
        Indices defining the subregion.
    
    Returns
    -------
    S : float
        Entropy in nats, or 0.0 if region too small.
    """
    if len(idx) < 3:
        return 0.0
    W_R, Omega_R = cs.reduced_state(idx)
    nu = symplectic_eigenvalues(W_R, Omega_R)
    if len(nu) < 1:
        return 0.0
    S, _ = entanglement_entropy(nu)
    return S


def tripartite_info(cs, t1, t2):
    """Tripartite mutual information I₃(A:B:C) for an exhaustive tripartition.
    
    Splits the diamond at x = t1, t2 into three exhaustive regions:
      A: x < t1,  B: t1 ≤ x < t2,  C: x ≥ t2
    covering the full diamond (A∪B∪C = full system).
    
    For a pure global state:
      I₃ = S(A) + S(C) - S(A∪B) - S(B∪C)
    
    In a 2D CFT, I₃ is UV-finite and proportional to c. For a volume-law
    dominated state, I₃ ≈ -2α·|B| (does NOT cancel — use with caution).
    
    Parameters
    ----------
    cs : CausalSet
        Must already be diagonalized.
    t1, t2 : float
        x-coordinate split points (t1 < t2).
    
    Returns
    -------
    I3 : float
        Tripartite information.
    components : dict
        Individual entropies and sizes.
    """
    x = cs.points[:, 1]
    
    A = np.where(x < t1)[0]
    B = np.where((x >= t1) & (x < t2))[0]
    C = np.where(x >= t2)[0]
    AB = np.where(x < t2)[0]
    BC = np.where(x >= t1)[0]
    
    SA = region_entropy(cs, A)
    SC = region_entropy(cs, C)
    SAB = region_entropy(cs, AB)
    SBC = region_entropy(cs, BC)
    
    # Exhaustive pure-state formula: I₃ = SA + SC - SAB - SBC
    I3 = SA + SC - SAB - SBC
    
    return I3, {
        "SA": SA, "SB": region_entropy(cs, B), "SC": SC,
        "SAB": SAB, "SBC": SBC,
        "nA": len(A), "nB": len(B), "nC": len(C),
    }


# ── References for comparison ───────────────────────────────────────

LQG_BETA_RATIO = 1.633  # (3/2)^(1/3) from hyperinvariant intertwiner spectrum
U1_BETA_RATIO = 2.0     # U(1) gauge theory
FLAT_BETA_RATIO = 1.0   # Free scalar flat spectrum
CFT_C_ESTIMATE = 1.0    # For 2D Ising/diamond

SCALING_EXPECTATION = {
    "cft_scalar_2d": 1/6,      # S ~ (c/3)*log(N)/2
    "cft_ising_2d": 1/12,      # c=1/2
    "diamond_cft": 1/6,        # c=1
}
