"""
Prediction 4: Horizon molecule temperature cutoff.

Tests the claim that the SJ vacuum on a Schwarzschild causal set produces
a modified Hawking temperature:

    T_cutoff = (hbar / 8pi G M) * (M / M_P)^(1/3)

The 1/3 exponent is tested by computing the entanglement entropy of the
exterior region at varying black hole mass M, extracting the effective
temperature, and fitting the scaling T(M) ~ M^{-2/3}.
"""

from .run import SchwarzschildCausalSet, run_test, plot_scaling
