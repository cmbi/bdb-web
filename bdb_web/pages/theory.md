title: What is a B-factor?

The following is heavily based on [Trueblood et al., 1996][1]
and references therein.

---

Displacement of atoms from their mean position in a crystal structure
diminishes the scattered X-ray intensity. The displacement may be the result of
temperature-dependent atomic vibrations or static disorder in a crystal
lattice. If the atomic displacements are assumed to be harmonic and
anisotropic, the attenuation of atomic scattering factors can be represented
by the atomic anisotropic Gaussian Debye-Waller factor

$T(\textbf{h}) = \exp{[-8\pi^2 \langle u_\textbf{h}^2 \rangle \frac{\sin^2 \theta}{\lambda^2}]}$. (1)

(equation 1.4.12 from [Trueblood et al., 1996][1]).
Here $u_\textbf{h}$ is the projection of the atomic displacement $\textbf{u}$
on the direction of diffraction vector $\textbf{h}$, $\theta$ is the scattering angle
and $\lambda$ is the X-ray wavelength. The average in the exponent denotes an
average over space and time. The mean-square displacements are termed
anisotropic displacement parameters (ADPs) as the average depends on the
direction of $\textbf{h}$. Referred to a Cartesian basis, an equivalent
representation of eq. (1) is

$T(\textbf{h}) = \exp{[-2\pi^2 \textbf{h}^\textbf{T}\textbf{Uh}]}$. (2)

The ADPs define the symmetric atomic mean-square displacement tensor

$\textbf{U} =
 \begin{pmatrix}
  U_{11} & U_{12} & U_{13} \\
  U_{12} & U_{22} & U_{23} \\
  U_{13} & U_{23} & U_{33}
 \end{pmatrix}$. (3)

An element $U_{ij}$ of $\textbf{U}$ has dimension (length)^2^. If the displacements are
(assumed to be) isotropic, the average in eq. (1) is constant and the
Debye-Waller factor only depends on the magnitude of $\textbf{h}$:

$T(|\textbf{h}|)=\exp{[-8\pi^2 \langle u^2 \rangle \frac{\sin^2 \theta}{\lambda^2}]}$. (4)

(equation 1.4.13 from [Trueblood et al., 1996][1]).
The B-factor is directly related to the mean square isotropic displacement of
the atom:

$B = 8\pi^2 \langle u^2 \rangle$. (5)

The (an)isotropic displacement parameters are variables during a typical
refinement and may therefore also contain contributions of apparent
displacements resulting from the use of an inadequate model or from overlooked
errors in the X-ray data. The "temperature factor" field in the ATOM records
of PDB files normally contains the isotropic B-factor or $B_{eq}$, the value that
represents isotropic displacement of atoms that were described by anisotropic
ADPs during refinement. The term "displacement parameter" is preferred over
"temperature factor" because the atomic displacements are not only a
consequence of thermal vibration but also of different atomic positions in
different unit cells. The equivalent B-factor can be derived from the
equivalent isotropic displacement parameter $U_{eq}$:

$B_{eq} = 8\pi^2 U_{eq} = \frac{8}{3} \pi^2 (U_{11} + U_{22} + U_{33})$. (6)

$U_{eq}$ is equivalent to the sum of the eigenvalues of $\textbf{U}$ and
represents the mean-square displacement averaged over all directions.
The ANISOU records or PDB entries normally contain the six independent elements
of the symmetric tensor scaled by a factor 10^4^.

[1]: http://www.iucr.org/resources/commissions/crystallographic-nomenclature/adp
