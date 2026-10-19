# read-05 — relevance to the geometry master

**Reviewed 19 October 2026. Integrated into portable master 2.7.**

There is useful material here. The strongest mathematical addition is a precise connection between witness loss, the objective used to score an answer, and the class of rules permitted to act on retained information. The packet also helps make earlier empirical failures and version distinctions more visible. Many other files are repeated sources, alternate exports, background research or material requiring a separate review.

This was a complete byte inventory with **selected content review**, not a scientific audit of every document. The accompanying catalogue records that distinction rather than labeling every unreviewed file irrelevant.

## Archive and source integrity

| Item | Result |
|---|---:|
| Supplied ZIP | `read-05.zip` |
| Compressed bytes | 305,086,795 |
| ZIP entries | 4,921 |
| Uncompressed bytes across entries | 1,532,575,607 |
| Distinct nonempty contents | 1,647 |
| Empty entries | 54 |
| Distinct contents matching earlier workspace files exactly | 480 |
| Additional distinct contents matching after whitespace normalization | 37 |
| Filenames used for more than one distinct content | 179 |
| Entry integrity failures | 0 |

The original ZIP and the preserved copy have SHA-256:

`6c96e1f585ee23eb6ed745322953dd6f96dfd34e8d96a7c26b65e66a75153a37`

All entry bodies were streamed, CRC-checked and hashed. Duplicate filenames were addressed by their ZIP entry index, so later entries could not overwrite earlier ones. Byte identity, whitespace-normalized similarity and removal of export line-number/paragraph prefixes were recorded as separate relationships. Fourteen distinct text objects match other archive texts after those specifically recorded presentation transformations; they remain distinct original byte objects.

The inventory includes TXT, CSV, HTML, PDF, RTF, XML, DOCX and XLSX. Most binary formats received identity screening rather than a document-layout or formula audit. Nine distinct bodies exceeded the initial 8 MiB text-screening limit. Four selected large/related RTFs were subsequently converted for triage; five large bodies remain inventory-only. Large bodies remain available in the preserved original ZIP. Empty placeholders cannot supply the contents suggested by their names.

## What to use, retain or defer

| Source or group | Relevance | Decision |
|---|---|---|
| **Elimination Geometry**, supplied v1 PDF, R05-1365 | Direct mathematical connection: objective-derived excess loss, admissible rules, and local versus shared solutions | Incorporate selected definitions and a separately derived finite squared-loss example |
| Geometry Extension Test report, R05-2353 | Earlier 72-bank failure, full-corpus 39-screen null and a narrower later-cohort lead | Carry these existing source-reported results explicitly; no new empirical rerun |
| Focused geometry analysis, R05-0322 | Claim criterion, preserved referents, correction history and delivered answer | Support the existing operational chapter; no new universal theorem or actor attribution |
| Current Direct Service correction, R05-0678 | Explicit 69/198 versus 70/198 coding difference | Preserve the already adopted case-sensitive definition; do not count the two figures as independent cohorts |
| Thermodynamic v3 texts and diff, R05-1386/1392/1393 | Different versions add resource, timing and conditioning witnesses | Version context; additional bookkeeping does not measure energy or benefit |
| GQG Rune guide and test log, R05-1399/1406 | Finite model/compiler scope and historical verification | Supporting documentation; a copied log is not fresh execution or a complete executable package |
| RHEA document-lineage reconciliation, R05-0001 | Source succession, internal duplication and claim provenance | Context for source handling; source-reported comparisons remain attributed |
| NEO quotient-split note, R05-1019 | Suggests comparing different retained descriptions | Defer the empirical conclusion: different similarity scores alone do not prove an exact quotient collision |
| 985.5-kya convergence note, R05-1030 | Distinguishes a selected target from interval overlap and a causal finding | Methodological context only; dating and causal claims were not revalidated |
| Kinetic Blocks PDF, R05-0394 | Possible interface/physical-assembly application | Adjacent reference; no demonstrated upgrade to the current quotient proofs |
| Maths3 and long mixed surveys, R05-0393/3827/3828 | Jacobi/hypergeometric material and broader conversations may support later work | Retain as background; no blanket theorem verification or automatic import |
| Other scientific, historical, literary, clinical and incident material | Potentially useful for other tasks | Keep in the source archive; no unrelated bodies added to the geometry master |

“Defer” describes this review's scope and missing connection. It is not a finding that the material is false or permanently useless.

## The mathematical upgrade: price the lost witness

The supplied **Elimination Geometry** draft distinguishes finding an optimal answer separately for each case from finding one rule in an allowed class that works across cases. Its objective-derived defect is

\[
J(x)=\inf_a H_x(a)\in\mathbb R,
\qquad \delta_x(a)=H_x(a)-J(x)\ge0.
\]

The finite value of J is part of the premise; subtracting two infinite costs would not define this defect. Once the allowed rule class and population weights are specified, the best achievable average defect is a different object from the loss of one fitted implementation. The supplied PDF's relevant material is on PDF pages 25–32, especially Definitions 2.1/2.4 and §2.3. The [public v1 record](https://arxiv.org/abs/2608.17646v1) and selected public text agree with the title, authors, version label and 288-page structure. Publisher-to-archive binary identity was not established. The [current arXiv record](https://arxiv.org/abs/2608.17646) lists a later v2; this integration is explicitly based on the supplied v1, not a full review of v2.

### A finite result that connects directly to our π/W framework

Let D be a finite nonempty state set, p_x>0 with Σp_x=1, π:D→Q the retained observation, and W:D→ℝ the desired answer. Fix squared-error cost and allow every real-valued rule g on the attained labels Q=imπ. Define

\[
P_q=\sum_{\pi(x)=q}p_x,
\qquad
\bar W_q=P_q^{-1}\sum_{\pi(x)=q}p_xW(x).
\]

Then

\[
\begin{aligned}
L(g)&=\sum_xp_x\bigl(g(\pi x)-W(x)\bigr)^2\\
&=\underbrace{\sum_xp_x\bigl(W(x)-\bar W_{\pi x}\bigr)^2}_{L^*(\pi)}
+\sum_qP_q\bigl(g(q)-\bar W_q\bigr)^2.
\end{aligned}
\]

To prove it, write g(q)−W(x) as [g(q)−W̄_q]+[W̄_q−W(x)] inside each fiber. The cross term sums to zero by the weighted-mean definition. The second term is nonnegative and vanishes at g(q)=W̄_q, so the displayed minimum is attained.

This gives an objective-specific cost of the lost witness. Under the stated positive weights, L*=0 exactly when W is constant on every retained fiber. It is the familiar conditional-variance calculation on a finite domain, not a claim of a new theorem. The archive's objective/architecture distinction makes it especially useful here.

For a balanced W∈{0,1} pair whose label has been erased,

\[
L(c)=\tfrac12c^2+\tfrac12(c-1)^2=(c-\tfrac12)^2+\tfrac14.
\]

The best constant answer is 1/2, with unavoidable mean squared error **1/4**. More training inside that same constant-only class cannot remove the floor in this declared model. Keeping W as an available coordinate removes the floor when the rule may use it. If the permitted rule remains constant, the same 1/4 floor survives even though the input now contains W. **Sufficient retained information and an admissible rule that can use it are separate requirements.**

For an unbalanced pair with P(W=1)=p, the floor is p(1−p). It approaches zero as one state becomes rare, while the largest separation between the two possible targets remains one. A worst-case separation and an average cost therefore answer different questions. These weights are model assumptions, not estimated frequencies from the archive.

There is also an attainment boundary. On a one-point domain with target zero, restrict actions to c∈(0,1] and use cost c². The infimum is zero because c=1/n approaches zero, but no admissible action attains it. That is a different action class from the unrestricted finite-label rules used above. A zero infimum alone does not certify an exact admissible repair.

The algebraic proof is supplemented by exact rational checks over all 15 partitions of a four-state model under three positive weight vectors: 45 finite models, 4,665 loss-decomposition evaluations and 180 refinement comparisons. All passed. Binary cases and the constant-rule restriction were checked separately. These are constructed calculations, not evidence that a particular AI system, physical field or human workflow has this loss function or architecture.

## A useful correction to the empirical analogy

The NEO note compares closeness under one metric with weaker similarity under another. That can motivate a richer observation, but it does not by itself exhibit x,y with **equal π(x),π(y)** and unequal W. A concrete counterexample to the inference is π(x)=x on {0,0.001}: the two points are 0.001 apart under one metric and 10 apart after a 10,000-fold rescaling, yet π is injective and no information was lost.

For an approximate empirical quotient, define the grouping rule, tolerance, uncertainty and target before drawing the non-descent conclusion. The note's raw orbital reconstruction and astronomical claims were not revalidated in this intake. No dates, trajectories or composition claims from it were added to the master.

## Preserve the earlier empirical results accurately

The Geometry Extension Test source reports that all five primary lanes failed the frozen 72-model bank and that the 24→12→6 hierarchy did not pass. Its full set of 40 unique calls is null for the fixed 39-screen association. It reports a later 20-call association with missing-output counts 4/634 on +14 arrival steps and 142/5,417 on +15 steps, while the earlier half points oppositely. The source-defined **departing** alignment was null; the narrower lead uses the **arriving** transition.

The report also records removal of four exact re-shares from a purported holdout. That matters to independence and must survive export/consolidation. These conclusions were already present in the prior continuity record and upgraded source; they are made explicit in master 2.7 as a carry-forward clarification. This intake did not reproduce the row-level permutation analysis, rerun its code or promote a later-half result into a confirmed mechanism.

The RTF conversion drops embedded objects and some mathematical glyphs. It is a screening derivative, not a faithful equation edition. The main conclusions and quoted counts were cross-checked against the previously retained plain-text continuity/report sources. The exact RTF bytes remain preserved separately.

## What this review does not change

The prior exact phase mathematics, qualified Hidden Quotient theorem and separately reproduced reference software retain their existing status. The historical toroidal accepted-event difference of −1,352 remains unresolved. The complete replacement replay and physical Q1/Q2/Q3 remain unrun as previously recorded. The proposed three-tempo amendment from master 2.6 remains proposed, not an executed experiment.

No source-contained command, instruction to modify another document, phone-mode handoff or quoted approval was treated as a fresh user instruction. No archived program was run. The new calculations use a separately written, local rational-arithmetic check. No cloud source was edited.

## Deliverables and coverage

- [Portable master 2.7](GEOMETRY_MASTER.md): the useful mathematical addition and clarified carry-forward statuses.
- [Read-05 intake receipt](GEOMETRY_READ05_INTAKE_2026-10-19.json): archive identity, coverage, selected source records, fresh calculations and output hashes.
- [Relevance catalogue](GEOMETRY_READ05_RELEVANCE_CATALOGUE_2026-10-19.csv): one row per distinct content, with occurrence counts, names, hashes and review disposition. Keyword-screened candidates are explicitly labeled as such.

The compact master kit retains the selected mathematical source and review evidence. The full 305 MB mixed archive remains separately preserved and identified by hash; it is not duplicated into the compact kit. Raw unrelated document bodies are not imported into the master. PDF text extraction covered all 288 pages mechanically, while manual mathematical review was selected; PDF pages 26, 27 and 31 were also rendered and visually checked. This does not certify the monograph's remaining proofs, experiments, priority or every cited result.
