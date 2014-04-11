title: About

A **B**-factor **D**ata**B**ank (**BDB**) entry is a PDB entry with full
isotropic B-factors. Information on the BDB decision scheme will shortly
appear on this page.


### <a name="motivation"></a>Motivation
If protein engineers, homology modellers, biologists, or bioinformaticians need
B-values from a PDB file, they normally want full isotropic B-values. Normally
it is indeed the full B-factor that is stored in the B-factor field in the ATOM
records of a PDB file. However, the field contains different measures in some
files, such as residual B-factors in case TLS refinement has been used
(REFMAC), or mean square amplitude of atomic vibration instead of B-factor
(RESTRAIN). The BDB contains PDB files with full isotropic B-factors in the
B-factor field if the original PDB file contains enough information to
determine the content of the B-factor field and calculate the full B-factor
if necessary.

### <a name="decision"></a>Decision scheme
The decision scheme behind the creation of BDB entries uses information
directly obtained from PDB entries. (See [info](#info) on BDB entry pages
below).

#### Decisions
![diagram](/static/images/flowchart.svg)

#### <a name="info"></a>Extra info on the BDB entry pages
These pages will show whether full B-factors have been calculated from the PDB
file or if full B-factors were already present in the PDB file. The information
that was used to arrive at this conclusion is shown in the Refinement and PDB
Entry Format sections. The refinement section is subdivided in software,
TLS-related info, other B-factor info and other refinement remarks.

**B-factor type according to PDB remediation**: in 2011 several problems were
[remediated](http://www.wwpdb.org/remediation.html) by the PDB. The
remediations included fixing TLS group definitions and determining whether the
B-factor type in the PDB file is likely to be residual or not. If the B-factor
type could not be verified according to the remediation a BDB file has not been
created.

**Number of TLS groups and B-factor type according to refinement remarks**:
these table rows show the information on the number of TLS groups or the type
of B-factor that could be extracted from REMARK 3 records.

**B-factor group type**: indicates if the protein and/or nucleic acid chain(s)
have been refined using a single overall B-factor, one or two B-factors per
residue, or individual B-factors.

**C&alpha; only**: indicates if the protein chain only consists of a C&alpha;
trace.

**Reproducible fraction of B-factors**: the fraction of B<sub>eq</sub> values
in the B-factor field of the ATOM records that could be reproduced using the
anisotropic temperature factors in the ANISOU records.

**Anisotropic temperature factors specified in correct order**: indicates if
B<sub>eq</sub> values could be calculated using the first three elements of
the anisotropic temperature factors in the ANISOU records (U<sub>11</sub>,
U<sub>22</sub>, and U<sub>33</sub>) or if a non-standard U<sub>ij</sub>
combination was necessary for the calculation.

**Other refinement remarks**: the "OTHER REFINEMENT REMARKS" section of REMARK
3.

**PDB entry format**: date and version of the PDB format used for the PDB
file.

### Created by
Wouter Touw &
[Gert Vriend](http://swift.cmbi.ru.nl/gv)
