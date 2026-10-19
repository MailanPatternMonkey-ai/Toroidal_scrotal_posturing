# Geometry Maximization archive recovery and verification

18 October 2026, America/New_York · Supports Geometry Master consolidation 2.4

The supplied collection restores two complete runnable releases: **Geometry Maximization v2.0** and **Toroidal Geometry v1.0**. Their inspected verification programs freshly passed **36 tests** and reproduced **11 examples containing 50 generated artifacts**, byte-for-byte on this Windows Python 3.12.14 runtime. The second release supplies the lattice, throat, configuration and example files absent from the previously reviewed repository root.

The [updated Geometry Master](C:/Users/drewd/Documents/Codex/2026-09-08/che/outputs/GEOMETRY_MASTER.md) now includes these results, the explicit approximation certificate, its numerical boundary limitation, the usable execution contracts and revised recovery status. The mathematical core matches earlier material under the declared presentation normalization below. The main addition is recovered, verified implementation access.

## What was recovered

| Release | Files, including its manifest | Fresh checks | Included examples |
|---|---:|---|---|
| [Geometry Maximization v2.0](C:/Users/drewd/Documents/Codex/2026-09-08/che/work/intake_oct18_maximization/geometry_v2_release/README.md) | 44 | 43 declared file hashes; 10 tests | Five exact-phase/numerical-comparison configurations |
| [Toroidal Geometry v1.0](C:/Users/drewd/Documents/Codex/2026-09-08/che/work/intake_oct18_maximization/toroidal_v1_release/README.md) | 88 | 87 declared file hashes; 26 tests | Three exact lattice fixtures and three curved-throat fixtures |

All 132 extracted files, including the two manifest files, had identical hashes before and after execution. The tests ran without third-party dependencies. The optional plot generator and offline browser explorer were not run; the historical browser QA receipt remains historical.

The Toroidal package preserves exactly the same Geometry v2.0 ZIP in its baseline. Two selected copies of that Geometry ZIP in the outer collection are identical. These copies establish lineage and availability; they are not independent corroborating experiments.

## Fresh phase results

| Configuration | Departures | Exact slips | Ideal-certified rows | Floating bin mismatches | Mismatches on ideal-certified rows |
|---|---:|---:|---:|---:|---:|
| `default_507` | 507 | 53 | 502 | 0 | 0 |
| `warped_39` | 39 | 5 | 1 | 3 | 0 |
| `exact_10000` | 10,000 | 1,034 | 10,000 | 0 | 0 |
| `boundary` | 39 | 4 | 38 | 0 | 0 |
| `bin_boundary` | 64 | 7 | 64 | 1 | 1 |

All four artifacts for each configuration—`run.json`, `summary.json`, `trace.csv` and the run checksum list—reproduced byte-for-byte. Tests include an independent integer-square-root oracle for all 10,000 departures, exact half-open endpoints, threshold perturbations of 10⁻⁴⁰, reduced recurrences, invalid-input rejection and overwrite refusal.

The three mismatches in the stronger-warp fixture and the single bin-boundary mismatch are documented, retained behavior. Release PASS does not mean all numerical labels agree. The phase labels use exact arithmetic in ℚ(√5); displayed coordinates and the iterated approximation use floating point.

For the second-order approximation G and smooth coordinate h, the rational residual bound is

\[
\widehat E_\epsilon=\frac{|\epsilon|^3}{3}\left[1+(1+|\epsilon|)^2\right],
\qquad
|h(G(x))-h(x)-\alpha|\le\widehat E_\epsilon.
\]

From identical initial data, the ideal phase error after n steps is at most nÊ. If the exact reference phase is distance d_n from the closest bin boundary, d_n>nÊ certifies the ideal bin; equality is insufficient. Identical initialization at n=0 and exact rotation at ε=0 are separate model-equality cases. This certificate does not enclose floating-point trigonometric or iteration errors. The boundary example demonstrates that distinction directly.

The added bound on the Haar measure of a conservative possible-error cover, min{1,39ÊN(N−1)}, follows by summing the 39 bin-boundary neighborhoods over N labels. It is a set-measure bound, not an observed numerical error rate.

Protocol v0.5 supplies a runnable deterministic phase lane. It accepts 1–100,000 departures, an exact starting phase in ℚ(√5)∩[0,1), and rational |ε|≤0.99. The mathematical diffeomorphism domain is the larger |ε|<1. Exact inputs reject floating JSON numbers; rational and decimal strings preserve the specified values.

## Fresh toroidal and throat results

The 26 tests comprise 17 lattice tests, seven throat tests and two reporting-rule tests. All three lattice examples reproduced seven artifacts each; all three throat examples reproduced three artifacts each. Thus the toroidal release reproduced 30 artifacts.

The lattice tests cover integer ∂²=0, independently accounted divergence, layer/cut conservation, mod-two Betti numbers (1,3,3,1), signed operator changes, sourced counterexamples, exact character identities, accessibility, work-stopping bias and the distinction between strong closure and a special stationary projection. The character coefficients are synthetic; this is not microscopic direct/dual partition-function validation.

Protocol v0.6 validates rectangular lattices with side lengths 2–16 and volume at most 512. It requires typed integer chains, canonical vertices and an even field-state charge modulus from 2 through 1000. It reports actual charge, membrane and parity defects, and leaves integer winding unavailable outside the integer divergence-free domain. It does not infer a missing membrane, solve arbitrary integer homology or assign a physical weight to a state. The example ledger contains 11 constructed operator events and 12 states; it has no random acceptance law.

For the circular throat, the recovered implementation uses the curved metric factor h=1−(r/A)cosϑ and corrected physical radial velocity −rU′/(2h). Baseline diagnostics were:

| Diagnostic | Fresh maximum residual | Declared tolerance |
|---|---:|---:|
| Cartesian divergence, corrected velocity | 1.09385×10⁻¹¹ | 1×10⁻⁷ |
| Material tangency | 7.58922×10⁻¹³ | 1×10⁻⁷ |
| Integrated side-flux balance | 2.53069×10⁻¹¹ | 7.06858×10⁻⁸ |

At the sampled points, the uncorrected straight-tube radial velocity instead gives maximum divergence about 2.28514×10⁻³. Flat and translated controls, constant material throughflow and spatial cocycle additivity also pass. The analytic formulas establish their stated kinematic identities; these finite differences and quadratures check the implementation. Numerical artifact comparison uses absolute tolerance 10⁻⁹ and relative tolerance 10⁻¹⁰, with exact structure. Every artifact was also byte-identical on this runtime.

The reporting tests validate declared decision rules, including the exact L_max=4ξ boundary. They do not fit data, establish the scientific completeness of the caller's gates or supply those gates' evidence.

## Lineage and preservation

The original [supplied ZIP](<C:/Users/drewd/OneDrive/Desktop/New folder/New folder (2)/New Stuff 9_2_26/GEOMETRY_MAXIMIZATION_v2.0.zip>) is **11,961,147,925 bytes** with **1,273 outer entries**. It includes a much larger collection of archives and videos. It is not the minimal Geometry v2.0 release.

| Object | SHA-256 |
|---|---|
| Original supplied collection | `02b176731ab825e9b8689a48ce8e7070f351a64245fdcf18a2a4f5c7db826333` |
| Intact Geometry Maximization v2.0 ZIP | `263681efe82513b062b75bdc23d9d16be2ed8bdee96adf01c562944d2960c3cb` |
| Intact Toroidal Geometry v1.0 ZIP | `623f07aaa0b1fd6cdf817966f09f42792e6c2baf05da55294c09e9ed88b14c8f` |
| Preserved Geometry v1.6 verification ZIP | `b4c71388b4211aa08643c49515a69965f6ce9f5aa7fdcc523744c38b788a701e` |

All 44 files of the intact phase release exactly match their corresponding outer-folder files. The outer folder contains two additional files: `DROP_IT.py` and cached Python bytecode. They were inventoried and copied as source material, but neither was executed. Verification ran only the inspected intact releases in their separate folders.

The earlier Docs snapshot of the phase core contains a tab header and `CC0- NO RIGHTS RESERVED` line, plus differing line endings and trailing whitespace. Removing only those specified differences gives the same core text. The original license-bearing snapshot remains preserved. This is a presentation-normalized match, not byte identity.

Among 35 same-name comparisons with files already present in the pinned Toroidal repository checkout, 23 match exactly and seven differ only by CRLF/LF line endings. The other five compare generic root files: two READMEs, two checksum lists and the Geometry verifier against the root's different verifier. The intact Toroidal verifier itself matches the pinned root exactly. The mixed root remains unsuitable as a combined release; use the complete recovered folders.

The phase verifier also CRC-checked the preserved 90-entry v1.6 archive and validated its six nested checksum registers. It did not execute the older algebraic verifiers. Historical proof/audit counts retain their earlier scope.

## Coverage and delivery

The original was read-only, hashed in full before and after review, and retained in place. All outer names and metadata were inventoried. Forty-nine selected outer members were read, CRC-checked and hashed; both complete nested releases were extracted and checked. Full reference/verifier/test code was inspected before execution. Other large outer archives, videos and binary-document contents were not exhaustively decompressed or reviewed. Source instructions were treated as document content.

The compact master kit contains the updated master, this review, both intact release ZIPs and the fresh receipts. The nested duplication is intentional so either release can be extracted directly. The original 12 GB collection remains separately preserved. Its unrelated material is not silently included in the verification claim.

This intake closes the recovered reference-package access gap. Full TD-COS-FH-001 replacement configuration enforcement, lossless recording, restart conformance and long replay remain outstanding. The historical −1,352 accepted-event discrepancy remains unresolved. Physical Q1/Q2/Q3, empirical TTSC and the prospective two-clock experiment remain unrun by this intake. No Docs, Drive files or remote repositories were edited.

The [machine-readable receipt](C:/Users/drewd/Documents/Codex/2026-09-08/che/outputs/GEOMETRY_MAXIMIZATION_INTAKE_2026-10-18.json) records the original identity, extraction and lineage manifests, fresh results, preservation checks and output hashes. The pre-upgrade 2.3 master is retained in the review workspace.
