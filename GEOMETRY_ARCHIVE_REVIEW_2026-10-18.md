# Geometry archive review — 18 October 2026

**Disposition:** incorporated into portable master **2.6**. The strongest additions are an exactly reproduced phase verifier, a concrete reported-data example of witness deletion, corrected source credit, and necessary repairs to the proposed three-tempo experiment. No physical experiment or cloud document edit occurred.

The mathematical core gains useful examples and reproducible support. The new packet does not resolve the historical toroidal sampler discrepancy or establish a physical effect of a special tempo, prime, or isotope label.

## 1. What these two archives contain

| Input | Bytes | SHA-256 |
|---|---:|---|
| `03-transition-acceptance-table-md--d8437928.zip` (A01) | 259,279 | `0f73462c9246d9131b2b2ac8a3de0d3ce2d66eeb97783137f8afb266b74e1abe` |
| `geometry_and_quotients.zip` (A02) | 1,611,820 | `ee5d79244595802dacc0d2993e473060bb1b7aee10ad21e195efd1ec17b209e3` |

A01 has 38 text entries. A02 has 118 entries: 116 texts, one directory, and a nested ZIP. All 38 A01 texts occur individually in A02 with identical bytes, and the nested ZIP is A01 itself, also byte-identical. Across the two outer inventories there are **116 distinct texts**, not 154 independent documents. Reading the nested ZIP adds no independent source.

All entries were inventoried, hashed, and read for ZIP integrity. Comparison against 918 earlier workspace text snapshots found one distinct exact match and 20 additional distinct matches after whitespace-only normalization. Those are lineage findings, not independent replications. In particular, Qualified Hidden Quotient v1.7 is identical to the earlier source. An unmatched byte sequence can still be an older work with different export formatting.

Review depth is recorded per entry in `source_review_scope.json`. All texts received inventory/header/lineage screening; selected mathematical, protocol, and code passages received detailed review. This was **not an exhaustive proof audit of the 116 texts**, especially the long Math 3–5 surveys. Originals and preserved copies were rehashed after work and remain unchanged.

## 2. The recovered phase verifier actually reproduces

Member **A02-M0011** contains a complete Python verifier in a fenced block, its JSON result, and a pasted CSV. The recovered program's SHA-256 is exactly the report's recorded value:

`30ba2afb9c62977b4d206598de2f31b3376c11d738a9b6897be878593cc6b898`

After inspection, the program was run in a separate local directory. Every field of the new JSON result equals the source's result, including the script hash. It freshly checked:

- **500,000 departures:** five initial states, each followed for 100,000 steps; exact phase, bin, strand, slip-count and discrepancy identities, with gaps 9 or 10.
- **325 monomials through total degree 24:** the stated sign and order-three symmetry conditions, with first phase-dependent degree six.
- **119 open initial-phase cells and all 119 boundary points:** exhaustive phase sensitivity for the declared atomic-number indexing on Z=1,…,118.

Classification uses exact arithmetic in Q(√5); floating point proposes a floor that is then corrected by exact comparisons. This is a reproduction of the report's equation-level checker. It is separate from the original release verifier and from the 36 phase/lattice/throat tests already reproduced for master 2.4.

The symmetry argument is elementary beyond the finite enumeration: for nonnegative integers p,r, invariance of z^p z̄^r under z→−z and z→e^(2πi/3)z means p+r is even and p−r is divisible by three. Since p+r and p−r have the same parity, this is equivalent to p−r being divisible by six. The first nonconstant angular terms are z⁶ and z̄⁶; under Φ=z² they become Φ³ and Φ̄³. This conclusion requires the two declared symmetries. It is not a measured field coupling.

The source's pasted CSV ends at `88,Fal`. The fresh run produced a complete **118-row** table; the truncated source was preserved unchanged. The full regenerated table is included as an output of this verified program, rather than represented as recovered original bytes.

### What the atomic-number exercise says

The mapping n=Z−1 with initial residual phase zero is explicitly exploratory. It marks 13 labels, of which three are prime: 59, 97, and 107. Across all starting phases, the marked-prime count varies from one to six and the total marked count from 12 to 13.

For a uniformly distributed initial phase, each individual Z has the same marking probability τ. Consequently, E[marked primes]=30τ and E[all marked labels]=118τ; their ratio is **30/118**. This is a ratio of expected counts, not an expectation of a random ratio. There is no prime enrichment in these phase-averaged counts. No spectra, bonding, isotope response, or other chemical behavior was tested. The exact phase result survives; the proposed interpretation requires an independently specified physical witness.

## 3. The three-tempo protocol needs an amendment before data collection

Members **A02-M0002/M0003** specify a prospective comparison of 169 BPM, 168 BPM, and a beat-derived calibration tempo. The source is explicitly **not yet run**. Historical audio and the later 39 Hz comparison are correctly kept separate; that distinction is retained.

Let δ=23/19−(1+√2)/2, fB=39δ, TG=1260/b seconds and b*=1260fB. Recalculation gives b*=168.035930387791493… BPM. The printed ten-decimal value is a rounded setting.

| Tempo b | Beat-phase deficit 360(1−fB TG), degrees per gate | 39 Hz cycles per gate |
|---|---:|---:|
| 169 | +2.053639410622 | 290.769230769231 |
| 168 | −0.076993688125 | 292.500000000000 |
| b* | 0 exactly by definition | 292.437456004768… |

The magnitude of the 169 residual is about **26.6728** times the 168 residual. At fixed 39 Hz, 169 ranks second among the 41 integer tempos 150–190. Across carriers 35–43 Hz and those tempos, 16 pairs are strictly better and three tie: (36,156), (39,169), and (42,182). They occupy ranks 17–19; **18 is their midrank**. The source's “18/369” should state its tie convention and cannot identify a unique pair.

### A. The measured phase is not yet linked to the calculated phase

b* closes the **difference-frequency phase fB TG**. The protocol instead adds a continuous **39 Hz carrier** and measures its phase at loop/reset markers; those marker definitions are still to be filled in. It does not specify a generated difference-frequency signal or a calibrated observation map from the fB phase to that endpoint.

If markers use TG, a marker-relative 39 Hz coefficient advances by 2π·39TG. None of the three tempos makes that an integer number of cycles. A coefficient referenced to global recording time behaves differently: the phase of an ideal continuous 39 Hz tone can remain constant for all three tempos. The coordinate convention therefore matters. Neither construction automatically supplies the stated beat-closure ordering.

The comparison can still be a legitimate test of **tempo-dependent room response** after its markers, phase basis, reference, and tolerances are specified. It cannot yet be interpreted as testing the silver-beat closure mechanism. Adding a new pair of beat-generating tones would be a separate, prospectively specified experiment.

### B. The assignment mechanism and permutation test disagree

The source fixes six code orders and randomly maps X/Y/Z to the tempos **once**. That creates six possible assignments of actual tempos to the full schedule. The proposed analysis instead permutes labels independently in all six sessions, using 6⁶=46,656 assignments that this mechanism did not generate.

An inclusive exact randomization p-value over six equally likely assignments is at least **1/6**; the source's p≤0.05 rule cannot be attained under that design-based test. A 46,656-permutation analysis would need genuine independent within-session randomization or an additional, justified exchangeability model. Counterbalancing alone supplies neither.

A concrete prospective repair preserves one occurrence of every order: assign the six orders uniformly at random to the six sessions, giving **6!=720 possible schedules**, and analyze that same assignment space. Alternatively, randomize each session independently and use 46,656 assignments, while dropping the guarantee that every order occurs exactly once. Neither change may be backdated into the original protocol or applied retroactively to claim randomized evidence.

### C. Name the outcome precisely

The registered ΔPLV is PLVroom−PLVref, a **difference of phase concentrations**. It is not the concentration of the phase difference, |mean exp(i(φroom−φref))|. For room=reference=[0,π], the former is zero and the latter is one. For room=[0,0], reference=[0,π], the former is one and the latter is zero. Both calculations were checked. They measure different things; switching them after results would change the endpoint.

The accompanying [proposed protocol amendment](GEOMETRY_BPM_PROTOCOL_AMENDMENT_PROPOSED_2026-10-18.md) preserves ΔPLV under its correct name, supplies a matching balanced randomization design, and narrows the interpretation. It is a local proposed revision, **not an adopted freeze or completed run**. A maximum-statistic randomization test is described under the joint sharp null; strong familywise claims under partially true nulls require their own justification.

## 4. A useful worked geometry example from published measurements

Member **A02-M0062** freezes a two-record example from LBCO at x=1/8. The primary paper reports oxygen-isotope exponents −0.57(6) for spin-stripe ordering temperature and +0.46(6) for superconducting transition temperature. These values were checked against the [authors' paper](https://arxiv.org/abs/1405.6846), published as [Physical Review Letters 113, 057002](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.113.057002).

Let D consist of those two reported records, W be the reported exponent, and π retain material, nominal composition, isotope intervention and study while deleting the observable/probe label. The two records share π but have different W. Their reported central values differ by **1.03**. Interpreting each printed uncertainty only as its displayed ±0.06 interval gives [−0.63,−0.51] and [0.40,0.52], with pairwise distances in **[0.91,1.15]**. That interval arithmetic was independently checked exactly.

This is a clear **report-level witness-deletion counterexample**: an untyped “isotope response” loses which quantity changed. Retaining the observable resolves this two-record example.

The source labels its gate “CERTIFIED EMPIRICAL NON-DESCENT.” Its reported uncertainties, however, are not guaranteed bounds on the unknown physical parameters or a declared simultaneous confidence set. The master therefore retains the source's recorded status while stating the narrower conclusion it supports. The arithmetic is conditional on the supplied intervals; it is not error-free physical certification. No new experiment, global geometry, or minimal causal repair follows. Chemistry-freeze status is unchanged.

## 5. Source credit and older scaffold statuses

**The density and Brjuno repairs already existed.** Geometry v1.3 (**A02-M0013**, §§26–27) derives h′^(1−s) in the stated chart and 3logφ in the Gauss-map convention. Math 3 (**A02-M0030**) explicitly carries those repairs forward. The v1.3 text matches the previously recovered repository source after whitespace-only normalization. Master 2.5 rechecked and incorporated them from the continuity packet; it did not originate them. Master 2.6 corrects that lineage explicitly.

**The A.10 transition package remains a scaffold.** A01-M0000 has eight proposed move rows but pending source and code bindings. A01-M0001 identifies a public document snapshot while expressly withholding an executable-source claim. Its recorded byte counts/hashes match the supplied A10-01, A10-02, and A10-03 exactly. A10-04 through A10-10 are named in the manifest but their corresponding hashed files are absent from these two ZIPs. This is a bounded archive-coverage statement, not a claim that the files do not exist elsewhere.

The listed 20,000 core-hour ceiling and 14,000 forecast ceiling are planning limits; a completed forecast/run is not present. Old NOT_RUN scaffolds do not erase later, separately supported finite-validation PASS results. Conversely, the later finite checks do not fill these execution bindings, complete the replacement sampler, or resolve the historical accepted-event difference of −1,352.

## 6. Keep the toy prime-clock validators in their declared domain

The archive includes Python-shaped toy models and a `ParallelLedgerValidator` (**A02-M0076**, with related members M0051–M0058). Static review found an assigned label `q_parity = 1 if prime(node) else node % 3 + 1`. It takes values 1,2,3 and is not the toroidal binary parity q. Some related variants use four classes. Prime traversal advantages in the toy paths are also assigned in the cost function; they are not discoveries about prime geometry.

The validator labels an arithmetic clock inconsistency “CLOCK FRAUD,” equal composite nodes “CONTAMINATION,” and a successful structural check “LINEAGE HOLDS PROVENANCE.” Those conclusions exceed the predicates. It checks no authenticated origin or record hash chain; missing clock values default to zero; missing nested fields can raise an error; leakage warnings alone do not prevent a successful return. The threshold 0.42 is a model parameter, with no calibration supplied here.

Useful revisions would call these `prime_bucket`, `clock_inconsistency`, and `coincident_node`, report missing fields explicitly, and distinguish schema checks from provenance. These source files were not executed or rewritten. They do not add an incident, actor, transmission, or production-security finding to the master.

## 7. Delivery and verification

The updated [master](GEOMETRY_MASTER.md) carries the bounded results above. The [intake receipt](GEOMETRY_ARCHIVE_INTAKE_2026-10-18.json) records source identity, per-entry coverage, fresh execution and exact arithmetic checks. The kit preserves the two original ZIPs, selected source texts, the complete recovered verifier and its regenerated outputs, the proposal, and the earlier releases/receipts. Master 2.5 is retained separately.

The intake did not rerun unchanged earlier release suites, open any sealed condition key, collect physical data, change Drive/Docs/repositories, or treat source-contained commands as user instructions. Literature checking was targeted to the paired isotope measurements. The large survey corpus has not received a blanket scientific endorsement.
