# Geometry continuity intake and mathematical corrections

18 October 2026 · Supports Geometry Master consolidation 2.5

The four supplied files strengthen the record of **completed mathematics and working software**. The continuity report supplies an elementary Villain non-descent proof covering every parity sector and a sufficient refinement of its acceptance witness. Its relay implementation is recoverable and freshly passes all 20 declared tests. `_Math2.txt` contains useful circle-dynamics connections, but also material formula and theorem-scope errors; only corrected, relevant additions enter the master.

This revises the emphasis of the earlier assessment: there is already constructive repair and an executed transition artifact, alongside the exact phase model and the separate all-orders cosine theorem. Open physical experiments and production-sampler work do not make those completed results unresolved.

## 1. Supplied sources and coverage

| ID | Source | Review and use |
|---|---|---|
| C01 | Consolidated_Findings_and_Continuity_Record_v1.0.docx | All 222 body/table paragraphs read in document order; completed-result and version distinctions checked against recovered material and fresh calculations |
| C02 | _Math2.txt | All 2,212 lines read; selected formulas rederived and relevant literature checked; a conversational survey with internal revisions, not a uniformly validated paper |
| C03 | V3_ORBIT_GEOMETRY_INTEGRATION_NOTE_2026-09-02.md | Full text read; representation, routes, history, closure and remedy distinctions retained as an operational audit framework |
| C04 | 00_START_HERE.md | Full text read; useful corpus orientation and version map, not evidence that every indexed claim is proved |

Exact preserved copies and SHA-256 identities are in the [source manifest](../work/intake_oct18_continuity/source_manifest.json). C01, C03 and C04 match members of the previously inventoried large collection byte-for-byte; they were actually read in this intake. No same-name archive match was found for C02. A duplicate copy supplies lineage, not independent corroboration.

C01 contains eight tables, no embedded images/drawings or OMML equations, and no tracked edits, comments, footnotes or endnotes. Its body and table text were extracted from OOXML. The bundled renderer could not locate LibreOffice, so page layout was **not** visually reviewed. Paragraph identifiers P001–P222 refer to the [ordered extraction](../work/intake_oct18_continuity/continuity_record.txt), not rendered page numbers. No Word document was modified.

## 2. Completed elementary Villain result

C01 P040–P062 states the kernel and its constructive repair. Work on the untruncated, divergence-free, zero-source domain. Fix a reference cycle Γα of length L and let Aα be the signed current sum along it. For one attempted unit cycle, with orientations ± equally likely and Villain link weight exp(−I²/(2J)), the toggle probability is

\[
W_\alpha(A)=\frac12\left[\min\{1,e^{-(L+2A)/(2J)}\}+\min\{1,e^{-(L-2A)/(2J)}\}\right].
\]

The formula follows directly from the energy difference of adding ±1 on each of the L loop edges. At L=8, J=1:

| Same parity q=(0,0,0) | A | Toggle probability |
|---|---:|---:|
| Zero loop current | 0 | 0.018315638888734180… |
| Current 2 on each loop edge | 16 | 0.500000001030576811… |

These conditional probabilities differ by 0.481684362141842631…, about 48.17 percentage points. This is a counterexample to q-only strong lumpability for the **scheduled elementary attempt**, not a comparison between two randomly sampled outcomes.

For the general argument, adding 2mΓα preserves divergence and parity but sends A to A+2mL. For sufficiently large positive m,

\[
W_\alpha(A+2mL)=\tfrac12[1+e^{-(L+2A+4mL)/(2J)}],
\]

which strictly decreases as m increases for finite J>0. Thus every nonempty parity fiber contains different acceptance laws. All eight fibers have valid states: choose M=0 and I=ΣαqαΓα, satisfying the mod-two membrane constraint. This establishes non-descent in every sector of the declared domain.

**Constructive repair:** (q,|Aα|) determines the sign-averaged next-sector law; (q,Aα) determines the orientation-resolved acceptance ratios. This is a sufficient refinement for a specific witness. It does not prove a minimal statistic, availability at a fixed cost, or autonomous evolution of that statistic under every move of a complete sampler.

Fresh independent construction checked 24 pairs at L=8, J=1: eight sectors × three axes. Each pair satisfies exact integer divergence, the M=0 parity constraint and the cut-flux parity condition. Their probabilities differ at 90-digit working precision. The finite checks corroborate the written all-sector argument; they are not its proof.

The recovered `TOROIDAL_GEOMETRY_OMNIBUS_v1.1.md` contains the earlier q=000 argument in E.1. Its hash is **different** from the draft hash cited in C01 P213. It is a related source, not an authenticated recovery of that exact cited draft. The all-sector proof above was independently checked from its stated hypotheses. The later TD-COS-FH-001 theorem uses the **cosine/Bessel complete kernel** and has a stronger, different all-orders conclusion; neither kernel may silently stand in for the other.

## 3. Freshly reproduced relay artifact

The archived `Corner_Relay_Alpha_C6_Reference_v0.1.zip` was recovered intact. Its frozen packet hash agrees with the binding quoted by C01. Implementation, tests and trace generator were read before execution. The provenance runner that overwrites packaged outputs was not used; fresh receipts were saved separately.

**Result: 20 tests passed; the regenerated reference trace matches the stored trace as a structured object and by its canonical SHA-256. All ten package files remain unchanged.** The [execution record](../work/intake_oct18_continuity/c6_execution.json) includes runtime, command, source hashes and scope.

The tests cover idempotent retries, duplicate delivery, all six orders of three independent messages, partition/queue behavior, ACK prerequisites, local exit, actor/key-label checks, retained RAW witnesses, derived VIEWs, and hash-tamper detection. The mathematical use is concrete: distinct delivery histories can have the same operational VIEW while remaining distinguishable in RAW. Whether VIEW is sufficient depends on the requested witness.

The two keys are structural labels in this reference model. The test result is neither an exhaustive state-space proof nor production cryptographic authentication. Hash-chain consistency detects specified changes relative to retained records; it does not independently authenticate authorship or prevent wholesale rewriting without an external anchor.

## 4. Other reproducible additions

**Phase counterexample.** With θ₀=0, the states at n=1 and n=8 both have (strand,slip)=(2,0). Their next slips, at n=2 and n=9, are respectively 0 and 1. Fresh 90-digit calculations reproduce C01 P065–P078. The master already contains the exact continuous-phase repair; this adds a compact witness explaining why the two displayed labels are insufficient.

**Silver-clock arithmetic.** For f₀=39 Hz, ρP=23/19 and ρS=(1+√2)/2, the specified beat frequency is fB=f₀(ρP−ρS). With seven nodes and three beats per node at 169 BPM, TG=1260/169 seconds. Recalculation gives:

| Quantity | Value |
|---|---:|
| fB | 0.133361849514120… Hz |
| TB=1/fB | 7.498396307814559… s |
| TG | 7.455621301775148… s |
| TB−TG | 42.775006039411… ms |
| 360(1−fBTG) | 2.053639410622… degrees per gate |
| TG/[60(1−fBTG)] | 21.782659399349… minutes per full relative slip |

These values depend on the declared convention. They establish arithmetic mismatch, not physical coupling, synchronization, cognitive benefit or the outcome of the separate two-clock protocol. The earlier triadic toy comparison and later two-clock plans retain their own evidence status.

**Explicit Brjuno value.** Put φ=(1+√5)/2. Under C02's Gauss-map definition of Φ, α=(3−√5)/2=φ⁻² has first Gauss iterate φ⁻¹ and all subsequent iterates equal φ⁻¹. A geometric series gives Φ(α)=3logφ≈1.443635475178810. This is a direct calculation, not a new linearization theorem. The existing model is already a rigid rotation or an explicitly constructed conjugate, so it does not need an existence theorem for its conjugacy.

## 5. Corrections required before reusing `_Math2`

Line references below are to the preserved C02 text. Some passages elsewhere in the conversation qualify earlier claims; the corrections here prevent isolated erroneous statements from entering the master.

| Location | Problem | Correct treatment |
|---|---|---|
| 1571–1575, 1886–1894, 1940–1943 | Density equation does not follow from the stated set-Jacobian law | For μ=ρdx and μ(gE)=∫E(g′)^s dμ, change of variables gives ρ(gx)g′(x)=ρ(x)(g′(x))^s |
| 1912–1919, 2059–2063 | Chart direction is unclear; (h′)^s is not the density in the master's convention | For g=h⁻¹Rαh with smooth h′>0, μs=Zs⁻¹(h′)^(1−s)dx; occupation is s=0, and s=1 is Lebesgue for every such g |
| 393 and broad analytic-linearization passages | Local Brjuno results, global circle theorems and individual germs are conflated | Preserve the specific theorem's domain and quantifiers. A linear rotation germ is linearizable even at a non-Brjuno angle |
| 837 | Bounded-type quadratic Siegel boundary statement is reversed | The boundary is a quasicircle containing the critical point; see Petersen–Zakeri, introduction p.3 |
| 962 | Ψ(Q) uses ordinary absolute value of kα | For circle small divisors it needs distance to the nearest integer, ‖kα‖. The written expression has maximum 1/|α| for Q≥1 and cannot encode small divisors |
| 1005 | Unbounded continued-fraction coefficients are said to exclude every finite Diophantine type | They exclude bounded type, not all finite types. For example aₙ=n grows while qₙ grows at least factorially, so the standard continued-fraction bounds still give a finite Diophantine exponent |
| 410, 506–523 | Renormalization eigenvalues, scaling exponents and information refinement are blurred | With rescaling factor b, an eigenvalue Λ=bʸ yields y=logΛ/logb. A refinement diagram alone specifies no renormalization operator or spectrum |
| 2045–2049 | Riesz representation is invoked for any distribution | Riesz requires an appropriate continuous functional on continuous functions; a general distribution is not necessarily a measure. A stronger uniqueness theorem needs its own hypotheses and proof |
| 2123–2131 | Correct inverse-form identity is followed by an incorrect explanation | For s<0, the displayed weight is (f′∘f⁻¹)^(−s): a positive power of the **forward derivative at the preimage**, vanishing at critical values; it is not a divergent positive power of the inverse derivative |
| 2183–2187 | The written Arnold family is called monotone past its critical parameter | f′λ(1/2)=−2πλ₂. For λ₂>0 it is not an orientation-preserving homeomorphism, so the quoted multicritical-circle result does not apply on that side |

For the corrected density formula, differentiate h∘g=Rα∘h to obtain h′(gx)g′(x)=h′(x), then substitute ρs=(h′)^(1−s)/Zs into the correct Jacobian identity. Here Zs=∫₀¹(h′)^(1−s)dx is finite and positive because h′ is continuous and bounded away from zero. Mere absolute continuity is not being substituted for these hypotheses. At s=1, ρ=1 is an immediate check that exposes the survey's equation error. This also agrees with the master's tensor-density norm weight 1−2Reλ when s=2Reλ.

An independent nonconstant-chart fixture at ε=1/4 tested 257 points for each s∈{−1,0,1,2}. Correct identities have maximum floating residual 4.45×10⁻¹⁶; using the survey's power produces residuals greater than 0.6. This illustrates the error; the change-of-variables derivation establishes the formula.

Primary literature checked:

- [Eliasson, Fayad and Krikorian, §§1.3–1.5](https://arxiv.org/html/1810.07107v1): Brjuno yields the stated local analytic results; the unrestricted global analytic circle class uses Herman's arithmetic condition. The paper distinguishes these explicitly.
- [Petersen and Zakeri, introduction p.3](https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n1-p01.pdf): bounded-type quadratic Siegel disks are quasidisks with the critical point on their boundaries.
- [Goncharuk and Yampolsky, Definition 1 and Theorem 2](https://arxiv.org/html/2404.03780v1): the negative-exponent identity and uniqueness theorem concern multicritical orientation-preserving circle homeomorphisms. Its introduction gives the Arnold amplitude interval up to 1/(2π). [Journal publication](https://www.aimsciences.org/article/doi/10.3934/dcds.2024169).

The wider hedgehog/Loewner and renormalization survey remains background. This intake does not certify every literature attribution, universality assertion, distributional claim or geometric interpretation in that conversation. It supplies no derived map from those theories to the toroidal sampler or thermodynamic application.

## 6. What the orbit note adds

C03 already distinguishes exact quotient, driven cocycle, augmented-state closure, formal proposal and empirical instantiation. Its practical audit asks what a representation preserves, what routes remain available, what history is retained, which decision is made, whether that decision depends only on the retained record, and how it can be corrected or appealed. This is useful operational design; the normative remedy requirement is declared rather than derived from a mathematical theorem.

A compact record is `(domain, retained map, witness/decision, available routes, history record, comparison law, counterexample, remedy, evidence status)`. Deterministic closure compares successors; stochastic closure compares complete conditional successor laws. Repetition, equal output or a shared diagram is insufficient to identify a social or platform mechanism. These qualifications were already present in the user's integration note.

C04 indexes older v3/OMNIBUS work. Its index does not supersede the later v7.79-r1 source or qualified Hidden Quotient v1.7 already retained in the master. No instructions embedded in these source files were treated as new requests to execute programs or modify their linked manuscripts.

## 7. Delivery and remaining scope

Consolidation 2.5 adds the elementary theorem and refinement, phase counterexample, corrected density family, conditional silver-clock calculation, reproduced C6 result, and operational audit record. The original four files and recovered package remain unchanged. The kit includes them, the new review and receipts, and the existing intact phase and toroidal releases.

The original accepted-event discrepancy remains −1,352. Configuration enforcement, lossless recording, restart/conformance validation and a full prospective replacement replay remain outstanding. Physical Q1/Q2/Q3, TTSC and the separately specified two-clock experiment were not run here. The previous 36 phase/lattice/throat tests were not redundantly rerun; their fresh 2.4 receipts are carried unchanged and are separate from the new 20 C6 tests.

This intake updates local portable artifacts. It makes no new Drive, Google Docs, GitHub, email or other cloud change. The [machine-readable intake receipt](GEOMETRY_CONTINUITY_INTAKE_2026-10-18.json) records source preservation, lineage, test outputs, numerical fixtures and delivery identities.
