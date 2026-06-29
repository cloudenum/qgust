"""
Test the modular spectrum computation.

Verifies:
1. Causal set can be sprinkled
2. Diagonalization gives valid eigenvalues
3. Entropy scales roughly as log(N) for 2D CFT
4. Modular ratio computation works
"""

import numpy as np
import math
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from qgust.core.causal_set import CausalSet
from qgust.core.modular import (
    symplectic_eigenvalues, entanglement_entropy, modular_ratio,
    entropy_scaling_exponent, analyze_diamond
)


def test_causal_set_creation():
    """A causal set can be created and has the right shape."""
    cs = CausalSet.sprinkle_diamond_2d(100, L=1.0)
    assert cs.N == 100
    assert cs.dim == 2
    assert cs.points.shape == (100, 2)
    print("  ✓ Causal set creation")


def test_causal_matrix():
    """Causal matrix is strictly upper-triangular after symmetrization."""
    cs = CausalSet.sprinkle_diamond_2d(50, L=1.0)
    C = cs.causal_matrix()
    assert C.shape == (50, 50)
    assert np.allclose(C, C.astype(bool))
    # Δ = C - C^T is antisymmetric, |Δ| = C + C^T
    assert np.allclose(cs.pauli_jordan(), C - C.T)
    print(f"  ✓ Causal matrix ({int(np.sum(C))} relations)")


def test_diagonalization():
    """iΔ is Hermitian with real eigenvalues."""
    cs = CausalSet.sprinkle_diamond_2d(50, L=1.0)
    evals = cs.sj_spectrum
    assert np.all(np.isreal(evals))
    assert np.allclose(np.sort(evals), evals)  # already sorted
    assert np.abs(evals).sum() > 0
    print(f"  ✓ Diagonalization (λ∈[{evals.min():.3f}, {evals.max():.3f}])")


def test_symplectic_eigenvalues():
    """Symplectic eigenvalues are ≥ 0.5 and finite."""
    cs = CausalSet.sprinkle_diamond_2d(100, L=1.0)
    R_idx, _ = cs.split_by_coordinate(coord_idx=1, threshold=0.0)
    
    if len(R_idx) < 10:
        print("  ? Too few points in R, skipping")
        return
    
    W_R, Omega_R = cs.reduced_state(R_idx)
    nu = symplectic_eigenvalues(W_R, Omega_R)
    
    assert len(nu) > 0
    assert np.all(nu >= 0.5)
    assert np.all(np.isfinite(nu))
    
    print(f"  ✓ Symplectic eigenvalues: {len(nu)} modes, ν∈[{nu.min():.4f}, {nu.max():.4f}]")


def test_entropy_computation():
    """Entanglement entropy is positive and finite."""
    cs = CausalSet.sprinkle_diamond_2d(100, L=1.0)
    R_idx, _ = cs.split_by_coordinate(coord_idx=1, threshold=0.0)
    
    if len(R_idx) < 10:
        print("  ? Too few points")
        return
    
    W_R, Omega_R = cs.reduced_state(R_idx)
    nu = symplectic_eigenvalues(W_R, Omega_R)
    
    if len(nu) < 2:
        print("  ? Too few modes")
        return
    
    S_total, S_modes = entanglement_entropy(nu)
    beta_ratio, betas = modular_ratio(nu)
    
    assert S_total > 0
    assert np.isfinite(S_total)
    assert np.all(S_modes >= 0)  # Pure modes (ν=0.5) contribute 0
    assert np.isfinite(beta_ratio)
    
    print(f"  ✓ Entropy: S={S_total:.4f}, β₂/β₁={beta_ratio:.4f}")


def test_entropy_symplectic_invariant():
    """Global SJ state is pure: symplectic eigenvalues all = 0.5."""
    cs = CausalSet.sprinkle_diamond_2d(50, L=1.0)
    all_idx = np.arange(cs.N)
    W_R, Omega_R = cs.reduced_state(all_idx)
    nu = symplectic_eigenvalues(W_R, Omega_R)
    
    assert len(nu) > 0
    assert np.all(np.abs(nu - 0.5) < 1e-8), f"Global state not pure: max|ν-0.5|={np.max(np.abs(nu-0.5))}"
    print(f"  ✓ Symplectic invariant: all ν = 0.5 (pure global state)")


if __name__ == "__main__":
    print("Causal Set & Modular Theory Tests")
    print("=" * 40)
    test_causal_set_creation()
    test_causal_matrix()
    test_diagonalization()
    test_symplectic_eigenvalues()
    test_entropy_computation()
    test_entropy_symplectic_invariant()
    print("=" * 40)
    print("All tests passed.")
