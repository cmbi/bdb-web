title: About

A **B**-factor **D**ata**B**ank (**BDB**) entry is a PDB entry with full
isotropic B-factors.

[What is a B-factor?][1]


### <a name="motivation"></a>Motivation
Protein engineers, homology modellers, biologists, crystallographers and
bioinformaticians frequently analyze B-factors in PDB structures because
B-factors are a measure of mobility. Normally full B-factors are stored in
the [B-factor field in the ATOM records][1] of a PDB file. However, in about
10% of the X-ray PDB files the B-factor field represents different quantities.
For example, ["residual" B-factors][2] without the
[isotropic TLS contribution][3] can be present, atomic
[mean-square displacements][1] instead of B-factors have been deposited,
or sometimes the [anisotropic overall scale][3] has not been included in the
B-factors. In general, this leads to lower B-factors than the B-factors
reported for the majority of the PDB files. Furthermore, the location of
apparent (normalized) B-factor maxima in a chain might be different
and might even shift to a different secondary structure element of a different
secondary structure type when full (estimates of) isotropic B-factors instead
of residual B-factors are considered.
Therefore, the different representations of disorder may influence both large
and small scale analyses of B-factors. The BDB aims to present a more
consistent B-factor representation.
The BDB contains PDB files with full isotropic B-factors in the
B-factor field if the original PDB file contains enough information to
determine the content of the B-factor field and calculate the full B-factor
if necessary.

#### <a name="reference"></a>Citation
If you use BDB entries, please cite:

Wouter G. Touw & Gert Vriend,
*"BDB: Databank of PDB files with consistent B-factors"* (2014)
Protein Engineering, Design and Selection (PEDS) 27 (11): 457-462.
[doi: 10.1093/protein/gzu044][11]

</br>

### <a name="download"></a>Download BDB entries
You can go to the download page of a single BDB entry by entering a PDB code in
the search box. The entire databank can be downloaded via `rsync`:

`rsync -avz rsync://rsync.cmbi.umcn.nl/bdb/??/????/????.bdb my-bdb/`

A list of all BDB entries is available [here][4].

</br>

### <a name="source"></a>Source code
The source code for generating BDB files from PDB files is available on
[GitHub][5].

</br>

### <a name="info"></a>Explanation of BDB entry pages
These pages will show whether full B-factors have been calculated from the PDB
file or if full B-factors were already present in the PDB file. The information
that was used to arrive at this conclusion is shown in the Refinement and PDB
Entry Format sections. The refinement section is subdivided in software,
TLS-related info, other B-factor info and other refinement remarks.

**B-factor type according to PDB remediation**: in 2011 several problems were
[remediated][6] by the PDB. The
remediations included fixing TLS group definitions and determining whether the
B-factor type in the PDB file is likely to be residual or not. If the B-factor
type could not be verified according to the remediation a BDB file has not been
created.

**Number of TLS groups and B-factor type according to refinement remarks**:
these table rows show the information on the number of TLS groups or the type
of B-factor that could be extracted from REMARK 3 records.

**SKTTLS validation summary**: results of TLS model tests after a [TLSANL][7]
run. Extreme residuals may indicate ADP problems. A detailed explanation is
given in the [SKTTLS][8] report description and in [this][9] paper about
validation of TLS models by Zucker, Champ & Merritt (2010).

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
[Gert Vriend][10]


[1]: {{ url_for("pages", name="theory") }}  "Theory"
[2]: http://dx.doi.org/10.1107/S0907444900014736 "Winn, Isupov & Murshudov"
[3]: {{ url_for("pages", name="tls_background") }} "TLS background"
[4]: http://www.cmbi.umcn.nl/WHY_NOT2/resources/list/BDB_PRESENT "List of all BDB entries"
[5]: https://github.com/cmbi/bdb "bdb"
[6]: http://www.wwpdb.org/remediation.html "PDB remediation"
[7]: http://legacy.ccp4.ac.uk/html/tlsanl.html "TLSANL"
[8]: http://legacy.ccp4.ac.uk/html/tlsanl.html#skttls "SKTTLS"
[9]: http://dx.doi.org/10.1107/S0907444910020421 "Zucker, Champ & Merritt"
[10]: http://swift.cmbi.umcn.nl/gv "Gert Vriend"
[11]: http://dx.doi.org/10.1093/protein/gzu044 "BDB article"
