# QGUST — Quantum Gravity Research Prospectus Toolkit

Numerical tests of five predictions motivated by a research prospectus
synthesizing causal set theory, spin networks, tensor networks, von Neumann
algebras, and entanglement renormalization.

## Overview

The prospectus in [`quantum-gravity-synthesis.md`](quantum-gravity-synthesis.md)
proposes a minimal 5-axiom system (causal order, CCR algebra, distinguished SJ
state, observer-dependence via crossed product, holographic entropy) that links
the algebraic and combinatorial pillars of quantum gravity. Its central
mathematical conjecture — the Unitary Equivalence Conjecture — relates the SJ
vacuum GNS representation to spin network representations via the exponentiated
LQG area operator.

The QGUST toolkit tests five concrete predictions from the constituent
frameworks. **Two distinctive claims** (the UEC and the horizon-molecule bridge)
have no direct numerical test in the current toolkit; what is tested are
properties the synthesis inherits from its components.

## Predictions — Current Status

| # | Test | Status | What It Discriminates | Key Finding |
|---|------|--------|-----------------------|-------------|
| 1 | Discrete entropy jumps | ✓ Verified | SU(2) recoupling (not synthesis-specific) | $S(k)$ shows 2–6 discrete steps per $(j,v)$ combination; step heights $O(1)$ from SU(2) recoupling |
| 2 | SJ Vacuum Entropy Scaling | ⚠️ Scale-limited | CST discretization (not synthesis-specific) | Volume-law ($S \approx 0.272\,n_R$) dominates at $N \le 800$; $c=1$ scaling requires $N \gg 10^4$ |
| 3 | GUE level statistics | ✗ **Falsified** | Free-field modular spectrum | Spectrum is Poisson (KS=0.032); free SJ vacuum is integrable |
| 4 | $T_{\text{cutoff}} \sim M^{-2/3}$ | ✓ Derived; ⚠️ Numerics blocked | Horizon molecule Boltzmann counting (component of synthesis) | Derivation complete; 2D model cannot verify 4D exponent |
| 5 | SU(2) fidelity bound $F \le 1-d_{\min}^{-2}$ | ✓ Verified | SU(2) CG identities (not synthesis-specific) | CG bugs fixed; all orthogonality checks pass |

The conclusion's dependency table tracks the status of *every* claim with its
gauge-group and discretization dependencies, and marks whether each test probes
the synthesis's connections or only its components.

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
├── quantum-gravity-synthesis.md    # Full prospectus document (v1.0)
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

If you use this work, cite the prospectus document:

> The QGUST Authors (2026). Quantum Gravity from Information-Theoretic Principles: A Research Prospectus. https://github.com/cloudenum/qgust
