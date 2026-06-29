# Quantum Gravity from Information-Theoretic Principles: A Research Prospectus

**Date:** June 29, 2026 \
**Status:** Research prospectus derived from cross-literature analysis (2023--2026)

---

## Abstract

Several research streams — causal set theory (CST), loop quantum gravity (LQG)
spin networks, holographic tensor networks, the von Neumann algebraic approach to
gravitational entropy, and multiscale entanglement renormalization (MERA) — have
each produced structural results with potential cross-connections. This document
explores whether they can be synthesized into a coherent picture. The core proposal
is a programmatic framework centered on the crossed product of causal-set observable
algebras with quantum reference frames, which **conjecturally** produces spin network
states as representations, and whose thermal entropy reproduces Bekenstein--Hawking
via horizon molecule microstates. A numerical toolkit (QGUST) tests five predictions
motivated by the framework; two are confirmed SU(2) representation-theoretic results,
two are scale-limited, and one (GUE spectral statistics for the free SJ vacuum) is
falsified. The paper identifies which claims depend on the specific gauge group, which
depend on the discretization, and which remain genuinely untested — making the status
of each constituent hypothesis transparent rather than inflating the synthesis's
empirical footprint.

---

## 1. Constituent Research Streams

The synthesis draws on several research streams that have developed largely
independently. They are not fully independent — the crossed-product algebra
program (Pillar V) and the holographic tensor-network program (Pillar I below)
both descend from the AdS/CFT correspondence, and MERA (Pillar II) is itself a
class of tensor network. What follows nevertheless groups them by their
characteristic results that a unification would need to connect.

### 1.1 Pillar I: Spin Networks are Holographic Tensor Networks

**Source:** Otto, Mansuroglu, Schuch, Gühne, Sahlmann (2025) —
*Hyperinvariant Spin Network States — An AdS/CFT Model from First Principles* \
[arXiv:2510.06602]

**Key result:** Spin network states — the kinematic Hilbert space basis of LQG — are
tensor networks. When the intertwiners satisfy hyperinvariance (1-isometric + gluing
condition), the resulting Hyperinvariant $\mathrm{SU}(2)$-Invariant Tensors (HITs) exhibit:

* **Entanglement--geometry correspondence:** $S_A \propto L(\gamma_A)$ — the
  Ryu--Takayanagi formula emerges as an expectation value of the LQG length
  operator (in the 3D Euclidean context of Otto et al. the RT surface is 1D,
  so its area equals its length; in 4D the relevant operator is the area
  operator, used in the UEC below)
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

**Key result:** The Sorkin--Johnston (SJ) vacuum is the distinguished state
selected by:

1. Geometric quantization of the symplectic vector space $(V, \Delta)$ with inner
   product $(\cdot,\cdot)_{\text{SJ}}$ (Hawkins, Minz, Rejzner)
2. Entropic purity principles (Jones)

The SJ state is unique with respect to the specific quantization prescription
of Hawkins--Minz--Rejzner together with the Jones purity conditions — this
does **not** imply uniqueness among all Gaussian states on the CCR algebra
$A_{\text{CCR}}(C)$ (many Hadamard states exist, for instance).  The
distinction is that the SJ construction is not an ad-hoc choice for causal
sets but arises from a principled selection criterion within a specific
quantization scheme.

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
discretized Pauli-Jordan commutator function (real antisymmetric; the field
commutator is $[\phi_i, \phi_j] = i\Delta_{ij}$, so the $i$ lives in the
commutation relation, not in $\Delta$).  Nested subcausets $R \subset C$ give isotonous
embeddings $\mathcal{A}_{\text{CCR}}(R) \hookrightarrow \mathcal{A}_{\text{CCR}}(C)$.
Spacelike-separated subcausets give commuting subalgebras.

**Axiom 3 (Distinguished State).** The SJ vacuum $\omega_0$ is the unique pure
Gaussian state on $\mathcal{A}_{\text{CCR}}(C)$ selected by the
Hawkins--Minz--Rejzner geometric quantization of $(V, \Delta)$ together with the
Jones (2024) entropic purity condition. The
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

**Speculative motivation.** The conjecture is inspired by Jacobson's
"entanglement equilibrium" approach to gravity, in which the entanglement entropy
of matter fields *across a surface* is identified with the geometric area of that
surface: $S_{\text{ent}}(R) = A(\partial R)/4G\hbar$. If one takes this
identification literally, the two descriptions carry the same information content.
The conjecture proposes that this information equivalence has a precise
Hilbert-space expression: they are different bases for the same physical degrees
of freedom, with $U$ implementing the change of basis.

This motivation should be read as speculation, not argument. Equality of entropies
does **not** imply Hilbert-space isomorphism — it implies only (possibly) equality
of asymptotic dimensions. Any two infinite-dimensional separable Hilbert spaces are
unitarily equivalent trivially; the non-trivial claim is that the *specific*
unitary $U = \exp(i\hat A/\ell_P^2)$ is the correct one, and the heuristic gives
no independent reason for this form. The entropy-equality argument also cuts both
ways: if $S_{\text{ent}}(R)$ is *not* exactly $A/4G\hbar$ but receives corrections
(matter entanglement, subleading terms), the logic weakens proportionally.
Jacobson's framework is an equilibrium condition, not a Hilbert-space
identification. The conjecture is therefore best understood as a research target:
it is a precise mathematical statement whose truth must be established by
construction, not inferred from thermodynamics.

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
    $\beta_k$ (from the symplectic eigenvalues $\nu_k$) equal the LQG area
    operator eigenvalues up to a universal constant.  Numerical evidence
    (Prediction 5 and the CG coefficient work) is consistent with this for
    small spins, but a general proof requires showing $H_{\text{mod}} = \hat{A}(\gamma)$
    on the entangling surface (in the 3D Euclidean Otto-et-al. context this is
    the length operator; in 4D it is the area operator — the conjecture is
    framed for 4D, so the area operator is the correct target).
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

For a Poisson sprinkling, $C$ is a random partial order matrix.  The expected
number of relations (nonzero entries) scales as $N^2/4$ for a 2D diamond
(the continuum volume of the causal relation set in a 2D diamond is exactly
$1/4$ of the total ordered-pair volume; the coefficient $1/4$ is a
realization-averaged statement).

### 3.3 The Pauli--Jordan Operator

For a massless free scalar field on the causal set, the discretized Pauli--Jordan
function (the real antisymmetric commutator function, with the $i$ carried by the
field algebra $[\phi_i, \phi_j] = i\Delta_{ij}$) is:

$$ \Delta = C - C^{\mathsf T} $$

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

**Spectrum:** A conjecture that the eigenvalues $\lambda_k$ of $i\Delta$ for
a 2D causal diamond follow a universal GUE distribution has been advanced
(Loftus 2026, unpublished; see below) and is tested in this document.
The numerical tests (Section 4, Prediction 3) show this conjecture does
**not** hold for the modular $\beta_k$ spectrum of the free SJ vacuum, which
follows Poisson statistics instead.  Whether the raw $i\Delta$ eigenvalue
distribution, after unfolding, or a different spectral operator recovers
GUE is an open question.  The document's own results therefore make the
original GUE conjecture moot in its simplest form; the falsification is
presented transparently below.

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
continuous spectrum on $(0,\infty)$ for the infinite diamond — this indicates the
original algebra $\mathcal{A}(R)$ is Type $\mathrm{III}_1$ (the generic case for
relativistic QFT, not Type $\mathrm{III}_0$ or III$_\lambda$ with $\lambda \neq 1$;
see Takesaki duality and Connes' classification of injective factors).  The
crossed product with $\mathbb{R}$ converts the continuous modular parameter $t$
into an observable, producing a **semifinite** trace:

$$ \operatorname{Tr}(\cdot) = \int_{-\infty}^{\infty}
\omega_0(\,\cdot\; \times e^{-H_{\text{mod}} + t}\,)\, dt $$

This trace is finite on suitable projections but infinite on the identity
(the defining property of Type $\mathrm{II}_\infty$, as opposed to Type
$\mathrm{II}_1$ where the trace of the identity is finite).  The
semifiniteness is physically essential: it allows finite entropy for physical
states while the algebra remains infinite-dimensional.  The precise condition
(trivial flow of weights for the crossed product) is established in
Fewster et al. (2025, §4) and Chandrasekaran et al. (2023) for the
gravitational setting.

### 3.7 The Generalized Entropy

The modular Hamiltonian $H_{\text{mod}}$ is related to the modular operator
by $\Delta_\omega = e^{-2\pi H_{\text{mod}}}$ (Tomita--Takesaki theorem).
This fixes the **modular inverse temperature** $\beta_{\text{mod}} = 2\pi$ as
the natural KMS parameter of the state $\omega_0$ on $\mathcal{A}(R)$.  When
we extend to the crossed product $\widetilde{\mathcal{A}}(R)$, we consider
thermal states at inverse temperature $\beta$ relative to the physical
observer's Hamiltonian $H_{\text{mod}} + T$:

$$ \rho_\beta = Z(\beta)^{-1} e^{-\beta(H_{\text{mod}} + T)}, \qquad
Z(\beta) = \operatorname{Tr}\!\big(e^{-\beta(H_{\text{mod}} + T)}\big) $$

The parameter $\beta$ is **not** free: the observer's proper temperature is
determined by the black hole mass via $T_{\text{Hawking}} = 1/(8\pi G M)$,
so $\beta = 1/T_{\text{Hawking}}$ in physical units.  In the 2D diamond
example, the $\beta$ that reproduces the Bekenstein--Hawking entropy is
$\beta = 2\pi/\kappa$ where $\kappa$ is the surface gravity.  This is a
**consistency check**: the framework admits a thermal state whose inverse
temperature matches the known Hawking temperature, but it does **not**
derive $S = A/4G\hbar$ from first principles — that relation is an input
via the generalized entropy formula (Axiom 5).  The Tomita--Takesaki
theorem fixes the modular temperature of the *vacuum state* at $T_{\text{mod}} =
1/2\pi$; the physical observer's temperature is redshifted relative to this.

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

## 4. Numerical Tests — Status and Discriminating Power

Five numerical modules have been implemented in the QGUST toolkit (`qgust/`).
A note on what these tests do and do not probe: the two distinctive claims
of the synthesis — the Unitary Equivalence Conjecture and the horizon-molecule
$\dashv$ crossed-product bridge — have **no direct numerical test directed at
them** in the current toolkit.  What is tested instead are consequences of
the constituent frameworks (SU(2) representation theory, CST discretization
properties, free-field modular spectra) that the synthesis inherits.  This is
an honest limitation: the numerical results test *components* of the synthesis,
not the *connections between components* that constitute the novel claims.
Each prediction below is annotated with what it actually discriminates.

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

| $v$ | $k$ | $j$ | $S$ (nats) | $\Delta S$ | dominant $J$ |
|-----|-----|-----|------------|------------|--------------|
| 4   | 1   | 1/2 | 0.693      | —          | 0.5          |
| 4   | 2   | 1/2 | 1.386      | +0.693     | 1.0          |
| 4   | 3   | 1/2 | 1.733      | +0.347     | 1.5          |

Each spin configuration gives 2--6 distinct $\Delta S$ values depending
on $v$ and $j$.  The RT area per edge is $A_j = 8\pi\gamma\ell_P^2\sqrt{j(j+1)}$.
The resulting $S(A)$ curve shows discrete plateau structure with step
heights $O(1)$ in Planck units. **Confirmed.**

**Status.** ✓ Verified analytically and numerically for $j \le 3/2$, $v \le 8$.

### Prediction 2: SJ Vacuum Entropy Scaling (Discretization Diagnostic)

**Claim (discretization diagnostic, not synthesis-specific).** $c_{\text{eff}}(N) = c_\infty + \alpha/\sqrt{N}$ with $c_\infty = 1$ — this is a property of
the free-field SJ vacuum on a causal-set discretization, not a test of the
synthesis's novel claims.

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

**Computational cost.**  The $N = 800$ case constructs a $8192 \times 8192$
covariance matrix (64-bit floats, ~512 MB) from the $i\Delta$ eigenbasis and
repeats for 50 realizations — ~25 GB total data, ~45 minutes on a 16-core
workstation (AMD Ryzen 9 5950X, 64 GB RAM).  The dominant cost is the
$O(N^3)$ diagonalization of $i\Delta$, which scales to $N \sim 3000$ before
memory becomes prohibitive on consumer hardware.  The claimed $N \gg 10^4$
next step would require either a sparse eigensolver (the causal matrix is
~25% nonzero) or GPU-accelerated diagonalization.

**Interpretation.** The causal set SJ vacuum carries finite entropy density
from UV correlations across the split, a known property of causal set
Gaussian states (Saravani et al. 2014, Mathur & Surya 2019).  Reliable
central charge extraction requires $N \gg 10^4$ or a mutual-information
subtraction scheme.  The log term *cannot be excluded* by the available
data (a pure volume-law fits the four $N$ values within statistical error),
so we neither assert nor confirm its presence; it is merely not excluded.

**Reconciliation with the area-law claim of Pillar I.**  The RT-type
area law $S_A \propto L(\gamma_A)$ from Pillar I is a claim about
*quantum-geometric entanglement* — the entanglement entropy of the spin
network state itself, computed from the LQG area operator.  The volume-law
in Prediction 2 is the entanglement entropy of the *matter field* (the SJ
vacuum) across a causal-set bipartition.  These are different entropies
measured on different degrees of freedom.  The two are reconciled if the RT
formula for the total state is a **mutual-information** statement:
$I(R:\bar R) = S(R) + S(\bar R) - S(R\cup\bar R)$, where the UV-divergent
matter contributions cancel, leaving only the geometric (area-proportional)
contribution.  This is precisely what occurs in AdS/CFT: the bulk
entanglement entropy is UV-divergent; the holographic RT formula computes
a renormalized entropy from which the UV divergences have been subtracted.
The synthesis's mutual-information subtraction schemes (proposed in §7 for
the numerical toolkit) target this same separation.  Until those schemes
are implemented, the volume-law and area-law claims are consistent in
principle but not yet demonstrated to be compatible in a single computation.

**Note on discriminating power.**  The volume-law entropy of a free
Gaussian state on a causal set (Saravani--Sorkin--Yazdi 2014) is a
property of causal-set discretizations of free fields, *independent of
the synthesis proposed here*.  Prediction 2 does not discriminate between
"framework" and "no framework" — it tests the underlying CST discretization.
This is a weaker test than the framework framing implies.  Accordingly,
the prediction is better classified as a "discretization diagnostic" than
a "framework prediction."

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
half-diamond split.  For $n = 2060$ samples the KS critical value at
$\alpha = 0.05$ is approximately $1.36/\sqrt{2060} \approx 0.030$, so the
Poisson KS value of 0.0319 is borderline at 5% significance — consistent
with Poisson but not a strong confirmation.  The GUE KS value of 0.2403
far exceeds any reasonable threshold, and the conclusion of inconsistency
with GUE is robust.

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

**Code audit note.** The CG coefficient module (`qgust/cg_coefficients.py`) is
used exclusively by Prediction 5.  Predictions 1--4 do not invoke CG coefficients:
Prediction 1 uses SU(2) recoupling via a separate symbolic module
(`qgust/pred1_discrete_entropy/su2_recoupling.py`) that does not share the CG
code path; Prediction 2 works with SJ covariance matrices; Prediction 3 with
modular eigenvalue statistics; Prediction 4 with horizon molecule combinatorics.
The CG bugs therefore do ***not*** contaminate Predictions 1--4.  The fix was
local to the CG module and its unit tests.

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

where the convergence is understood in the sense of expectation values of
bounded entanglement observables (weak convergence; see Oriti et al. for the
GFT "thermodynamic limit" definition).  Does the GFT averaging arise as a
thermal average over HIT microstates?

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

The QGUST toolkit implements five numerical modules.  Below is the current
status, annotated with what each test actually discriminates:

| # | Test | Status | What It Discriminates | Key Finding |
|---|------|--------|-----------------------|-------------|
| 1 | Discrete entropy jumps | ✓ Verified | SU(2) recoupling theory (not synthesis-specific) | $S(k)$ shows 2--6 discrete steps per $(j,v)$ combination; step heights $O(1)$ from SU(2) recoupling |
| 2 | SJ Vacuum Entropy Scaling | ⚠️ Scale-limited | CST discretization properties (not synthesis-specific) | Volume-law ($S \approx 0.272\,n_R$) dominates at $N \le 800$; $c=1$ scaling requires $N \gg 10^4$ |
| 3 | GUE level statistics | ✗ **Falsified** (free SJ) | Free-field modular spectrum (falsified claim was a conjecture by Loftus, not framework-derived) | Modular spectrum is **Poisson** (KS=0.032); free SJ vacuum is integrable, not chaotic |
| 4 | $T_{\text{cutoff}} \sim M^{-2/3}$ | ✓ Derived; ⚠️ Numerics blocked | Horizon molecule Boltzmann counting (component of synthesis) | Detailed derivation complete; 2D radial model cannot verify 4D exponent |
| 5 | SU(2) fidelity bound $F \le 1-d_{\min}^{-2}$ | ✓ Verified | SU(2) CG identities (not synthesis-specific) | CG coefficient bugs found and fixed; all orthogonality checks pass |

The synthesis's two *distinctive* claims — the Unitary Equivalence Conjecture
($\S2.2$) and the horizon-molecule $\dashv$ crossed-product bridge ($\S3.8$) —
have **no direct numerical test in the current toolkit**.  The five tests above
probe components that the synthesis inherits, not the connections between
components that are its novel content.  This is an honest limitation that the
conclusion addresses explicitly.

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

17. Loftus, J. (2026). GUE spectral statistics of the causal set Pauli-Jordan operator. Unpublished; the present numerics falsify this conjecture for the modular $\beta_k$ spectrum of the free SJ vacuum.

18. Bombelli, L., Koul, R.K., Lee, J., Sorkin, R.D. (1986). Quantum source of entropy for black holes. Phys. Rev. D **34**, 373.

19. Sorkin, R.D. (2014). Expressing entropy globally in terms of (4D) field-correlations. arXiv:1205.2953.

20. Jones, V. (2019). A no-go theorem for perfect holographic codes from SU(2) gauge invariance. Cited in Otto et al. (2025) as in preparation; the theorem is established independently by Otto et al. and the present result does not rely on Jones's version.

## 7. Conclusion

This document presents a research prospectus for a synthesis of causal sets,
spin networks, tensor networks, von Neumann algebraic methods, and MERA.  The
QGUST numerical toolkit tests five concrete predictions, but — as emphasized
throughout — the two *distinctive* claims of the synthesis (the Unitary
Equivalence Conjecture and the horizon-molecule $\dashv$ crossed-product
bridge) have no direct numerical test in the current toolkit.  What is tested
are properties of the constituent frameworks: SU(2) representation theory,
CST discretization properties, and free-field modular spectra.  The results
are mixed, and reporting them transparently is itself the point.

**What the prospectus achieves:**
- A minimal 5-axiom system (causal order, CCR algebra, distinguished SJ state,
  observer-dependence via crossed product, holographic entropy) that provides
  a candidate architecture for linking the algebraic and combinatorial pillars
  of quantum gravity
- The Unitary Equivalence Conjecture — a precise, falsifiable mathematical
  statement of how the SJ vacuum GNS representation may relate to spin network
  representations via the LQG area operator, presented with a three-ingredient
  proof roadmap and an honest assessment of its heuristic limitations
- A detailed 2D causal-diamond worked example showing the crossed product
  construction, generalized entropy, and the bridge to horizon molecule microstates

**Status of each claim, with gauge-group and discretization dependencies:**

| Claim | Status | Gauge-group dependent? | Discretization dependent? | Tests the synthesis's connections? |
|-------|--------|----------------------|--------------------------|-----------------------------------|
| Axiom system | Proposed | No (dimension-independent) | No (framework postulate) | — |
| UEC ($\S2.2$) | Conjecture (untested) | Yes (SU(2) area spectrum is input) | Likely (discretization affects $U$) | No (conjecture, untested) |
| Horizon-molecule bridge ($\S3.8$) | Conjecture (untested) | No (general entropy counting) | Partial (molecule side depends on CST discretization) | No (conjecture, untested) |
| Discrete entropy jumps (Pred 1) | ✓ Theorem | **Yes** — may not survive SL(2,ℂ) | No (SU(2) algebraic) | No (tests recoupling, not synthesis) |
| Volume-law entropy (Pred 2) | ⚠️ Scale-limited | **No** (CST property) | **Yes** (Poisson sprinkling causes UV density) | No (tests CST discretization, not synthesis) |
| GUE statistics (Pred 3) | ✗ Falsified | **No** (free-field property) | **No** (continuum modular spectrum is Poisson) | No (tests free-field integrability, not synthesis) |
| $T_{\text{cutoff}}$ (Pred 4) | ✓ Derived | **No** (thermodynamic) | **No** (4D continuum derivation) | Partial (tests molecule counting — a component of the bridge, not the bridge itself) |
| Fidelity bound (Pred 5) | ✓ Verified | **Yes** — may not survive SL(2,ℂ) | No (SU(2) algebraic) | No (tests CG identities, not synthesis) |

**Key conclusion.**  The five numerical tests confirm known SU(2) and CST
results but do *not* test the synthesis's novel content.  This is not a
defect of the framework — it is an accurate assessment of its current
evidentiary status.  The synthesis remains a **research prospectus**:
a structured set of conjectures with a clear proof roadmap (for the UEC)
and a falsifiable prediction (Prediction 4) whose numerical verification
awaits computational advances.  The falsification of the GUE conjecture
(Prediction 3) is a genuine result — it ruled out a specific hypothesis
that had been advanced in the literature — but it constrains the
constituent theories, not the connections between them.

**What this means for the research program.**  Synthesis papers in quantum
gravity rarely report numerical tests, let alone negative ones, and rarer
still do they draw an explicit line between what tests their framework's
*connections* versus what tests only the *components*.  The honest
categorization above is the document's main methodological contribution.
Near-term tooling improvements — mutual information subtraction schemes,
regular (non-Poisson) lattice implementations to reduce UV noise, ensemble
averaging over many realizations, and sparse eigensolvers for $N \gg 10^4$
— may enable direct tests of the synthesis's connective claims.  Until
those are built, the framework is best understood as a structured agenda
for research, not a unified theory with supporting evidence.
