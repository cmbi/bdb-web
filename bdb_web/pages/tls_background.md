title: TLS background

Displacement of groups of atoms can be modeled by the TLS formalism presented
in detail by Schomaker and Trueblood (1968). The TLS formalism describes a
rigid-body displacement with three tensors T, L, and S for Translation,
Libration, Screw. Useful qualitative and quantitative explanations of the TLS
formalism summaries are presented by Winn, Isupov and Murshudov (2001),
Painter and Merritt (2005, 2006). All of the papers above are references for
this page.

T and L are symmetric 3x3 tensors with units in &#8491;^2^ and radians^2^,
respectively. The
translation tensor T describes the anisotropic translational displacement for
the atoms in the rigid body and is analogous to the individual anisotropic
mean-square displacement tensor [U][1]. The rotation of the rigid body is
described by the libration tensor L. The screw tensor S describes the
correlation between the rotation and translation of a rigid body undergoing
rotation about three non-intersecting orthogonal axes.

Here, we consider the total [ADP][1] to have 3 contributions:
U = U~crystal~ + U~TLS~ + U~atom,residual~

The overall anisotropy U~crystal~ is generally modeled using a single
anisotropic scale factor. The isotropic component of the overall scale factor
is usually included in the B-factors, but in [some][2] PDB files this is not
the case. U~TLS~ can be related to the T, L, and S tensors, their origin,
and an atom in the TLS group located at x, y, z as:

U~TLS~^11^ = L^22^z^2^+ L^33^y^2^- 2L^23^yz+ 2S^21^z- 2S^31^y+ T^11^

U~TLS~^22^ = L^11^z^2^+ L^33^x^2^- 2L^31^xz- 2S^12^z+ 2S^32^x+ T^22^

U~TLS~^33^ = L^11^y^2^+ L^22^x^2^- 2L^12^xy- 2S^23^x+ 2S^13^y+ T^33^

U~TLS~^12^ = -L^33^xy+ L^23^yxz- L^13^yz- L^12^z^2^- S^11^z+ S^22^z+ S^31^x- S^32^y+ T^12^

U~TLS~^13^ = -L^22^xz+ L^23^yx- L^13^y^2^+ L^12^yz+ S^11^y- S^33^y+ S^23^z- S^21^x+ T^13^

U~TLS~^23^ = -L^11^yz- L^23^x^2^+ L^13^xy+ L^12^xz- S^22^x+ S^33^x+ S^12^y- S^13^z+ T^23^

A TLS model can be interpreted as a sum of 6 independent displacements:
3 screw librations about non-intersecting axes and 3 translations. The program
[TLSView][3] (Painter and Merrit, 2005) is very useful for visualizing the TLS
motion.

Modeling U~atom,residual~ is described [here][1]. The B-factor in PDB files is
usually the sum of the isotropic components of U~crystal~, U~TLS~, and
U~atom,residual~.


### Additional analyses: PDB versus BDB
Several analyses of the (differences between) PDB and BDB files are described
in the [BDB paper][4].

In the article we show that the global B-factor maximum smoothed in a
5-residue window in a PDB chain is often tens of residues away from the
maximum in the corresponding BDB chain.

This figure shows correlation of the C&alpha;-C&alpha; distance between the
maxima with the distance in primary structure.

![][5]


### References and Further Reading

* Painter, J. and Merritt, E.A. (2005) Acta Crystallogr. D, 61, 465-471.
* Painter, J. and Merritt, E.A. (2006) Acta Crystallogr. D, 62, 439-450.
* Schomaker, V. and Trueblood, K.N. (1968) Acta Crystallogr. B, 24, 63-76.
* Winn, M.D., Isupov, M.N. and Murshudov, G.N. (2001) Acta Crystallogr. D, 57, 122-133.
* Zucker, F., Champ, P. and Merritt, E.A. (2010) Acta Crystallogr. D, 66, 889-900.

[1]: {{ url_for("pages", name="theory") }} "U"
[2]: http://phenix-online.org/pipermail/phenixbb/2012-August/018927.html
"overall anisotropic scale"
[3]: http://pymmlib.sourceforge.net/doc/tlsview/tlsview.html "TLSView"
[4]: {{ url_for("pages", name="about") }} "About BDB"
[5]: {{ url_for("static", filename="background/penta_caca_seq_dist.png") }}
"maxima"
