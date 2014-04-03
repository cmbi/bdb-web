title: About

A BDB entry is a PDB entry with full isotropic B-factors. Information on the BDB decision scheme will shortly appear on this page.

### Motivation
If protein engineers, homology modellers, biologists, or bioinformaticians need
B-values from a PDB file, they normally want full isotropic B-values. Normally
it is indeed the full B-factor that is stored in the B-factor field in the ATOM
records of a PDB file. However, the field contains different measures in some
files, such as residual B-factors in case TLS refinement has been used
(REFMAC), or mean square amplitude of atomic vibration instead of B-factor
(RESTRAIN). The **B**-factor **D**ata **B**ank (**BDB**) contains PDB files
with full isotropic B-factors in the B-factor field if the software could
determine the content of the B-factor field in the original PDB entry.

### Decision scheme

#### Variables

#### Decisions

### Created by
Wouter Touw &
[Gert Vriend](http://swift.cmbi.ru.nl/gv)
