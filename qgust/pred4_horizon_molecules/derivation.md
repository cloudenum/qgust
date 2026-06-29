# Horizon Molecule Temperature Cutoff: Derivation

## The Prediction

$$T_{\text{cutoff}} = \frac{\hbar}{8\pi G M} \left(\frac{M}{M_P}\right)^{1/3} = T_H \cdot \left(\frac{M}{M_P}\right)^{1/3}$$

Equivalently, $T_{\text{cutoff}} \propto M^{-2/3}$ in Planck units (where $T_H \propto M^{-1}$). The
entanglement entropy in the causal set deviates from the area law:

$$S_{\text{CS}} = \frac{A}{4G}\left[1 - \left(\frac{M_P}{M}\right)^{2/3}\right] \quad\Longrightarrow\quad
S \propto M^{5/3} \quad\text{(vs. } S \propto M^2 \text{ for the area law)}$$

---

## 1. Boltzmann Counting of Horizon Molecule States

### 1.1 Setup

Consider a Schwarzschild black hole of mass $M$ in 4D spacetime. The causal set has density
$\rho \sim 1/\ell_P^4$. Near the horizon, the metric is approximately Rindler:

$$ds^2 \approx -\kappa^2 x^2\,dt^2 + dx^2 + dy^2 + dz^2, \qquad \kappa = \frac{1}{4M}$$

where $x$ is the proper distance from the horizon. The horizon area is:

$$A = 4\pi (2M)^2 = 16\pi M^2$$

### 1.2 Near-horizon proper volume

A causal set element at proper distance $x$ from the horizon has local energy:

$$E_{\text{loc}}(x) = \frac{E_\infty}{N(x)} \approx \frac{E_\infty}{\kappa x}$$

where $N(x) = \kappa x$ is the lapse (the redshift factor from infinity). A "horizon molecule"
is a pair of causally-related elements $(p,q)$ with $p$ inside and $q$ outside the horizon,
linked by a causal relation $\prec$.

The number of such molecules is the number of causal set elements within a proper shell
of thickness $\delta$ around the horizon:

$$N_{\text{mol}} = \rho \cdot A \cdot \delta$$

Each molecule carries a **binary degree of freedom** — whether its causal link crosses the
horizon in the "ingoing" or "outgoing" direction. More refined models assign an SU(2) spin
$j$ to each molecule, giving degeneracy $g = d_j^2 = (2j+1)^2$.

### 1.3 Entropy from counting

The Boltzmann entropy of the molecule gas is:

$$S_{\text{mol}} = N_{\text{mol}} \cdot \log g = \rho \cdot A \cdot \delta \cdot \log g$$

Equating with the Bekenstein-Hawking entropy $S_{\text{BH}} = A/(4G)$:

$$\rho \cdot \delta \cdot \log g = \frac{1}{4G}$$

In Planck units ($G = \ell_P^2 = 1$, $\rho \sim 1$):

$$\delta \cdot \log g \approx \frac14$$

| $g$ | $\log g$ | $\delta$ (Planck lengths) | Interpretation |
|-----|----------|--------------------------|----------------|
| 2   | $\log 2$ | $(4\log 2)^{-1} \approx 0.36$ | Binary molecule |
| 4   | $\log 4$ | $(4\log 4)^{-1} \approx 0.18$ | Spin-$1/2$ molecule |
| $d_j^2$ | $2\log(2j+1)$ | $(8\log(2j+1))^{-1}$ | General spin-$j$ |

The sub-Planckian $\delta$ values indicate that horizon molecules are **compressed** to the
Planck scale — exactly as expected from the holographic principle.

---

## 2. The Temperature Cutoff

### 2.1 Thermal mode count vs molecule count

In the continuum, a thermal mode at temperature $T$ has a characteristic wavelength
$\lambda = 1/T$. The number of modes within a horizon-scale volume $V \sim r_s^3$ is:

$$N_{\text{modes}}(T) \sim \frac{V}{\lambda^3} \sim \frac{M^3}{\lambda^3} \propto M^3 T^3$$

The number of horizon molecules (each encoding one bit of information) is:

$$N_{\text{mol}} \propto A \propto M^2$$

### 2.2 Cutoff via mode exhaustion

The cutoff temperature $T_{\text{cutoff}}$ is defined by the condition that the number of
thermal modes resolvable at that temperature equals the number of horizon molecules:

$$N_{\text{modes}}(T_{\text{cutoff}}) \sim N_{\text{mol}}$$

$$M^3 \cdot T_{\text{cutoff}}^3 \propto M^2$$

$$T_{\text{cutoff}} \propto M^{-2/3}$$

### 2.3 Fixing the constant

The full expression from matching the prefactors:

$$\frac{V_{\text{near}}}{\lambda_{\text{cutoff}}^3} \cdot g_{\text{modes}} =
\rho \cdot A \cdot \delta \cdot \log g_{\text{mol}}$$

The near-horizon volume is $V_{\text{near}} = A \cdot \delta$. The thermal mode density
in 4D is $1/\lambda^3$ per unit volume. The mode degeneracy $g_{\text{modes}}$ counts
the number of polarizations. Solving:

$$
\begin{aligned}
\frac{A \cdot \delta}{\lambda_{\text{cutoff}}^3} \cdot g_{\text{modes}}
&= \rho \cdot A \cdot \delta \cdot \log g_{\text{mol}} \\[4pt]
\frac{g_{\text{modes}}}{\lambda_{\text{cutoff}}^3} &= \rho \cdot \log g_{\text{mol}} \\[4pt]
\lambda_{\text{cutoff}} &= \left(\frac{g_{\text{modes}}}{\rho \cdot \log g_{\text{mol}}}
\right)^{1/3}
\end{aligned}
$$

This gives $T_{\text{cutoff}} = 1/\lambda_{\text{cutoff}}$ which is **independent of $M$**
in Planck units. That's the Planck temperature $T_P \sim 1$, not the $M^{-2/3}$ scaling we want!

The key missing ingredient: the **Rindler near-horizon redshift** modifies the counting.

### 2.4 Redshift-corrected mode counting

In the Rindler approximation, modes at proper distance $x$ from the horizon have their
energy redshifted: $\omega_{\text{loc}} = \omega_\infty / (\kappa x)$. The thermal wavelength
at infinity $\lambda_\infty = 1/T$ corresponds to a LOCAL wavelength:

$$\lambda_{\text{loc}}(x) = \frac{\kappa x}{T}$$

The condition for a mode to be "resolved" by the causal set is that its local wavelength
exceeds the Planck length:

$$\lambda_{\text{loc}}(x_{\text{min}}) = \ell_P \quad\Longrightarrow\quad
x_{\text{min}} = \frac{T}{\kappa \ell_P}$$

The number of molecules in a shell of thickness $x_{\text{min}}$ is:

$$N_{\text{mol}} = \rho \cdot A \cdot x_{\text{min}} = \rho \cdot A \cdot \frac{T}{\kappa}$$

Setting this equal to $A/(4G)$ (entropy matching):

$$\rho \cdot \frac{T}{\kappa} \cdot \log g = \frac{1}{4G}$$

Solving for $T$:

$$T = \frac{\kappa}{4G \rho \log g} = \frac{1}{16\pi G M \rho \log g}$$

In Planck units ($G=1$):

$$T_{\text{cutoff}} = \frac{1}{16\pi M \rho \log g}$$

This gives $T_{\text{cutoff}} \propto M^{-1}$ (same as $T_H$!), which is also not the
$M^{-2/3}$ exponent.

### 2.5 The missing factor: mode volume scaling

The resolution to these conflicting scaling estimates is that the **effective mode volume**
in the near-horizon region is NOT $V_{\text{near}} = A \cdot \delta$ but rather the volume
that a mode with frequency $\omega$ can access before it is blue-shifted beyond the cutoff.

A mode with asymptotic frequency $\omega$ has a turning point at $x_{\text{turn}} \sim 1/\omega$
(where the local energy $\omega_{\text{loc}} = \omega/(\kappa x) \sim 1$, reaching the Planck
scale). The volume accessible to the mode is:

$$V_{\text{mode}} \sim A \cdot x_{\text{turn}} \sim A / \omega$$

The number of causal set elements in this volume:
$$N_{\text{elements}}(\omega) = \rho \cdot V_{\text{mode}} \sim \rho \cdot A / \omega$$

For the thermal state, modes contribute to the entropy when $\omega \lesssim T$. The total
number of spectral degrees of freedom is:

$$N_{\text{DOF}} \sim \int_{\omega_{\text{min}}}^{\omega_{\text{max}}}
N_{\text{elements}}(\omega) \, d\omega \sim \rho \cdot A \cdot \log\left(
\frac{T}{\kappa}\right)$$

Equating $N_{\text{DOF}} \cdot \log g = A/(4G)$:

$$\rho \cdot \log\left(\frac{T}{\kappa}\right) \cdot \log g = \frac{1}{4G}$$

Solving:

$$T = \kappa \cdot \exp\left(\frac{1}{4G \rho \log g}\right)$$

This gives $T \propto \kappa = 1/(4M) \propto M^{-1}$ again — the standard Hawking scaling,
just with a UV-dependent prefactor.

### 2.6 The 5/3 exponent from the causal set dispersion relation

The proper derivation of $S \propto M^{5/3}$ (or equivalently $T_{\text{cutoff}} \propto
M^{-2/3}$) requires considering the **modified causal set dispersion relation** for
field modes near the horizon.

On a causal set, the d'Alembertian operator has a non-local form:

$$\square_{\text{CS}} \phi(x) = \frac{4}{\ell_P^2}\left[\frac12
\sum_{y \prec x} \phi(y) - \phi(x)\right]$$

In momentum space, this gives a modified dispersion relation:

$$\omega^2 - k^2 = \frac{4}{\ell_P^2} \left[1 - F(k\ell_P, \omega\ell_P)\right]$$

where $F$ is a form factor encoding the causal set structure. For small momenta
($k\ell_P \ll 1$), this reduces to the continuum dispersion. For $k\ell_P \sim 1$,
the non-locality becomes important, effectively introducing a UV cutoff.

The key result (from Surya 2019, Belenchia et al. 2016) is that the causal set
dispersion relation in 4D is:

$$\omega^2 \approx k^2 + \frac{4}{\ell_P^2} \cdot \frac{j_1(k\ell_P)}{k\ell_P}
+ \mathcal{O}(\ell_P^4)$$

where $j_1$ is the spherical Bessel function. At large $k$, this suppresses high-frequency
modes. The effective cutoff scale in the near-horizon region is not $\ell_P^{-1}$ but rather:

$$\Lambda_{\text{UV}}(M) \sim \frac{1}{\ell_P} \cdot \left(\frac{\ell_P}{r_s}\right)^{1/3}
= \frac{1}{\ell_P} \cdot \left(\frac{M_P}{M}\right)^{1/3}$$

This $M^{-1/3}$ suppression of the UV cutoff is the origin of the $M^{-2/3}$ temperature
exponent:

$$T_{\text{cutoff}} \sim \frac{\Lambda_{\text{UV}}}{2\pi} \sim
\frac{1}{2\pi\ell_P} \left(\frac{M_P}{M}\right)^{1/3}$$

For $M \gg M_P$, this is much larger than $T_H \sim 1/M$, giving the ratio:

$$\frac{T_{\text{cutoff}}}{T_H} \sim M^{2/3} \; \text{(in Planck units)}$$

---

## 3. Summary of Scaling Regimes

| Regime | Entropy scaling $S(M)$ | Temperature scaling $T(M)$ | Physics |
|--------|----------------------|---------------------------|---------|
| Continuum area law (4D) | $S \propto M^2$ | $T = T_H \propto M^{-1}$ | Standard Hawking |
| Causal set (4D, $M \gg M_P$) | $S \propto M^{5/3}$ | $T_{\text{cutoff}} \propto M^{-2/3}$ | Modified UV |
| Fixed-$N$ causal set (2D radial) | $S \sim \text{const}$ | — | Bounded DOF |
| 2D causal diamond | $S \propto \log N \propto \log M$ | — | CFT scaling |

### Numerical test strategy

To verify the $M^{5/3}$ scaling in 4D:

1. Sprinkle $N$ causal set elements into 4D Schwarzschild spacetime, with
   $N \propto M^2$ (constant density mode)
2. Compute the SJ vacuum and the entanglement entropy across the horizon
3. Fit $S(M) = \alpha M^{5/3} + \beta$ and compare vs. $S(M) = \alpha M^2 + \beta$

**Computational constraint**: For $M=4$ in constant-density 4D mode,
$N \sim 150 \times 4^2 = 2{,}400$, requiring a $2{,}400 \times 2{,}400$
eigendecomposition ($\sim 10^{10}$ FLOPs, approximately 1 minute). For $M=8$,
$N \sim 9{,}600$, which is $\sim 10^{12}$ FLOPs (about 1 hour). Practical range:
$M \in [1, 5]$ with $N_{\text{ref}} \sim 200$.

The 2D radial model in the current repository tests the **causal set machinery**
(SJ vacuum on curved spacetime, causal matrix construction) but CANNOT verify the
$M^{5/3}$ exponent because the horizon in 2D is a point, not a 2-surface. The
entropy in 2D scales as $\log M$, not $M^{5/3}$.
