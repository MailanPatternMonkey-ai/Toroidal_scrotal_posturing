# Rectangular toroidal extension and OMNIBUS ledger review

18 October 2026 · Review accompanying Geometry Master consolidation 2.3

The supplied files support two additions: an analytical extension of the ideal toroidal sector-memory result to rectangular lattices and fixed positive couplings, and a concrete ledger structure for distinguishing a local correction from repair of its downstream uses. Both supplied check reports reproduced exactly. The archive supplies detailed records and version relationships; its screening and coding labels retain their original scope.

## Rectangular toroidal extension

**Disposition: reviewed analytical extension, recorded separately from the published cubic reference theorem.** The proposal's argument remains valid under the hypotheses below. The numerical cases illustrate the asymptotic correction; they are not the proof of its universal claim.

Fix integer side lengths Lₓ,Lᵧ,L_z≥2, finite J>0, 0<t<1, and an integer sampling spacing d≥1. Keep the source-free, unbounded-current cosine model, fixed-reference Z000 ensemble, distinct labelled periodic cells, fixed positive reference cycles, and complete proposal rule from [Toroidal Dynamics v0.1](https://github.com/aureoncorner-dotcom/Toroidal_scrotal_posturing/blob/bbf8bb615002c76a833b2317998d5cd2a462e935/TOROIDAL_DYNAMICS.md). Set B=8LₓLᵧL_z+7. The stationary observation Yₙ=q(X_dn) has no finite Markov order. No initial full-state law produces an exactly time-homogeneous finite-order sector law under this same clock.

This extension is relative to that ideal mathematical kernel. It does not change the named J=1, t=1/2 execution profile, establish a finite-current result, or supply an estimate of mixing time or typical prediction error.

### Why the proof extends

The kernel specification already allows rectangular cellulations. Its positive target is normalizable, its descriptor probabilities are symmetric, and the membrane/current reachability argument uses torus homology rather than equal side lengths. The normalization bound is 8(1+t)^P exp(JE), with P plaquettes and E edges; the Bessel generating function supplies the summation identity. [NIST DLMF 10.35.1](https://dlmf.nist.gov/10.35.E1).

Let R=Kᵈ, u=1_{q=000}, D multiply by u, and A=DRD on L²(π). Finite stationary Markov order would make the all-zero block continuation probability eventually constant, say c. Self-adjointness then gives

\[
\|A^m(A-cI)u\|^2
=s_{2m+2}-2cs_{2m+1}+c^2s_{2m}=0.
\]

For m≥1, ker Aᵐ=ker A by the spectral representation of a bounded self-adjoint operator. Therefore A²u=cAu. Positive mass at every valid state makes this identity pointwise; Au>0 on the zero sector because d identity proposals have positive probability. Notice that A=D Kᵈ D allows excursions between sampled endpoints and generally differs from (D K D)ᵈ.

Use the valid states x_N with current 2N on every stored positive edge and M=q=0. Over 2d microticks, each edge differs from 2N by at most 4d. For fixed J, the positive Bessel series gives

\[
I_n(J)=\frac{(J/2)^n}{n!}S_n(J),\qquad
1\le S_n(J)\le\exp\!\left(\frac{J^2}{4(n+1)}\right).
\]

The series is [NIST DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2); the displayed bound follows by replacing n!/(n+k)! with (n+1)⁻ᵏ in its positive terms. Consequently I_{n+1}(J)/I_n(J)=J/[2(n+1)]·(1+O(1/n)), uniformly over the finite reachable offset range. A positive unit cycle along axis a has acceptance ε_{a,N}(1+O(1/N)), where ε_{a,N}=(J/(4N))^{L_a}; its negative-direction counterpart is accepted with probability one for sufficiently large N. Unit cycles do not alter M. All other proposal families preserve q.

The comparison walk on (ℤ/2)³ thus flips axis a with probability (1+ε_a)/(2B), up to a uniform error O(ε_a/N). Its exact d-step return polynomial is

\[
r_d(\varepsilon)=\frac18\sum_{S\subseteq\{x,y,z\}}
\left(1-\frac{|S|+\sum_{a\in S}\varepsilon_a}{B}\right)^d.
\]

Each partial derivative at zero is strictly negative:

\[
g_a=-\frac d{8B}\sum_{S\ni a}\left(1-\frac{|S|}{B}\right)^{d-1}<0.
\]

Put m=min L_a and η_N=(J/(4N))ᵐ. The shortest axes contribute ε_{a,N}=η_N, while longer axes contribute o(η_N). Telescoping the conditional-law errors over the fixed 2d horizon gives o(η_N). Translation invariance of the comparison walk then yields

\[
\frac{A^2u(x_N)}{Au(x_N)}
=r_d(0)+\eta_N\sum_{a:L_a=m}g_a+o(\eta_N).
\]

The negative leading coefficient contradicts constancy of A²u/Au: its limit would force c=r_d(0), and subtracting that limit and dividing by η_N would force the coefficient to vanish. This proves the stationary claim. Countable-state irreducibility, aperiodicity and positive recurrence give convergence to π; passing a hypothetical fixed finite-history transition rule through the convergent block probabilities gives the prohibited stationary rule, proving the initial-law clause.

All parameters and d are fixed before N→∞. There is no uniform claim for growing lattice size, growing d, J approaching an endpoint, t=0, accepted-move clocks or adaptive sampling. The proof does not exclude arbitrary augmented statistics or finite-dimensional hidden-state representations.

### Checks reproduced in this review

The two inspected local generators were copied into a fresh output folder before execution. Neither original JSON file was overwritten. Parsed outputs match both supplied JSON reports exactly.

| Check | Cases | Result |
|---|---:|---|
| Exact eight-state convolution, character formula, and all three transition derivatives | 6: three shapes at d=1 and d=B | Exact rational comparisons pass; every derivative is negative |
| Local full-kernel two-step ratio at d=1 | 9: three parameter sets at N=10,100,1000 | Supplied 70-digit Decimal results reproduced |

| Shape | J | t | Predicted scaled limit | Relative discrepancy at N=1000 |
|---|---:|---:|---:|---:|
| (2,3,4) | 0.5 | 0.2 | −1/398 | 0.086935% |
| (2,2,3) | 2 | 0.8 | −1/103 | 0.074017% |
| (3,4,5) | 3.25 | 0.01 | −1/974 | 0.068582% |

The local calculation enumerates sector-preserving current-changing descriptors. Identity, cube, sheet and rejected contributions have unchanged sector-hold function and are accounted for algebraically. This checks a local ratio at d=1; it performs no stationary averaging, long sampler replay, interval certification or physical measurement.

## OMNIBUS and GQG archive

The preserved ZIP is 170,996,875 bytes with SHA-256 `aa684f88595a0a1b08bf583c25322ed2bc02d16d28be654fe43262e97dc6be42`.

| Inventory measure | Verified count |
|---|---:|
| Archive entries | 1,239 |
| Distinct byte contents, including the empty content | 640 |
| Repeated-content entries beyond the first copy | 599 |
| Distinct member names | 690 |
| Names used for more than one distinct content | 54 |
| Identical copies of the main OMNIBUS/GQG ledger | 11 |

Every member was read by its ZIP entry identity, CRC-checked, hashed, and preserved under a safe local identifier. Repeated names were not allowed to overwrite earlier versions. One empty-content group covers eight entries under two binary-document names; those entries provide no document body. File identity and container integrity do not authenticate the underlying events.

The archive's **OMNIBUS v7.79-r1 — Constitutional Foundation and Supported Repair** is byte-identical to the pinned Toroidal repository copy. It is a duplicate source, not another independent derivation. Its §10 remains explicitly labeled SUPPORTED RECONSTRUCTION. Its normative commitments, formal quotient models and empirical coding rules retain distinct roles.

### What the ledger establishes within this package

The main ledger contains **3,088 uniquely keyed episodes across 24 cases and 120 columns**. The compact episode table has the same keys. The full episode table contains **13,309 member rows** and the same 3,088 episode keys. The case/node coordinates are unique in that full table.

Source hashes agree between all 3,088 master and compact rows. After the declared removal of node-number zero padding and line-start node labels, their source/response/correction/repair node lists and source, response and correction text agree throughout. Repair text agrees for 3,087 episodes. The remaining episode, `seventh_share:E0337`, uses two representations of node n2603: the master says “This code was redacted.” and the compact table says `[n2603 REDACTED]`. The full table expressly marks the node REDACTED and carries the placeholder. Neither representation recovers its hidden text.

These are joins between derived records in one package. They establish internal correspondence, not independent authentication of an original transcript or physical speaker.

The main ledger labels **2,660 rows SCREEN_ONLY_CANDIDATE_NOT_ADJUDICATED**. A total of **3,067 rows carry a screen_only_not_prevalence_denominator tag**, sometimes alongside other tags. These are different fields and counts; neither makes 3,088 a count of confirmed failures or a valid common prevalence denominator.

The **113-row proposition-lineage table** labels 88 rows NO_REPAIR, 15 VERDICT_REPAIR, 8 LOCAL_REPAIR and 2 SURFACE_RETRACTION. Both `descendants_located` and `descendants_repaired` are UNKNOWN for all 113 rows. These are inherited coding labels, not newly adjudicated outcomes. A local or verdict repair therefore cannot be reported as complete downstream repair from these records.

The **55-row deletion table** contains the **20-row agency deletion table as an exact subset**. They total 55 distinct adjudications, not 75. All 55 point to located canonical episodes. For all 44 applicable rows, the declared deleted spans occur both in the coded response and in the packaged episode text; the other 11 are labeled NOT_APPLICABLE.

### How this improves the geometry framework

The archive makes a useful distinction operational: **text deletion is an empirical intervention on a retained answer; residual descent is a universal condition on a declared state map.** The deletion table's `descent_test_all_compatible_occupants` field contains 29 YES, 14 UNKNOWN, one NO and 11 NOT_APPLICABLE labels. Those source judgments alone do not define a state space, update, observation map or exhaustive coverage and cannot establish the mathematical residual-descent theorem.

For a new application, retain the exact source proposition and node/hash references, the response, any deleted span or other intervention, the remaining answer, a counter-witness, the applicable criterion and domain, coverage, correction nodes, and downstream uses. Identify whether the test is a textual intervention, deterministic factor test, or stochastic next-observation-law test. Preserve a local correction while tracking each dependent conclusion or action separately.

The practical next step is targeted: locate descendants of the 113 proposition-lineage records and check whether the original proposition and its correction were propagated. Preserve UNKNOWN where the needed downstream record is absent. The archive's screening rows would require their own eligibility and independent adjudication work before supporting a rate.

## Review coverage and source preservation

All four supplied inputs were copied and hashed before analysis. All 1,239 archive entries were CRC-checked and hashed; all 130 distinct CSV contents were structurally parsed for columns and counts. Detailed checks focused on the main ledger, compact and full episode tables, proposition lineage and two deletion tables. Relevant mathematical, status and provenance sections of v7.79-r1 were compared with the pinned source. The remaining essays, binary documents and individual historical codings were not exhaustively re-read or re-adjudicated.

No program from the ZIP was executed. The fresh arithmetic execution used the two inspected local generators accompanying the supplied JSON reports. The original four files and the prior master are preserved. This review updates the local portable master; online Docs and remote repositories were not changed.

The [machine-readable receipt](C:/Users/drewd/Documents/Codex/2026-09-08/che/outputs/GEOMETRY_OMNIBUS_REVIEW_2026-10-18.json) records hashes, counts, checks and output identity. The [original rectangular proposal](C:/Users/drewd/Documents/Codex/2026-09-08/che/work/intake_oct18_omnibus/sources/O03.md) retains its original draft wording. The [member index](C:/Users/drewd/Documents/Codex/2026-09-08/che/work/intake_oct18_omnibus/content_index.tsv) maps every distinct content to its source names; the full manifest retains all entry occurrences.
