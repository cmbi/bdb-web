title: About

A **B**-factor **D**ata**B**ank (**BDB**) entry is a PDB entry with full
isotropic B-factors.

[What is a B-factor?][1]


### <a name="motivation"></a>Motivation
If protein engineers, homology modellers, biologists, or bioinformaticians need
B-factors from a PDB file, they normally want full isotropic B-factors.
Normally it is indeed the full B-factor that is stored in the B-factor field
in the ATOM records of a PDB file. However, sometimes the field contains
"residual" B-factors or atomic mean-square displacements instead of B-factors.
The BDB contains PDB files with full isotropic B-factors in the
B-factor field if the original PDB file contains enough information to
determine the content of the B-factor field and calculate the full B-factor
if necessary.

#### <a name="reference"></a>Citation
If you use BDB entries, please cite:

Wouter G. Touw & Gert Vriend,
*"BDB - a databank of PDB files with full isotropic B-factors."* (2014)
**Submitted**

</br>

### <a name="download"></a>Download BDB entries
You can go to the download page of a single BDB entry by entering a PDB code in
the search box. The entire databank can be downloaded via `rsync`:

`rsync -avz rsync://rsync.cmbi.ru.nl/bdb/??/????/????.bdb my-bdb/`

A list of all BDB entries is available [here][2].

</br>

### <a name="info"></a>Explanation of BDB entry pages
These pages will show whether full B-factors have been calculated from the PDB
file or if full B-factors were already present in the PDB file. The information
that was used to arrive at this conclusion is shown in the Refinement and PDB
Entry Format sections. The refinement section is subdivided in software,
TLS-related info, other B-factor info and other refinement remarks.

**B-factor type according to PDB remediation**: in 2011 several problems were
[remediated][3] by the PDB. The
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

**P only**: indicates if the nucleic acid chain only consists of a phoshorus
trace.

**Reproducible fraction of B-factors**: the fraction of B~eq~ values
in the B-factor field of the ATOM records that could be reproduced using the
anisotropic temperature factors in the ANISOU records.

**Anisotropic temperature factors specified in correct order**: indicates if
B~eq~ values could be calculated using the first three elements of the
anisotropic temperature factors in the ANISOU records (U~11~, U~22~, and U~33~)
or if a non-standard U~ij~ combination was necessary for the calculation.

**Other refinement remarks**: the "OTHER REFINEMENT REMARKS" section of REMARK
3.

**PDB entry format**: date and version of the PDB format used for the PDB
file.


</br>


### Created by
Wouter Touw &
[Gert Vriend][4]


[1]: /theory "Theory"
[2]: http://www.cmbi.ru.nl/WHY_NOT2/resources/list/BDB_PRESENT "List of all BDB
entries"
[3]: http://www.wwpdb.org/remediation.html "PDB remediation"
[4]: http://swift.cmbi.ru.nl/gv
