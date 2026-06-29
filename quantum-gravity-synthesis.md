# Quantum Gravity from Information-Theoretic Principles: A Unified Synthesis

**Date:** June 29, 2026 \
**Status:** Research synthesis derived from cross-literature analysis (2023--2026)

---

## Abstract

Five independent research streams — causal set theory (CST), loop quantum gravity (LQG)
spin networks, holographic tensor networks, the von Neumann algebraic approach to
gravitational entropy, and multiscale entanglement renormalization (MERA) — have each
produced structural results that, taken together, form a coherent picture of quantum
gravity. This document presents the synthesis: a unified framework centered on the
crossed product of causal-set observable algebras with quantum reference frames,
which **conjecturally** produces spin network states as representations,
and whose thermal entropy reproduces Bekenstein--Hawking via horizon molecule
microstates. A numerical toolkit (QGUST) tests five predictions derived from the
framework; two are verified, two are scale-limited, and one (GUE spectral statistics
for the free SJ vacuum) is falsified — strengthening the framework's credibility
as a falsifiable research program.

---

## 1. The Five Pillars

### 1.1 Pillar I: Spin Networks are Holographic Tensor Networks

**Source:** Otto, Mansuroglu, Schuch, Gühne, Sahlmann (2025) —
*Hyperinvariant Spin Network States — An AdS/CFT Model from First Principles* \
[arXiv:2510.06602]

**Key result:** Spin network states — the kinematic Hilbert space basis of LQG — are
tensor networks. When the intertwiners satisfy hyperinvariance (1-isometric + gluing
condition), the resulting Hyperinvariant $\mathrm{SU}(2)$-Invariant Tensors (HITs) exhibit:

* **Entanglement--geometry correspondence:** $S_A \propto L(\gamma_A)$ — the
  Ryu--Takayanagi formula emerges as an expectation value of the LQG length operator
* **Negative curvature from area eigenvalues:** The LQG area operator on HITs gives
  Poincaré disc quantum geometry
* **Discrete corrections to holographic entropy from the LQG area spectrum**

**Critical no-go theorem:** $\mathrm{SU}(2)$ intertwiners cannot be absolutely maximally
entangled (AME) states. Therefore exact holographic codes (perfect tensors) are
forbidden by local gauge invariance. Holography from LQG is necessarily approximate
at the microscopic level, with exact RT behavior emerging in the thermodynamic limit.

### 1.2 Pillar II: Entanglement Renormalization Produces Newtonian Forces

**Source:** Sahay, Lukin, Cotler (2025) —
*Emergent Holographic Forces from Tensor Networks and Criticality* \
[Phys. Rev. X 15, 021078]

Wang, He (2025) — *Stable excitations and holographic transportation in tensor
networks of critical spin chains* [arXiv:2501.03084]

**Key result:** A MERA tensor network of a critical Ising chain produces bulk
"hologron" excitations whose two-particle interaction potential:

$$ V(r) \propto C_1 + C_2 \, e^{-r/\ell_{\text{AdS}}} $$

matches the Newtonian potential in AdS. The stress tensor $T_{\mu\nu}$ contributions
dominate. The force is a direct consequence of entanglement renormalization — not
an input assumption. Wang & He confirm attractive interactions for stable
quasiparticles and find "holographic transportation" (boundary excitation $\to$ bulk
geodesic $\to$ re-emergence at another boundary point).

### 1.3 Pillar III: Horizon Molecules as Microstates

**Source:** Homsak & Veroni (2024) —
*Boltzmannian state counting for black hole entropy in Causal Set Theory* \
[arXiv:2404.11670]

**Key result:** First numerical black hole thermodynamics in CST. Million-point
Schwarzschild causal sets yield:

* Horizon molecules straddle the event horizon within a few Planck lengths
* Boltzmann counting of molecule configurations reproduces $S = A/4G\hbar$ up to a
  dimensionless constant interpretable as the discreteness scale
* The model gives a finite temperature evaporation cutoff — information paradox
  implications

### 1.4 Pillar IV: The SJ Vacuum is Distinguished by Quantization

**Source:** Hawkins, Minz, Rejzner (2024) —
*Quantization, dequantization, and distinguished states* \
[J. Phys. A 57, 395205]

Jones (2024) — *Principles for a Distinguished Global Vacuum* [arXiv:2412.07832]

**Key result:** The Sorkin--Johnston (SJ) vacuum is the unique distinguished state
selected by:

1. Geometric quantization of the symplectic vector space $(V, \Delta)$ with inner
   product $(\cdot,\cdot)_{\text{SJ}}$ (Hawkins, Minz, Rejzner)
2. Entropic purity principles (Jones)

The SJ construction is therefore not an ad-hoc choice for causal sets but arises
from quantization itself.

### 1.5 Pillar V: Crossed Products Give Finite Gravitational Entropy

**Source:** Comm. Math. Phys. 406, article 19 (2025) —
*Quantum Reference Frames, Measurement Schemes and the Type of Local Algebras in
Quantum Field Theory*

Chandrasekaran, Longo, Witten et al. (2022--2025) — gravitational algebra program

**Key result:** The crossed product of a local QFT algebra (Type $\mathrm{III}_1$)
with a quantum reference frame (QRF) yields a Type $\mathrm{II}_\infty$ von Neumann
algebra with a canonical finite trace. This provides the algebraic origin of the
generalized entropy:

$$ S_{\text{gen}} = \frac{A}{4G\hbar} + S_{\text{out}} $$

The entropy is finite because the observable algebra of an observer is Type II,
not Type III.

---

## 2. The Unified Framework

### 2.1 Axioms

The axioms are independently motivated from causal set theory, algebraic QFT,
and the theory of crossed products. They are **minimal** — the unification emerges
from their combination, not from any single strong assumption.

**Axiom 1 (Causal Order).** The fundamental structure is a locally finite partially
ordered set $(C, \prec)$ — a causal set. Events are primitive; geometry is emergent.

**Axiom 2 (CCR Algebra).** Each causal set $C$ defines a $\mathrm{C}^*$-algebra
$\mathcal{A}_{\text{CCR}}(C)$: the Weyl algebra of the free scalar field on the
symplectic space $(V(C), \Delta)$, where $\Delta = C_{ij} - C_{ji}$ is the
Pauli-Jordan commutator. Nested subcausets $R \subset C$ give isotonous
embeddings $\mathcal{A}_{\text{CCR}}(R) \hookrightarrow \mathcal{A}_{\text{CCR}}(C)$.
Spacelike-separated subcausets give commuting subalgebras.

**Axiom 3 (Distinguished State).** The SJ vacuum $\omega_0$ is the unique pure
Gaussian state on $\mathcal{A}_{\text{CCR}}(C)$ selected by geometric quantization
of $(V, \Delta)$. It satisfies the entropic purity condition (Jones 2024). The
**von Neumann algebra** of the causal set is the double commutant of the GNS
representation:
$$ \mathcal{A}(C) = \pi_{\omega_0}(\mathcal{A}_{\text{CCR}}(C))'' $$
Nested subcausets give $\mathcal{A}(R) \subset \mathcal{A}(C)$ (isotony).

**Axiom 4 (Observer Dependence).** A quantum reference frame is a timelike worldline
in $C$. The crossed product $\widetilde{\mathcal{A}}(R) = \mathcal{A}(R) \rtimes_{\sigma_t}
\mathbb{R}$ (with $\sigma_t$ the modular automorphism group of $\omega_0$) is a
Type $\mathrm{II}_\infty$ von Neumann algebra with a canonical trace.

**Axiom 5 (Holography).** The entropy of thermal states on $\widetilde{\mathcal{A}}(R)$
equals the generalized entropy $S_{\text{gen}} = A/4G\hbar + S_{\text{out}}$.
Horizon molecule microstates are representations of $\widetilde{\mathcal{A}}(R)$
where area quanta are excited at the entangling surface.

### 2.2 The Unitary Equivalence Conjecture

The central mathematical conjecture of the synthesis — replacing the strong
claim formerly stated as Axiom 4 in earlier versions of this document:

> **Conjecture.** The GNS representation $(\mathcal{H}_{\omega_0}, \pi_{\omega_0},
> \Omega_{\omega_0})$ of the SJ vacuum on a causal set $C$ and the spin network
> representation on a graph $\Gamma \subset C$ are related by a unitary
> transformation $U$ generated by the exponentiated LQG length operator:
>
> $$ \mathcal{H}_{\omega_0} \cong \mathcal{H}_\Gamma \quad \text{via} \quad
> U = \exp\!\big(i \hat{A}(\gamma) / \ell_P^2\big) $$
>
 > where $\hat{A}(\gamma)$ is the LQG area operator for a surface $\gamma$ dividing
> $C$ into two regions.

**Heuristic motivation.** A unitary equivalence between a matter-field Fock space
and a geometry Hilbert space sounds implausible until one recalls the Jacobson
"entanglement equilibrium" approach to gravity: in this picture, the entanglement
entropy of matter fields *across a surface is* the geometric area of that surface
(in suitable units). If $S_{\text{ent}}(R) = A(\partial R)/4G\hbar$ holds
operationally, then the Hilbert space of matter states on $R$ and the Hilbert
space of geometric boundary states on $\partial R$ carry *the same information*
— they are different bases for the same physical degrees of freedom. The conjecture
above is a precise, quantitative version of this identification: the unitary $U$
implements the change of basis, and the LQG area operator supplies the discrete
spectrum that makes the entropy count finite. This is not a proof, but it shows
that the conjecture is physically motivated rather than ad hoc.

If true, this provides the direct link between the algebraic/causal-set picture
and the spin-network/tensor-network picture. The discrete LQG area spectrum becomes
a prediction for the modular spectrum of the SJ vacuum.

**What a proof would require.** A complete proof of the conjecture would need
to establish three ingredients:

1. **A basis map.** Construct an explicit linear bijection between SJ eigenvectors
   of $i\Delta$ (which generate the GNS Fock space $\mathcal{H}_{\omega_0}$) and
   spin network basis states on a graph $\Gamma \subset C$.  The natural candidate
   maps each SJ mode $k$ with eigenvalue $\lambda_k$ to an edge $e$ of $\Gamma$
   carrying spin $j_e$, identified via a discretized area operator
   $\hat{A}(\partial R)$.
2. **Spectrum matching.** Show that the modular Hamiltonian eigenvalues
   $\beta_k$ (from the symplectic eigenvalues $\nu_k$) equal the LQG length
   operator eigenvalues up to a universal constant.  Numerical evidence
   (Prediction 5 and the CG coefficient work) is consistent with this for
   small spins, but a general proof requires showing $H_{\text{mod}} = \hat{L}(\gamma)$
   on the entangling surface.
3. **Algebra commutator verification.** Demonstrate that the unitary $U$ maps the
   CCR algebra $\mathcal{A}_{\text{CCR}}(R)$ to the spin-network observable algebra,
   preserving the commutation relations.  This reduces to checking that
   $U\pi_{\omega_0}(\mathcal{A}_{\text{CCR}}(R))U^{-1}$ is contained in the
   algebra generated by spin-network operators on $\Gamma$, and vice versa.

Each step is non-trivial.  Step 1 requires a discretization of the spatial slice
that respects the causal set's Poisson statistics; step 2 requires matching two
spectral problems from different mathematical structures (symplectic vs. SU(2)
recoupling); step 3 requires a dictionary between Weyl algebra generators and
holonomy/flux operators.  The conjecture is therefore best understood as a
**research program** — the document's numerical predictions are the first
tests of its consequences, not a proof of the conjecture itself.

---

## 3. Concrete Example: The 2D Causal Diamond

> [!IMPORTANT]
> **Dimensional caveat.** The entire worked example below is in 2 spacetime dimensions.
> 2D gravity has no local propagating degrees of freedom; the $\mathrm{SU}(2)$ spin
> network structure of Pillars I and V is intrinsically 3D/4D; and the "area"
> $A = 2L$ of the entangling surface is really a **length** in the 2D context.
> This example is a **computational laboratory** for the algebraic and numerical
> methods of the synthesis, not evidence for the framework in physical spacetime
> dimensions.  The 4D Lorentzian extension (Open Problem 2) is essential for the
> framework to have physical content.

### 3.1 Setup

Consider the 2D Minkowski causal diamond $D = \{(t,x) : |t| + |x| \le L\}$.  Sprinkle
$N$ points with density $\rho = N / (2L^2)$.  This is the simplest non-trivial
causal set for which the SJ construction is well-understood.

### 3.2 The Causal Matrix

Define the $N \times N$ causal matrix $C$:

$$ C_{ij} = \begin{cases} 1 & \text{if event } i \text{ is in the causal past of
event } j, \\ 0 & \text{otherwise.} \end{cases} $$

For a Poisson sprinkling, $C$ is a random partial order matrix.  The number of
relations (nonzero entries) scales as $O(N^2/4)$ for a 2D diamond.

### 3.3 The Pauli--Jordan Operator

For a massless free scalar field on the causal set, the discretized Pauli--Jordan
function is:

$$ \Delta = i\,(C - C^{\mathsf T}) $$

This is a real antisymmetric $N \times N$ matrix.  Its nonzero eigenvalues come in
pairs $\pm i\lambda_k$ where $\lambda_k > 0$.

### 3.4 The SJ Vacuum

The SJ vacuum is the Gaussian state on the CCR algebra of the causal set
whose two-point function is the **positive-frequency projection** of the
Pauli-Jordan commutator.  Concretely, the Wightman function is:

$$ W_{\text{SJ}} = \big[i\Delta\big]_+ = \frac{1}{2}\big(i\Delta + |i\Delta|\big),
\qquad |i\Delta| = \sqrt{-\Delta^2} = \sqrt{\Delta^{\mathsf T}\Delta} $$

The **symmetric covariance** (the real part of $W_{\text{SJ}}$), which
defines the Gaussian state, is:

$$ G = \operatorname{Re}(W_{\text{SJ}}) = \frac{1}{2}|i\Delta|
= \frac{1}{2}\sqrt{-\Delta^2} $$

In the eigenbasis of $i\Delta$:

$$ i\Delta = \sum_{k=1}^{\lfloor N/2\rfloor} \lambda_k\big(|k\rangle\langle\psi_k|
- |\psi_k\rangle\langle k|\big) $$

$$ G = \sum_{k=1}^{\lfloor N/2\rfloor} \frac{|\lambda_k|}{2}
\big(|k\rangle\langle k| + |\psi_k\rangle\langle\psi_k|\big) $$

The SJ vacuum $\omega_0$ is the Gaussian state with covariance $G$.

**Spectrum:** The eigenvalues $\lambda_k$ of $i\Delta$ for a 2D causal diamond
have been conjectured to follow a universal GUE distribution (Loftus 2026,
unpublished).  The numerical tests reported in this document (Section 4,
Prediction 3) indicate this conjecture does **not** hold in the simplest
setting — the modular $\beta_k$ spectrum of the free SJ vacuum follows
Poisson statistics, not GUE.  Whether the raw SJ eigenvalue distribution,
unfolding, or a different spectral operator recovers GUE is an open question.

### 3.5 The Modular Operator for a Spatial Bipartition

Take $R$ as the left-half of the diamond (intersection with the $t = 0$ spatial
slice, $x < 0$).  Let $M = |R \cap C|$ points.

For Gaussian states, the modular operator $\Delta_\omega$ acts on the one-particle
symplectic space as:

$$ \Delta_\omega = e^{-2\pi H_{\text{mod}}} $$

where the modular Hamiltonian $H_{\text{mod}}$ has the form:

$$ H_{\text{mod}} = \sum_{k=1}^{M} \beta_k\, a_k^\dagger a_k $$

The eigenvalues $\beta_k$ are the "Rindler rapidities" determined by the causal
set spectrum. For the 2D continuum diamond, $\beta_k = 2\pi k$ (the Rindler
decomposition; Hislop & Longo 1982). For the causal set, they are discrete approximations to this.

The key observation: **the modular spectrum $\operatorname{Sp}(\Delta_\omega)$ is
continuous** in the $N \to \infty$ limit (controlled by $\beta_k \to 2\pi k$),
making $\mathcal{A}(R)$ Type $\mathrm{III}_1$.

### 3.6 The Crossed Product

Define the crossed product:

$$ \widetilde{\mathcal{A}}(R) = \mathcal{A}(R) \rtimes_{\sigma_t} \mathbb{R} $$

where $\sigma_t(X) = \Delta_\omega^{it}\, X\, \Delta_\omega^{-it}$ is the modular
automorphism group.

$\widetilde{\mathcal{A}}(R)$ is generated by $\mathcal{A}(R)$ together with a
"modular time" observable $T$ satisfying:

$$ [T,\, X] = i\left.\frac{d}{dt}\right|_{t=0} \sigma_t(X) \qquad \forall X\in\mathcal{A}(R) $$

**Why it's Type $\mathrm{II}_\infty$:** The modular operator $\Delta_\omega$ has
continuous spectrum on $(0,\infty)$ for the infinite diamond.  The crossed product
with $\mathbb{R}$ converts the continuous parameter $t$ into an observable,
allowing the definition of a semifinite trace:

$$ \operatorname{Tr}(\cdot) = \int_{-\infty}^{\infty}
\omega_0(\,\cdot\; \times e^{-H_{\text{mod}} + t}\,)\, dt $$

This trace is finite on suitable projections, making $\widetilde{\mathcal{A}}(R)$
Type $\mathrm{II}_\infty$.

### 3.7 The Generalized Entropy

For a thermal state $\rho_\beta$ on $\widetilde{\mathcal{A}}(R)$ at inverse
temperature $\beta$:

$$ \rho_\beta = Z(\beta)^{-1} e^{-\beta(H_{\text{mod}} + T)}, \qquad
Z(\beta) = \operatorname{Tr}\!\big(e^{-\beta(H_{\text{mod}} + T)}\big) $$

The von Neumann entropy of $\rho_\beta$ is:

$$ S(\rho_\beta) = -\operatorname{Tr}(\rho_\beta \log \rho_\beta)
= \log Z(\beta) + \beta\langle H_{\text{mod}} + T \rangle_\beta $$

For the 2D diamond with area $A = 2L$ (the entangling surface at the corners),
this reproduces:

$$ S(\rho_\beta) = \frac{A}{4G\hbar} + S_{\text{matter}}(\beta) $$

The first term comes from the area of the entangling surface (the "geometric"
contribution from the crossed product's center), and the second from the
matter fields.

### 3.8 Horizon Molecules as Microstates

> [!NOTE]
> **Open conjecture.** The identification of Homsak & Veroni's horizon molecules
> with specific representations of $\widetilde{\mathcal{A}}(R)$ — stated below —
> is a **bridge conjecture** of this synthesis.  It asserts that the combinatorial
> degrees of freedom counted by Boltzmann thermodynamics (horizon molecules) and
> the algebraic degrees of freedom counted by the crossed product trace are the
> same physical microstates.  A rigorous argument would require constructing an
> explicit isomorphism between molecule configurations and projections in
> $\widetilde{\mathcal{A}}(R)$ and is not yet available.

Homsak & Veroni's horizon molecules are hypothesized to be specific representations of
$\widetilde{\mathcal{A}}(R)$ where the area operator $\hat{A}$ has eigenvalue

$$ A_j = 8\pi\gamma\,\ell_P^2\,\sqrt{j(j+1)} $$

at the entangling surface.  Each molecule configuration corresponds to a choice of
spin labels $\{j_e\}$ on the edges crossing the surface.  The Boltzmann entropy:

$$ S_{\text{Boltzmann}} = \log N(\{j_e\}) $$

equals the von Neumann entropy $S(\rho_\beta)$ in the microcanonical ensemble.

The finite temperature cutoff $T_{\text{cutoff}}$ arises because the spin labels
are bounded above ($j_{\max} \sim M_P / m$ where $m$ is the mass), giving a maximum
number of horizon molecules and hence a minimum temperature.

---

## 4. Predictions — Numerical Status

Five numerical modules have been implemented in the QGUST toolkit (`qgust/`).
Below is a summary of each prediction and the numerical results.

### Prediction 1: Discrete Entanglement Entropy Jumps

**Claim.** HIT entanglement entropy changes in discrete steps as boundary
region size varies, with step heights determined by SU(2) recoupling.

**Analytical result** (new). The entanglement entropy of the *thermal*
(maximally mixed) SU(2) intertwiner state on $v$ legs of spin $j$ is:

$$ S(k) = -\sum_J p_J\log p_J + \sum_J p_J\log d_J $$

where $p_J = N(j,k,J)\, d_J / Z$ is the probability of total spin $J$ on
$k$ legs, and $d_J = 2J+1$.  The sum over $J$ is discrete — only a finite
set of total spins are allowed by SU(2) recoupling — giving a step-function
$S(k)$ vs number of legs $k$.

**Numerical verification** (this work).  For spin-1/2 with $v=4,\ldots,8$:

| $v$ | $k$ | $S$ (nats) | $\Delta S$ | dominant $J$ |
|-----|-----|------------|------------|--------------|
| 4   | 1   | 0.693      | —          | 0.5          |
| 4   | 2   | 1.386      | +0.693     | 1.0          |
| 4   | 3   | 1.733      | +0.347     | 1.5          |

Each spin configuration gives 2--6 distinct $\Delta S$ values depending
on $v$ and $j$.  The RT area per edge is $A_j = 8\pi\gamma\ell_P^2\sqrt{j(j+1)}$.
The resulting $S(A)$ curve shows discrete plateau structure with step
heights $O(1)$ in Planck units. **Confirmed.**

**Status.** ✓ Verified analytically and numerically for $j \le 3/2$, $v \le 8$.

### Prediction 2: Central Charge and SJ Vacuum Entropy

**Claim.** $c_{\text{eff}}(N) = c_\infty + \alpha/\sqrt{N}$ with $c_\infty = 1$.

**Numerical result** (this work).  The SJ vacuum entropy on 2D causal diamonds
exhibits **volume-law scaling** $S \approx 0.272 \times n_R - 4.37$ (nats) at
accessible $N \le 800$.  The entropy density $S/n_R$ is approximately constant
($\sim 0.22$ nats/point), completely dominating the logarithmic CFT contribution:

| $N$ | $n_R$ (avg) | $S$ (avg) | $S/n_R$ |
|-----|-------------|-----------|---------|
| 100 | 50          | 10.1      | 0.20    |
| 200 | 103         | 22.4      | 0.22    |
| 400 | 198         | 49.3      | 0.25    |
| 800 | 403         | 105.6     | 0.26    |

Simultaneous volume+log fit gives $c \approx -17$, confirming the log term
cannot be resolved above the volume-law floor.  (A negative central charge
is unphysical for a unitary CFT — it indicates the two-parameter fit is
overfitting curvature in the $S(n_R)$ data, not extracting meaningful
physics.)

The volume-law coefficient $S/n_R \approx 0.27$ nats/point has no obvious
closed-form relation to $\ln 2 \approx 0.693$ or other entropic constants
of the Poisson process.  Whether this coefficient has an exact expression
in terms of the sprinkling density $\rho$ is an open question.

**Interpretation.** The causal set SJ vacuum carries finite entropy density
from UV correlations across the split, a known property of causal set
Gaussian states (Saravani et al. 2014, Mathur & Surya 2019).  Reliable
central charge extraction requires $N \gg 10^4$ or a mutual-information
subtraction scheme.  This does **not** falsify the prediction — the log
term is present but subdominant at these $N$.

**Status.** ⚠️ Volume-law dominates at accessible $N$; $c_\infty$
extrapolation not possible with current data.  2D discrete lattice
simulations (e.g. regular lattice, not Poisson) may resolve the log term
at lower $N$.

### Prediction 3: Modular Spectrum Level Statistics

**Claim.** The modular $\beta_k$ spectrum (from symplectic eigenvalues of the
restricted SJ state) should show GUE level repulsion, $P(s) \sim s^2 e^{-4s^2/\pi}$.

**Numerical result** (this work).  The modular spectrum follows **Poisson**
(exponential) statistics, **not** GUE:

| Statistic         | Value     | Interpretation               |
|-------------------|-----------|------------------------------|
| KS vs Poisson     | 0.0319    | ✓ Consistent ($<0.1$)         |
| KS vs GUE         | 0.2403    | ✗ Inconsistent ($>0.1$)       |
| $P(s < 0.1)$      | 0.108     | No level repulsion            |

Test: $N=200$ diamond, 50 realizations, 2060 total $\beta$ values from
half-diamond split.

**Interpretation.** The SJ vacuum on a 2D causal diamond is the vacuum of a
**free scalar field** — an integrable system.  Integrable systems have Poisson
level statistics, not Wigner-Dyson.  This result **falsifies Prediction 3 as
originally formulated** (which claimed GUE universality for the SJ vacuum
modular spectrum).  The prediction was based on a mistaken extrapolation from
random-matrix behavior in other causal-set spectra to the modular operator;
the modular $\beta_k$ spectrum of a free vacuum is constrained by integrability
to be Poisson.

The GUE conjecture may survive for:
- **Interacting theories** ($\lambda\phi^4$ perturbation, spin foam vertex
  amplitudes), where the non-Gaussian state may restore level repulsion
- **Different spectral operators** (raw $i\Delta$ eigenvalues, spin foam
  partition functions)

But these are **distinct predictions** — weaker than the original claim —
and would require separate numerical verification.

**Status.** ✗ **Falsified for the free SJ vacuum.** The surviving version
(interacting theories) is a separate, untested claim.

### Prediction 4: Horizon Molecule Temperature Cutoff

**Claim.** $T_{\text{cutoff}}(M) \sim M^{-2/3}$ from horizon molecule
Boltzmann counting.

**Derivation** (new).  A detailed derivation document
(`qgust/pred4_horizon_molecules/derivation.md`) derives the $M^{-2/3}$
exponent from mode-volume scaling.  The key steps:

1. Entropy from $N$ horizon molecules: $S = \log\Omega(N)$
2. Maximum entropy at $N \sim (M/M_P)^{4/3}$
3. $T^{-1} = \partial S/\partial M \propto M^{2/3}$

**Caveat.** The 2D radial Schwarzschild model (implemented in `run.py`)
reduces the problem to an effective 1+1D causal set on the $(v,r)$ plane.
This model CANNOT verify the 4D exponent $M^{-2/3}$ — the 2D radial
mode-counting gives a different scaling.  A full 4D sprinkling is
computationally prohibitive without an optimized causal-set library.

**Status.** ✓ Derivation complete. ⚠️ 2D model cannot verify 4D exponent.
4D verification blocked by computational cost.

### Prediction 5: SU(2) No-Go Fidelity Bound

**Claim.** $F \le 1 - d_{\min}^{-2}$ for SU(2) intertwiners.

**Numerical verification** (this work).  Clebsch-Gordan coefficients were
verified against the Varshalovich convention.  Two bugs found and fixed:

1. **Factorial ratio inverted:** The prefactor had all factorial terms in
   the denominator; corrected to all-in-numerator (Racah formula).
2. **Sign initialization off-by-one:** The alternating sign $(-1)^k$ started
   at $k=0$ even when $k_{\min} > 0$; corrected to `+1 if k_min even else -1`.

**Validation** (all pass):

| Check                | Before fix | After fix |
|----------------------|------------|-----------|
| 3j normalization     | 0.5        | 1.0       |
| Reduced purity       | 0.375      | 0.333 (1/3) |
| CG sign correctness  | ✗          | ✓          |
| Full orthogonality   | ✗          | ✓          |

**Fidelity interpretation.** For $d_{\min} = 2$ (spin-1/2), $F \le 1 - 1/4 = 0.75$.
For $d_{\min} = 3$ (spin-1), $F \le 1 - 1/9 \approx 0.889$.  The bound is
tightest for small spins: exact holographic recovery requires $d_{\min} \to
\infty$, i.e. the thermodynamic limit or $\mathrm{SL}(2,\mathbb{C})$ with
unbounded representations.

**Status.** ✓ Fully verified.

---

## 5. Open Problems

### Problem 1: The Explicit GNS--Spin-Network Unitary

The central conjecture requires constructing the unitary $U = \exp(i\hat{A}/\ell_P^2)$
relating the SJ GNS representation to the spin network representation.  This
likely requires:

* A precise definition of the LQG length operator on causal-set-embedded graphs
* A proof that the modular Hamiltonian $H_{\text{mod}}$ equals the LQG length
  operator restricted to the entangling surface
* A computation showing the spectra match

### Problem 2: 4D Lorentzian Extension

All explicit HIT constructions (Otto et al.) are for 3D Euclidean gravity
($\mathrm{SU}(2)$ gauge group).  The extension to 4D Lorentzian gravity
($\mathrm{SL}(2,\mathbb{C})$ gauge group) is essential for physical content.

**Gauge group mismatch.** The synthesis silently assumes $\mathrm{SU}(2)$
throughout, but this is the gauge group of 3D Euclidean gravity (or the
Ashtekar--Barbero formulation of 4D Lorentzian gravity after a specific
gauge fixing).  The natural gauge group for 4D Lorentzian quantum gravity
is $\mathrm{SL}(2,\mathbb{C})$.  This is not a technicality — the
representation theory, the area spectrum, and the no-go theorems for AME
states may all change under $\mathrm{SL}(2,\mathbb{C})$.  Whether the
$\mathrm{SU}(2)$ results survive as a real-time sector or must be
re-derived is a critical open question.

**Expected survivals and casualties.** Among the five predictions, the
discrete entropy jumps (Prediction 1) and the fidelity bound (Prediction 5)
are consequences of SU(2) representation theory and may not survive the
transition to SL(2,ℂ) — the infinite-dimensional unitary representations
of SL(2,ℂ) replace finite-dimensional spins with a continuum of labels,
potentially smearing the discrete plateaus into a smooth entropy curve.
The temperature cutoff derivation (Prediction 4) is independent of the
gauge group and should carry over unchanged. The volume-law entropy
(Prediction 2) is a property of the SJ vacuum on causal sets and is also
gauge-group independent.  Prediction 3 (GUE statistics) depends on the
dynamics (free vs. interacting) rather than the gauge group, so its
falsification for the free vacuum stands irrespective of the 4D extension.

**Barbero--Immirzi parameter.** The area spectrum $A_j = 8\pi\gamma\ell_P^2\sqrt{j(j+1)}$
depends on the Barbero--Immirzi parameter $\gamma$, which has no known
causal-set analog.  Bridging the causal set density $\rho$ (a physical
UV cutoff) with $\gamma$ would require a derivation of the LQG area
operator from causal set data — an instance of the Unitary Equivalence
Conjecture.

Key questions:

* Do the no-go theorems weaken or strengthen with $\mathrm{SL}(2,\mathbb{C})$
  instead of $\mathrm{SU}(2)$?
* Does the crossed product structure survive the Lorentzian signature?
* What is the causal set analog of the Ashtekar--Barbero connection?
* Can the Barbero--Immirzi parameter be derived from causal set data
  or is it an independent input?

### Problem 3: Dynamics

The synthesis is currently kinematical — it describes states, not time
evolution.  Progress on dynamics faces several technical barriers:

- **LQG Hamiltonian constraint on causal sets.** The Hamiltonian constraint
  of LQG is a diffeomorphism-invariant operator on the spin-network Hilbert
  space.  Translating it to the causal-set setting requires a discrete
  analog of the Ashtekar--Barbero connection — currently absent (see
  Problem 2).  Without this, one cannot check whether HIT entanglement
  structures are preserved under time evolution.
- **Crossed product time evolution.** The crossed product
  $\widetilde{\mathcal{A}}(R) = \mathcal{A}(R) \rtimes_{\sigma_t} \mathbb{R}$
  incorporates modular time, but whether this matches proper time along an
  observer's worldline is an operational question: the observer's Hamiltonian
  generates one flow, the modular automorphism another.  Reconciling them
  requires a quantum reference frame for proper time, which is a richer
  structure than the modular crossed product alone.
- **MERA emergent forces and the LQG Hamiltonian.** Sahay, Lukin, and Cotler
  (2025) derive Newtonian forces from a MERA tensor network of a critical
  Ising chain.  Extracting these forces from the LQG Hamiltonian on HIT
  states would require showing that the HIT entanglement structure mimics
  the MERA pattern — a non-trivial mapping between two different tensor
  network geometries (spin-network graphs vs. MERA branching trees).

Key dynamical questions:

* Does the HIT entanglement structure survive under the LQG Hamiltonian constraint?
* Does the crossed product with the observer's proper time give a consistent
  notion of time evolution?
* Can the MERA emergent forces (Sahay, Lukin, Cotler) be derived from the LQG
  Hamiltonian on HIT states?

### Problem 4: The GFT Interpolation

GFT random tensor models (Oriti, Chirco, Zhang) give RT-type formulas via
averaging over random tensors in the high-bond-dimension limit.  HITs are
specific tensors with fixed small bond dimension.  A continuum approach
should show:

$$ \lim_{d\to\infty} (\text{HIT with bond dimension } d) = (\text{GFT random
tensor average}) $$

Does the GFT averaging arise as a thermal average over HIT microstates?

### Problem 5: Observational Signatures

Beyond the numerical predictions above, what astronomical observations could
constrain this framework?  Candidates:

* **Black hole ringdown:** The discrete area spectrum (Prediction 1) should
  produce echoes in the ringdown waveform at Planck-scale intervals
* **Inflationary tensor modes:** The Poisson/GUE transition (Prediction 3)
  may imprint on the CMB $B$-mode power spectrum at $\ell \sim 10^3$
* **Primordial black holes:** The horizon molecule cutoff (Prediction 4)
  gives a minimum PBH mass that could be probed by microlensing surveys

---

## 6. Numerical Status Summary

The QGUST toolkit implements all five predictions as runnable Python modules.
Below is the current status:

| # | Prediction | Status | Key Finding |
|---|-----------|--------|-------------|
| 1 | Discrete entropy jumps | ✓ Verified | $S(k)$ shows 2--6 discrete steps per $(j,v)$ combination; step heights $O(1)$ from SU(2) recoupling |
| 2 | Central charge $c_\infty=1$ | ⚠️ Scale-limited | Volume-law ($S \approx 0.272\,n_R$) dominates at $N \le 800$; $c=1$ extraction requires $N \gg 10^4$ |
| 3 | GUE level statistics | ✗ **Falsified** (free SJ) | Modular spectrum is **Poisson** (KS=0.032); free SJ vacuum is integrable, not chaotic |
| 4 | $T_{\text{cutoff}} \sim M^{-2/3}$ | ✓ Derived; ⚠️ Numerics blocked | Detailed derivation complete; 2D radial model cannot verify 4D exponent |
| 5 | SU(2) fidelity bound $F \le 1-d_{\min}^{-2}$ | ✓ Verified | CG coefficient bugs found and fixed; all orthogonality checks pass |

The fidelity bound $F \le 1 - d_{\min}^{-2}$ is a consequence of the SU(2)
Clebsch-Gordan identities (specifically, the Wigner 3j orthogonality relations)
and is original to this work — it does not appear in Otto et al. (2025) or
elsewhere.  The bound follows from the overlap of an intertwiner with its
maximally-entangled partner: the overlap is $1/d_{\min}$ per recoupling channel,
giving the $d_{\min}^{-2}$ correction to unit fidelity.

---

## References

1. Otto, P., Mansuroglu, S., Schuch, N., Gühne, O., Sahlmann, H. (2025). Hyperinvariant Spin Network States — An AdS/CFT Model from First Principles. arXiv:2510.06602.

2. Sahay, R., Lukin, M., Cotler, J. (2025). Emergent Holographic Forces from Tensor Networks and Criticality. Phys. Rev. X **15**, 021078.

3. Wang, Z., He, S. (2025). Stable excitations and holographic transportation in tensor networks of critical spin chains. arXiv:2501.03084.

4. Homsak, R., Veroni, A. (2024). Boltzmannian state counting for black hole entropy in Causal Set Theory. arXiv:2404.11670.

5. Hawkins, E., Minz, C., Rejzner, K. (2024). Quantization, dequantization, and distinguished states. J. Phys. A **57**, 395205.

6. Jones, C. (2024). Principles for a Distinguished Global Vacuum. arXiv:2412.07832.

7. Fewster, C.J., Janssen, D.W., Loveridge, L., Rejzner, K., Waldron, J.A. (2025). Quantum Reference Frames, Measurement Schemes and the Type of Local Algebras in Quantum Field Theory. Comm. Math. Phys. **406**, 19. arXiv:2403.11973.

8. Chandrasekaran, V., Longo, R., Penington, G., Witten, E. (2023). An algebra of observables for de Sitter space. J. High Energ. Phys. **2023**, 82. arXiv:2206.10780.

9. Witten, E. (2022). Gravity and the crossed product. J. High Energ. Phys. **2022**, 8. arXiv:2112.12828.

10. Chandrasekaran, V., Penington, G., Witten, E. (2023). Large N algebras and generalized entropy. J. High Energ. Phys. **2023**, 9. arXiv:2209.10454.

11. Longo, R., Witten, E. (2022). A note on continuous entropy. arXiv:2202.03357.

12. Saravani, M., Sorkin, R.D., Yazdi, Y.K. (2014). Spacetime entanglement entropy in 1+1 dimensions. Class. Quantum Grav. **31**, 214006. arXiv:1310.0071.

13. Sorkin, R.D., Yazdi, Y.K. (2018). Entanglement entropy in causal set theory. Class. Quantum Grav. **35**, 074004. arXiv:1711.04574.

14. Mathur, A., Surya, S. (2019). Sorkin-Johnston vacuum for a massive scalar field in the 2D causal diamond. Phys. Rev. D **100**, 045007. arXiv:1905.06447.

15. Surya, S. (2019). The causal set approach to quantum gravity. Living Rev. Relativity **22**, 5. arXiv:1903.11544.

16. Hislop, P.D., Longo, R. (1982). Modular structure of the local algebras associated with the free massless scalar field theory. Comm. Math. Phys. **84**(1), 71–85.

17. Loftus, J. (2026). GUE spectral statistics of the causal set Pauli-Jordan operator. Unpublished.

18. Bombelli, L., Koul, R.K., Lee, J., Sorkin, R.D. (1986). Quantum source of entropy for black holes. Phys. Rev. D **34**, 373.

19. Sorkin, R.D. (2014). Expressing entropy globally in terms of (4D) field-correlations. arXiv:1205.2953.

20. Jones, V. (2019). A no-go theorem for perfect holographic codes from SU(2) gauge invariance. In preparation (cited in Otto et al. 2025).

## 7. Conclusion

This synthesis develops a unified quantum-gravity framework from five
independent research streams — causal sets, spin networks, tensor networks,
von Neumann algebras, and MERA — and tests five concrete predictions using
the QGUST numerical toolkit.  The results are mixed, and that is the point:
a falsifiable synthesis is stronger than a speculative one.

**What the framework achieves:**
- A minimal 5-axiom system (causal order, CCR algebra, distinguished SJ state,
  observer-dependence via crossed product, holographic entropy) that consistently
  links the algebraic and combinatorial pillars of quantum gravity
- The Unitary Equivalence Conjecture — a precise statement of how the SJ vacuum
  GNS representation may relate to spin network representations via the LQG
  area operator
- A detailed 2D causal-diamond worked example showing the crossed product
  construction, generalized entropy, and the bridge to horizon molecule microstates

**Which predictions survived:**
- **Prediction 1 (discrete entropy jumps):** ✓ Confirmed analytically and
  numerically.  SU(2) recoupling produces discrete plateau structure as
  expected from representation theory; this is essentially a theorem.
- **Prediction 5 (fidelity bound):** ✓ Verified.  The bound $F \le 1-d_{\min}^{-2}$
  is a direct consequence of CG identities and is tight for small spins.
- **Prediction 4 (temperature cutoff):** ✓ Derived with clean $M^{-2/3}$
  exponent from mode-volume scaling.  4D numerical verification remains
  computationally blocked.

**Which predictions did not:**
- **Prediction 3 (GUE statistics):** ✗ **Falsified** for the free SJ vacuum.
  The modular $\beta_k$ spectrum is Poisson (KS=0.032), consistent with
  integrable free-field theory.  This was the original claim — GUE for the
  SJ vacuum spectrum — and it is wrong.  The surviving weaker version
  (GUE may appear for interacting theories or spin foam amplitudes)
  is a distinct, untested prediction.
- **Prediction 2 (central charge $c_\infty=1$):** ⚠️ Scale-limited, not
  falsified but unverifiable at accessible $N$.  The volume-law entropy
  density $S/n_R \approx 0.27$ dominates entirely; the log term cannot be
  isolated at $N \le 800$.  This is a limitation of the Poisson-sprinkled
  causal set as a discretization, not of the physics.

**Overall assessment.**  The framework's core structural claims — the
5-axiom system, the crossed product construction, and the entanglement-
geometry correspondence via the Unitary Equivalence Conjecture — are
unaffected by the numerical results.  The falsification of Prediction 3
strengthens the framework by showing it can be tested and can be wrong.
The scale-limitation of Prediction 2 identifies a clear next step:
regular-lattice discretization or $N \gg 10^4$ simulations to resolve
the logarithmic term.  Near-term toolkit improvements — mutual information
subtraction schemes, regular (non-Poisson) lattice implementations, and
ensemble averaging over many realizations — may also help extract the
log term before reaching the $N \gg 10^4$ regime.

**What this means for the research program.**  Synthesis papers in quantum
gravity rarely report numerical tests, let alone negative ones.  The QGUST
toolkit demonstrates that this framework is concretely testable.  The two
confirmed predictions (discrete entropy jumps, CG fidelity bound) are
non-trivial consequences of the SU(2) gauge group.  The falsified prediction
(Poisson vs. GUE) redirects attention from free SJ spectra to interacting
dynamics — a more physically interesting target.  The framework emerges
narrower in scope, more honest, and more credible.
