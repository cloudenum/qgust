# QGUST — Quantum Gravity Unified Synthesis Toolkit

Numerical tests of five predictions from a unified quantum-gravity framework combining causal set theory, spin networks, tensor networks, von Neumann algebras, and entanglement renormalization.

## Overview

Five research streams — causal set theory (CST), loop quantum gravity (LQG) spin networks, holographic tensor networks, the von Neumann algebraic approach to gravitational entropy, and multiscale entanglement renormalization (MERA) — have each produced structural results that form a coherent picture of quantum gravity. This project:

1. **Presents the synthesis** in [`quantum-gravity-synthesis.md`](quantum-gravity-synthesis.md) — a 700-line document with a minimal 5-axiom system, the Unitary Equivalence Conjecture, and a detailed 2D causal-diamond worked example.
2. **Tests five predictions** via the numerical QGUST toolkit (`qgust/`).

## Predictions — Current Status

| # | Prediction | Status | Key Finding |
|---|-----------|--------|-------------|
| 1 | Discrete entanglement entropy jumps from SU(2) recoupling | ✓ Verified | $S(k)$ shows 2–6 discrete steps per $(j,v)$ combination; step heights $O(1)$ from representation theory |
| 2 | Central charge $c_\infty=1$ from SJ vacuum entropy | ⚠️ Scale-limited | Volume-law ($S \approx 0.272\,n_R$) dominates at $N \le 800$; $c=1$ extraction requires $N \gg 10^4$ |
| 3 | GUE level statistics from modular $\beta_k$ spectrum | ✗ **Falsified** | Modular spectrum is Poisson (KS=0.032); free SJ vacuum is integrable, not chaotic |
| 4 | Horizon molecule temperature cutoff $T_{\text{cutoff}} \sim M^{-2/3}$ | ✓ Derived; ⚠️ Blocked | Derivation from mode-volume scaling complete; 2D model cannot verify 4D exponent |
| 5 | SU(2) fidelity bound $F \le 1-d_{\min}^{-2}$ | ✓ Verified | CG coefficient bugs found and fixed; all orthogonality checks pass |

## Repository Structure

```
qgust/
├── qgust/                          # Python package
│   ├── core/                       # Core numerical infrastructure
│   │   ├── causal_set.py           # Causal set sprinkling, causal matrix, SJ spectrum
│   │   └── modular.py              # Symplectic eigenvalues, entropy, modular ratio, tripartite info
│   ├── pred1_entropy_jumps/run.py  # Discrete entropy jumps via SU(2) recoupling
│   ├── pred2_central_charge/run.py # SJ vacuum entropy scaling
│   ├── pred3_gue_statistics/run.py # Modular β spectrum level statistics
│   ├── pred4_horizon_molecules/    # Schwarzschild causal set + entropy scaling
│   │   ├── run.py
│   │   └── derivation.md           # T_cutoff derivation
│   ├── pred5_su2_nogo/run.py       # SU(2) CG coefficients, intertwiners, fidelity bound
│   └── cli.py                      # CLI entry point
├── tests/test_modular.py           # 6/6 tests passing
├── quantum-gravity-synthesis.md    # Full synthesis document (v0.3)
├── pyproject.toml
└── README.md
```

## Requirements

- Python 3.13+
- NumPy 2.5+

No SciPy dependency. CG coefficients for $j>5$ may overflow Python's integer factorial.

## Quick Start

```bash
python -m qgust.cli --help
python tests/test_modular.py        # Run test suite
```

## Licensing

- **Code** (the `qgust/` package, tests, and all `.py` files): MIT License — see [`LICENSE`](LICENSE).
- **Document** ([`quantum-gravity-synthesis.md`](quantum-gravity-synthesis.md)): Creative Commons Attribution 4.0 International (CC-BY-4.0).

## Citation

If you use this work, cite the synthesis document:

> The QGUST Authors (2026). Quantum Gravity from Information-Theoretic Principles: A Unified Synthesis. https://github.com/cloudenum/qgust
