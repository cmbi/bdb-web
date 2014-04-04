title: About

A **B**-factor **D**ata**B**ank (**BDB**) entry is a PDB entry with full isotropic B-factors. Information on the BDB decision scheme will shortly appear on this page.

### Motivation
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

### Decision scheme
The decision scheme behind the creation of BDB entries uses information
directly obtained from PDB entries. The variables used for making decisions are
explained here and are also visible on the pages for individual BDB entries.

#### Variables
**A**:
**B**:
**C**:
**D**:
**E**:
**F**:
**G**:

#### Decisions
![diagram](/static/images/flowchart.svg)

#### Extra info on the BDB entry pages
**B-factor group type**: indicates if the protein and/or nucleic acid chain(s)
have been refined using a single overall B-factor, one or two B-factors per
residue, or individual B-factors.

**Correct Uij**: true if the B-factors in the ATOM records could only be
reproduced if a non-standard combination of U fields in the ANISOU records was
used.

### Created by
Wouter Touw &
[Gert Vriend](http://swift.cmbi.ru.nl/gv)
