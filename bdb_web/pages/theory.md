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
on the direction of diffraction vector $\textbf{h}$, $\theta$ is the scattering
angle and $\lambda$ is the X-ray wavelength. The average in the exponent
denotes an average over space and time. The mean-square displacements are
termed anisotropic displacement parameters (ADPs) as the average depends on the
direction of $\textbf{h}$. Referred to a Cartesian basis, an equivalent
representation of eq. (1) is

$T(\textbf{h}) = \exp{[-2\pi^2 \textbf{h}^\textbf{T}\textbf{Uh}]}$. (2)

The ADPs define the symmetric atomic mean-square displacement tensor

$\textbf{U} =
 \begin{pmatrix}
  U_{11} & U_{12} & U_{13} \\
  U_{12} & U_{22} & U_{23} \\
  U_{13} & U_{23} & U_{33}
 \end{pmatrix}$. (<a name="eq3"></a>3)

An element $U_{ij}$ of $\textbf{U}$ has dimension (length)^2^. If the
displacements are (assumed to be) isotropic, the average in eq. (1) is constant
and the Debye-Waller factor only depends on the magnitude of $\textbf{h}$:

$T(|\textbf{h}|)=\exp{[-8\pi^2 \langle u^2 \rangle \frac{\sin^2 \theta}{\lambda^2}]}$. (4)

(equation 1.4.13 from [Trueblood et al., 1996][1]).
The B-factor is directly related to the mean square isotropic displacement of
the atom:

$B = 8\pi^2 \langle u^2 \rangle$. (5)

A macromolecular crystal structure is typically represented by three
coordinates (X,Y,Z), an [occupancy][13] parameter, and a "temperature factor"
in the [coordinate section][10] of PDB files ([Figure 1][3]). These parameters
are estimated during a computational process crystallographers refer to as
*refinement*. The goal of refinement is to improve the agreement between the
modeled structure and the reflections measured in the diffraction experiment.
The (an)isotropic displacement parameters are variables during a typical
refinement and may therefore also contain contributions of apparent
displacements resulting from the use of an inadequate model or from overlooked
errors in the X-ray data. The "temperature factor" field in the [ATOM
records][2] of PDB files normally contains the isotropic B-factor (
[Figure 1][3]) or $B_{eq}$, the value that represents isotropic displacement of
atoms that were described by anisotropic ADPs during refinement.


```
ATOM      1  N   THR A   1      17.047  14.099   3.625  1.00 13.79           N  
ATOM      2  CA  THR A   1      16.967  12.784   4.338  1.00 10.80           C  
ATOM      3  C   THR A   1      15.685  12.755   5.133  1.00  9.19           C  
ATOM      4  O   THR A   1      15.268  13.825   5.594  1.00  9.85           O  
ATOM      5  CB  THR A   1      18.170  12.703   5.337  1.00 13.02           C  
ATOM      6  OG1 THR A   1      19.334  12.829   4.463  1.00 15.06           O  
ATOM      7  CG2 THR A   1      18.150  11.546   6.304  1.00 14.23           C  
```

**<a name="fig1"></a>Figure 1** Thr 1 from [1crn][4]. After the atom's
identifiers the XYZ coordinates, occupancy, and B-factor are listed in these
[ATOM records][2].
</br>
</br>

The term "displacement parameter" is
preferred over "temperature factor" because the atomic displacements are not
only a consequence of thermal vibration but also of different atomic positions
in different unit cells. The equivalent B-factor can be derived from the
equivalent isotropic displacement parameter $U_{eq}$:

$B_{eq} = 8\pi^2 U_{eq} = \frac{8}{3} \pi^2 (U_{11} + U_{22} + U_{33})$. (<a
name="eq6"></a>6)

$U_{eq}$ is equivalent to the sum of the eigenvalues of $\textbf{U}$ and
represents the mean-square displacement averaged over all directions.
The [ANISOU records of PDB entries][5] normally contain the six independent
elements of the [symmetric tensor][9] scaled by a factor 10^4^ ([Figure 2][6]).


```
ATOM   3293  N   GLY B 635      15.522  -6.753  35.480  1.00 67.46           N  
ANISOU 3293  N   GLY B 635     7637  10155   7840    125    844     10       N  
ATOM   3294  CA  GLY B 635      16.002  -5.527  34.860  1.00 66.06           C  
ANISOU 3294  CA  GLY B 635     7519   9866   7715     35    723   -268       C  
ATOM   3295  C   GLY B 635      14.981  -4.446  34.608  1.00 69.48           C  
ANISOU 3295  C   GLY B 635     7997  10158   8244     -4    724   -496       C  
ATOM   3296  O   GLY B 635      15.107  -3.358  35.185  1.00 71.22           O  
ANISOU 3296  O   GLY B 635     8207  10502   8350    -17    684   -734       O  
```

**<a name="fig2"></a>Figure 2** Gly 635 from [3zzw][7]. U~11~, U~12~, U~13~,
U~12~, U~13~, and U~23~ are stored in the [ANISOU records][5] after the
identifier columns. The last numeric column of the [ATOM records][2] is
the equivalent B-factor, B~eq~, calculated from the six U~ij~ elements ([eq. 3]
[9]) in the ANISOU records ([eq. 6][8]).
</br>
</br>

###<a name="occ"></a>Occupancy
B-factors in PDB files commonly are seen as a measure of (local) mobility in
the (macro)molecule. As mentioned above, this is only partly true.

When 3D structures are solved by crystallography, then, as the name suggests,
crystals are needed. And in crystals by necessity crystal artefacts are
observed. The three most important artefacts are
1) crystal packing artefacts at those locations where the (macro)molecules
interact with other (macro)molecules in the crystal;
2) parts of the crystal have a different conformation of the molecule (static
disorder);
3) alternate locations when parts of the macromolecule are happy in multiple
conformations (dynamic disorder).
Crystal packing artefacts are a whole story in themselves
and are not of relevance for the BDB. You find information about these
artefacts in other PDB-facilities.
Alternate locations are most often seen for amino acid side chains when these
can have multiple rotamers that are energetically similarly favourable.
If this is observed in the crystal, then you will find side multiple chain
atoms with alternate location indicators A, B, etc. The occupancies normally
add up to unity ([Figure 3][11]). If no alternates have been observed, the
occupancy simply equals 1.00 (e.g. [Figure 1][3], [Figure 2][6])


```
ATOM    435  N   SER A  69      78.391  18.901  31.786  1.00  8.05           N  
ATOM    436  CA ASER A  69      77.622  17.702  31.446  0.70  8.36           C  
ATOM    437  CA BSER A  69      77.646  17.698  31.413  0.30  8.16           C  
ATOM    438  C   SER A  69      76.425  18.043  30.558  1.00  8.31           C  
ATOM    439  O   SER A  69      76.220  17.431  29.497  1.00  8.35           O  
ATOM    440  CB ASER A  69      77.152  17.000  32.717  0.70  9.01           C  
ATOM    441  CB BSER A  69      77.274  16.853  32.636  0.30  8.36           C  
ATOM    442  OG ASER A  69      76.383  15.862  32.393  0.70 10.15           O  
ATOM    443  OG BSER A  69      76.364  17.530  33.477  0.30  8.59           O  
```

**<a name="fig3"></a>Figure 3** Ser 69 from [4jf1][12]. Two alternate locations
have been observed for this side-chain (A and B) with occupancies 0.7 and 0.3.
</br>
</br>

It is often impossible to accurately model occupancy and ADPs separately
because they are highly correlated. Only at high resolution it may be possible
to resolve close alternate positions instead of modeling the atoms with large
B-factors.


[1]: http://www.iucr.org/resources/commissions/crystallographic-nomenclature/adp
[2]: http://www.wwpdb.org/documentation/format33/sect9.html#ATOM "ATOM records"
[3]: #fig1 "Figure 1"
[4]: http://www.rcsb.org/pdb/explore/explore.do?structureId=1crn "1crn"
[5]: http://www.wwpdb.org/documentation/format33/sect9.html#ANISOU "ANISOU
records"
[6]: #fig2 "Figure 2"
[7]: http://www.rcsb.org/pdb/explore/explore.do?structureId=3zzw "3zzw"
[8]: #eq6 "Equation 6"
[9]: #eq3 "Equation 3"
[10]: http://www.wwpdb.org/documentation/format33/sect9.html "coordinate
section"
[11]: #fig3 "Figure 3"
[12]: http://www.rcsb.org/pdb/explore/explore.do?structureId=4jf1 "4jf1"
[13]: #occ "Occupancy"
