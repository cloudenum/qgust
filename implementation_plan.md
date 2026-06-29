# Quantum Gravity Unified Simulation Toolkit (QGUST)

A Python-based numerical simulation toolkit to test the five predictions from the *Quantum Gravity from Information-Theoretic Principles* synthesis.

## Overview

The toolkit is organized as a Python package (`qgust`) with five simulation modules — one per prediction — plus shared core infrastructure for causal sets, spin networks, and tensor networks. All computations are CPU-based (NumPy/SciPy), with optional GPU acceleration via JAX for large causal sets.

---

## Proposed Changes

### Project Structure

```
qgust/
├── pyproject.toml              # [NEW] Project metadata & dependencies
├── README.md                   # [NEW] Usage guide and theory summary
│
├── qgust/                      # [NEW] Main package
│   ├── __init__.py
│   │
│   ├── core/                   # Shared infrastructure
│   │   ├── __init__.py
│   │   ├── causal_set.py       # Causal set sprinkling & causal matrix
│   │   ├── sj_vacuum.py        # Sorkin-Johnston vacuum construction
│   │   ├── spin_network.py     # SU(2) spin network states & area operator
│   │   ├── tensor_network.py   # Tensor network utilities (wraps quimb)
│   │   └── modular.py          # Modular operator, crossed product, entropy
│   │
│   ├── pred1_entropy_jumps/    # Prediction 1: Discrete S_A jumps on HITs
│   │   ├── __init__.py
│   │   ├── hit_construction.py # Hyperinvariant intertwiner construction
│   │   ├── entropy.py          # Entanglement entropy vs boundary size
│   │   └── run.py              # CLI entry point & plotting
│   │
│   ├── pred2_central_charge/   # Prediction 2: c_eff(N) scaling
│   │   ├── __init__.py
│   │   ├── scaling.py          # SJ vacuum at varying N, extract c_eff
│   │   └── run.py              # CLI entry point & plotting
│   │
│   ├── pred3_gue_statistics/   # Prediction 3: GUE universality
│   │   ├── __init__.py
│   │   ├── spectral.py         # Level spacing analysis & Wigner surmise fit
│   │   └── run.py              # CLI entry point & plotting
│   │
│   ├── pred4_horizon_molecules/# Prediction 4: Temperature cutoff
│   │   ├── __init__.py
│   │   ├── molecules.py        # Horizon molecule counting & thermodynamics
│   │   └── run.py              # CLI entry point & plotting
│   │
│   └── pred5_su2_nogo/         # Prediction 5: Recovery fidelity bound
│       ├── __init__.py
│       ├── fidelity.py         # SU(2) intertwiner code analysis
│       └── run.py              # CLI entry point & plotting
│
├── notebooks/                  # [NEW] Jupyter notebooks for exploration
│   ├── 01_causal_set_basics.ipynb
│   ├── 02_sj_vacuum_2d.ipynb
│   ├── 03_hit_entropy.ipynb
│   ├── 04_gue_statistics.ipynb
│   └── 05_horizon_molecules.ipynb
│
└── tests/                      # [NEW] Unit tests
    ├── test_causal_set.py
    ├── test_sj_vacuum.py
    ├── test_spin_network.py
    ├── test_predictions.py
    └── conftest.py
```

---

### Core Infrastructure

#### [NEW] `qgust/core/causal_set.py`

Causal set generation and manipulation.

- **`CausalSet` class**: Represents a causal set as a DAG
  - `sprinkle_diamond_2d(N, L)` — Poisson sprinkle `N` points into 2D Minkowski diamond $|t|+|x| \le L$
  - `sprinkle_diamond_4d(N, L)` — 4D extension
  - `sprinkle_schwarzschild(N, M, r_range)` — Sprinkle into Schwarzschild spacetime
  - `causal_matrix()` → $N \times N$ sparse boolean matrix $C_{ij}$
  - `link_matrix()` → Transitive reduction (irreducible relations only)
  - `longest_chain()`, `antichain_width()` — Dimension estimators
  - Uses `scipy.sparse` for $N > 10^4$; dense NumPy for smaller sets

- **Complexity**: Sprinkling is $O(N)$; causal matrix construction is $O(N^2)$ pairwise comparisons (parallelizable). Practical limit: $N \sim 10^5$ on desktop (16 GB RAM for dense matrix = $N^2 \times 1$ byte $\approx$ 10 GB).

#### [NEW] `qgust/core/sj_vacuum.py`

Sorkin-Johnston vacuum construction.

- **`SJVacuum` class**:
  - Takes a `CausalSet` and computes:
    1. Pauli-Jordan matrix: $\Delta = i(C - C^T)$
    2. Eigendecomposition of $i\Delta$ → eigenvalues $\{\pm \lambda_k\}$
    3. Positive part: $W_{\text{SJ}} = \frac{1}{2}(i\Delta + |i\Delta|)$ — the two-point function / Wightman matrix
  - `eigenvalues()` → sorted positive eigenvalues $\lambda_k$
  - `wightman_matrix()` → $W$ matrix
  - `covariance_matrix()` → Gaussian state covariance for entropy computations

- **Algorithm**: Full eigendecomposition via `scipy.linalg.eigh` for antisymmetric matrices. For $N > 5000$, use iterative methods (`scipy.sparse.linalg.eigsh` on $\Delta^T \Delta$) to get top-$k$ eigenvalues.

- **Known pitfall**: The SJ vacuum is real-valued on the causal set, but the Wightman function requires careful handling of the positive/negative frequency split. We follow Mathur & Surya (2019) conventions.

#### [NEW] `qgust/core/spin_network.py`

SU(2) spin network states and operators.

- **`SpinNetwork` class**:
  - Defined on a graph $\Gamma$ (NetworkX graph) with edges labeled by half-integer spins $j_e$
  - `area_eigenvalue(j)` → $8\pi\gamma \ell_P^2 \sqrt{j(j+1)}$
  - `area_spectrum(j_max)` → Full sorted area spectrum up to $j_{\max}$
  - `intertwiner_space(vertex)` → Dimension and basis of intertwiner space at a vertex (Clebsch-Gordan decomposition via `sympy.physics.quantum.cg`)
  - `evaluate(connection)` → Evaluate spin network function on a discretized $SU(2)$ connection

- **`AreaOperator` class**:
  - Acts on spin network Hilbert space for a given surface $\gamma$
  - `spectrum()` → Eigenvalues with multiplicities
  - `degeneracy(A)` → Number of spin configurations giving total area $A$

#### [NEW] `qgust/core/tensor_network.py`

Thin wrapper around `quimb` for tensor network operations.

- `build_mera(chi, num_layers)` — Construct a binary MERA with bond dimension $\chi$
- `build_hit(graph, spins)` — Construct hyperinvariant tensor from SU(2) intertwiners
- `entanglement_entropy(tn, region)` — Compute $S_A$ for a boundary region via SVD
- `contract(tn)` — Full contraction (exact or approximate via `quimb.tensor`)

#### [NEW] `qgust/core/modular.py`

Modular theory and crossed product computations.

- **`ModularOperator` class**:
  - Takes a Gaussian state covariance $W$ restricted to a subregion $R$
  - Computes modular Hamiltonian eigenvalues $\beta_k$ from the restricted Wightman function
  - `spectrum()` → $\{e^{-2\pi\beta_k}\}$
  - `entropy(beta)` → Von Neumann entropy of thermal state at inverse temperature $\beta$
  - `crossed_product_trace(f)` → Evaluates the semifinite trace $\text{Tr}(f) = \int \omega_0(f \cdot e^{-H_{\text{mod}} + t}) dt$

- **`generalized_entropy(W, region, beta)`** → Computes $S_{\text{gen}} = A/(4G\hbar) + S_{\text{matter}}$

---

### Prediction Modules

#### [NEW] `qgust/pred1_entropy_jumps/`

**Goal**: Demonstrate discrete jumps in holographic entanglement entropy on HIT spin networks.

**Algorithm**:
1. Construct a HIT tensor network on a regular tree graph (Bethe lattice) with specified spins $\{j_e\}$
2. For each boundary subregion size $|A| = 1, 2, \ldots, |B|$:
   - Compute $S_A$ via SVD of the reduced density matrix
   - Compute $L(\gamma_A)$ — the minimal cut through the HIT network (Ryu-Takayanagi surface), with length given by LQG area eigenvalues on crossed edges
3. Plot $S_A$ vs $L(\gamma_A)$ — expect piecewise linear with discrete steps

**Key parameters**: Graph valence $v \in \{3, 4, 5, 6\}$, spins $j \in \{1/2, 1, 3/2, 2\}$, number of layers $\ell \in \{3, 4, 5, 6\}$

**Expected output**: Plots showing step-function behavior with step heights $\Delta S \sim O(1)$ in Planck units

#### [NEW] `qgust/pred2_central_charge/`

**Goal**: Show $c_{\text{eff}}(N) = c_\infty + \alpha / \sqrt{N}$ convergence.

**Algorithm**:
1. For each $N \in \{100, 316, 1000, 3162, 10000, 31623, 100000\}$:
   - Generate $M = 50$ independent Poisson sprinklings of 2D causal diamond
   - Compute SJ vacuum for each
   - Extract entanglement entropy $S(l)$ for subregions of size $l$
   - Fit $S(l) = (c/3) \log(l/\epsilon) + \text{const}$ to extract $c_{\text{eff}}(N)$
   - Average over $M$ samples
2. Fit $c_{\text{eff}}(N)$ vs $N$ to the scaling form $c_\infty + \alpha N^{-1/2}$
3. Extrapolate $c_\infty$ and compare with $c = 1$

**Computational cost**: The bottleneck is eigendecomposition at $N = 10^5$ ($O(N^3)$ for full, $O(N^2 k)$ for iterative top-$k$). At $N = 10^5$ with full decomposition: ~hours per sample. We'll use iterative methods for large $N$ and only compute the top $O(\sqrt{N})$ eigenvalues.

> [!IMPORTANT]
> The $N = 10^5$ case will be very slow with full eigendecomposition (~hours per sample on a modern CPU). We'll provide an option to use iterative/truncated methods that sacrifice accuracy on deep IR modes but are sufficient for $c_{\text{eff}}$ extraction.

#### [NEW] `qgust/pred3_gue_statistics/`

**Goal**: Verify GUE level spacing statistics in the SJ vacuum spectrum.

**Algorithm**:
1. Generate causal set, compute $i\Delta$, get eigenvalues $\{\lambda_k\}$
2. Unfold the spectrum: $\tilde{\lambda}_k = \bar{N}(\lambda_k)$ where $\bar{N}$ is the mean cumulative level count (polynomial fit)
3. Compute nearest-neighbor spacings $s_k = \tilde{\lambda}_{k+1} - \tilde{\lambda}_k$
4. Normalize: $\bar{s} = 1$
5. Histogram $P(s)$ and fit to:
   - Wigner surmise (GUE): $P(s) = (32/\pi^2) s^2 e^{-4s^2/\pi}$
   - Poisson: $P(s) = e^{-s}$
   - GOE: $P(s) = (\pi/2) s \, e^{-\pi s^2/4}$
6. Compute $\chi^2$ goodness-of-fit for each ensemble

**Extension**: Repeat for spin foam vertex amplitude spectrum (compute EPRL vertex amplitude for given boundary spins, extract eigenvalues of the amplitude matrix).

#### [NEW] `qgust/pred4_horizon_molecules/`

**Goal**: Compute horizon molecule configurations and derive temperature cutoff.

**Algorithm**:
1. Generate Schwarzschild causal set with $N$ points near horizon
2. Identify horizon molecules: pairs $(p, q) \in C$ with $p$ inside and $q$ outside the horizon, $|r_p - r_H|, |r_q - r_H| < \delta$ (a few Planck lengths)
3. Count molecule configurations $N(\{j_e\})$ that give total area $A = A_H \pm \delta A$
4. Compute Boltzmann entropy $S = \log N$ and compare with $A/(4G\hbar)$
5. Find maximum entropy $S_{\max}(M)$ and derive cutoff temperature:
   $$T_{\text{cutoff}} = \left(\frac{\partial S_{\max}}{\partial E}\right)^{-1}$$
6. Compare with predicted formula $T_{\text{cutoff}} = \frac{\hbar}{8\pi G M}\left(\frac{M}{M_P}\right)^{1/3}$

> [!NOTE]
> The Schwarzschild sprinkling follows the approach of Homsak & Veroni (2024) and the MSci_Schwarzschild_Causets repository. We'll adapt their methodology for our framework.

#### [NEW] `qgust/pred5_su2_nogo/`

**Goal**: Verify the SU(2) no-go bound on holographic recovery fidelity.

**Algorithm**:
1. For a graph $\Gamma$ with valence $v$ and edge spins $\{j_e\}$:
   - Compute the intertwiner space $\text{Inv}(\bigotimes_e V_{j_e})$ at each vertex
   - Construct the HIT tensor from these intertwiners
   - Attempt to construct a holographic code: encode a bulk qudit into boundary spins
   - Compute recovery fidelity $F$ using the Knill-Laflamme conditions
2. Compare with the predicted bound $F \le 1 - d_{\min}^{-2}$ where $d_{\min} = \min_e(2j_e + 1)$
3. Scan over $j \in \{1/2, 1, 3/2, \ldots, 5\}$ and $v \in \{3, 4, 5, 6\}$

---

### Dependencies

```
numpy >= 1.24
scipy >= 1.11
matplotlib >= 3.7
networkx >= 3.1
sympy >= 1.12
quimb >= 1.8
tqdm >= 4.65
```

Optional:
```
jax[cpu]          # GPU/TPU acceleration for large N
jupyterlab        # Notebook exploration
pytest            # Testing
```

---

## User Review Required

> [!IMPORTANT]
> **Language choice**: The plan uses pure Python (NumPy/SciPy) for all core computations. For $N > 10^4$ causal sets, performance will be a bottleneck. Options:
> - **(a)** Stay pure Python — simpler, but $N = 10^5$ takes hours per eigendecomposition
> - **(b)** Use JAX for GPU-accelerated linear algebra — faster, but adds complexity
> - **(c)** Write critical inner loops in C/C++ with pybind11 — fastest, most complex
>
> My recommendation: Start with **(a)** for correctness, add **(b)** later as optional acceleration. Thoughts?

> [!IMPORTANT]
> **Scope for initial version**: The full toolkit covers all 5 predictions. Should I:
> - **(a)** Build all 5 modules in one pass (comprehensive but larger initial effort)
> - **(b)** Start with Predictions 2 and 3 (SJ vacuum + GUE statistics) since they share the core causal set infrastructure, then iterate
> - **(c)** Start with Prediction 1 (HIT entropy) since it's the most visually striking result
>
> My recommendation: **(b)** — Predictions 2 & 3 share the heaviest core infrastructure (causal set + SJ vacuum), and GUE statistics is the most directly testable claim. Once those work, the others layer on naturally.

## Open Questions

> [!NOTE]
> **Barbero-Immirzi parameter**: The area spectrum formula $A_j = 8\pi\gamma\ell_P^2\sqrt{j(j+1)}$ depends on the Barbero-Immirzi parameter $\gamma$. Common values: $\gamma = \ln 2 / (\pi\sqrt{3}) \approx 0.2375$ (Dreyer/Meissner), $\gamma = 0.2740$ (newer computations). Which value should we use as default? I'll make it configurable with $\gamma = 0.2375$ as default.

> [!NOTE]
> **Causal diamond size**: For the 2D diamond, the paper uses $L$ as the half-size. For numerical work, we set $L = 1$ (dimensionless) and vary $N$ (sprinkling density = $N/2$). This is equivalent to varying $\rho = N/(2L^2)$ at fixed $L$. Confirm this is the intended parameterization?

> [!NOTE]
> **Visualization style**: Should plots follow a specific journal style (PRL, CQG, etc.), or is a clean matplotlib style with LaTeX labels sufficient for now?

## Verification Plan

### Automated Tests

```bash
pytest tests/ -v                       # Unit tests
python -m qgust.pred2_central_charge.run --N 100 300 1000 --samples 5  # Quick smoke test
python -m qgust.pred3_gue_statistics.run --N 500 --samples 10          # GUE fit test
```

**Validation checks**:
- `test_causal_set.py`: Verify causal matrix is upper-triangular (after topological sort), transitivity, correct relation count scaling $O(N^2/4)$
- `test_sj_vacuum.py`: Verify $W$ is positive semidefinite, $W - W^* = i\Delta/2$, eigenvalue positivity
- `test_spin_network.py`: Verify area eigenvalues match known LQG spectrum, intertwiner dimensions match Clebsch-Gordan counting
- `test_predictions.py`: Small-$N$ regression tests against known analytical results (e.g., 2D diamond with $N = 50$, known $c = 1$ in continuum limit)

### Manual Verification

- Reproduce Figure 2 of Mathur & Surya (2019) — SJ Wightman function on 2D causal diamond
- Reproduce GUE level spacing statistics for random antisymmetric matrices as a control
- Visual inspection of $S_A$ vs $L(\gamma_A)$ plots for discrete jump structure
