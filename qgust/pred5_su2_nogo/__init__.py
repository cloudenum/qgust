"""
Prediction 5: SU(2) holographic recovery fidelity bound.

Tests the claim that for SU(2) hyperinvariant tensor networks (HITs),
the holographic recovery fidelity F is bounded by:

    F ≤ 1 - d_min^{-2},   d_min = min_e (2j_e + 1)

where d_min is the minimum bond dimension across edges of the graph.
The bound follows from the no-go theorem for absolutely maximally
entangled (AME) states in SU(2) gauge theory (Otto et al. 2025).
"""

from .run import (
    su2_irrep_dim, clebsch_gordan,
    intertwiner_dimension, hit_recovery_fidelity, run_test
)
