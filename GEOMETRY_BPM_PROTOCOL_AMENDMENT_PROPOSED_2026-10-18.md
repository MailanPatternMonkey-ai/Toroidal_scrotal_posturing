# Proposed amendment — three-tempo room comparison

**Status: PROPOSED / NOT FROZEN / NOT RUN.** Prepared 18 October 2026 against `PCO-20260826-B04B9138`, the supplied “13-Square / Phase-Closure BPM Comparison — Frozen Run Protocol v1.0.” The original remains unchanged. This document repairs the prospective comparison; it does not authorize hardware operation, recover historical audio, or supply observations.

## 1. Correct the experiment's claim

Compare the trial-level, reference-adjusted **phase concentration difference at 39 Hz** among 169 BPM, 168 BPM, and the rounded beat-derived calibration tempo 168.0359303878 BPM, in one specified room/apparatus configuration.

The algebraic calibration is b*=1260·39·[23/19−(1+√2)/2]. It closes the calculated difference-frequency phase when gate duration is TG=1260/b. It does not close the phase of the 39 Hz carrier itself. Refer to this condition as **beat-derived calibration tempo**, not a measured “exact closure” condition.

The experiment may detect a tempo-dependent acoustic difference. It does not by itself test an instantiated silver-beat oscillator or establish a special physical mechanism. Keep the historical Phase H reconstruction separate, including the original distinction about whether 39 Hz was historically present. A future beat-phase experiment must specify its generated signal and observation map in a separate prospective protocol.

## 2. Preserve and correctly name the endpoint

Retain the original endpoint:

ΔPLV = |mean exp(iφroom,k)| − |mean exp(iφref,k)|.

Call it **difference of phase concentrations**. Its range is [−1,1]. It is not |mean exp(i(φroom,k−φref,k))|. If the latter is desired, register it separately before collecting data; do not substitute it after observing the former.

For the marker-relative version, define the complex coefficient in each 1-second Hann window using a basis exp[−2πi·39·(t−tk)], where tk is that marker's time on the common recording clock. Compute room and reference with identical windows, sample indices, and amplitude eligibility rules. Record the sign convention. A global-time Fourier basis is a different observable and must not be substituted.

Before freeze, supply the actual marker file and definition. If the intended gate is 21 tempo beats, use the common beat-unit convention and ideal tk=t0+k·1260/b, then document its mapping to actual sample indices and rounding. If the project uses other loop/reset markers, retain their exact definition and recalculate the predictions. Do not assume the displayed meter alone proves a 21-beat gate.

For an ideal continuous 39 Hz tone with 21-beat markers, the reference phase increment is 2π·49140/b modulo 2π. It is nonzero for all three conditions. Verify this arithmetic against the generated direct reference before a room run. Any claimed reference ordering must be derived from the actual finite marker sequence, window convention and retained sample range, rather than inferred from the fB calibration.

The original 1,307-second full-signal duration and removal of the first/last 60 seconds can remain. Record the resulting marker counts per condition. Different counts can change finite-sample concentration behavior and must be part of reference verification, not a post-result adjustment.

## 3. Use a genuinely randomized balanced schedule

Retain six sessions and the six orders XYZ, XZY, YXZ, YZX, ZXY, ZYX, each used once. **Before collecting any outcomes, randomly assign those six orders to sessions by sampling a uniform permutation.** Retain the draw procedure and a private assignment record. Keep the global tempo-to-code mapping concealed under the original blinding arrangement.

This supplies 6!=720 equally likely complete balanced schedules. Each condition still appears twice in each ordinal position. The previous fixed session order plus one random global code map supplies only six allocations and does not justify 6⁶ independent session permutations.

The analyst should verify the allocation procedure without opening the condition mapping early. No concealed key was accessed during this document review. If the original design has already been run, preserve that fact; this amendment applies to a new prospective run only.

An alternative design may randomize each session independently, in which case the space is 6⁶=46,656 assignments. That alternative does not guarantee all six orders occur exactly once. Do not combine the balancing guarantee of one design with the probability model of the other.

## 4. Match inference to that assignment space

Use the session-level ΔPLV values. Define the two original contrasts, averaged over the six sessions:

- Csquare = mean[Δ169 − (Δ168+Δcalibration)/2].
- Cprecision = mean[Δcalibration − Δ168].

For the proposed balanced design, enumerate the 720 allowed complete assignments and calculate M=max(|Csquare|,|Cprecision|) for each. The inclusive exact global p-value is the number of assignments with M at least as large as observed, divided by 720. Define numerical tie handling before analysis. Do not use a 46,656-assignment reference distribution for this design.

This is an exact randomization test under the **joint sharp null that assigning the tempos has no effect on the outcomes**, with the assignment process and frozen outcome procedure correctly implemented. Report both estimated contrasts and all six session values. The maximum statistic tests the declared family under that joint null; it is not, without additional argument, strong familywise protection for separately asserted contrast discoveries under every partially true null.

For a simple prospective decision rule, require the global p≤0.05 plus the original directional consistency in at least five of six sessions, and describe the result as a candidate-level tempo separation. Treat identification of which contrast carries it as an estimate requiring replication, unless a separately justified multiple-testing procedure has been frozen.

Use all six valid sessions for this confirmatory version. If any session is incomplete, retain its observations descriptively and report the confirmatory test incomplete; do not silently enumerate a different assignment space or discard failed sessions to rescue significance. Freeze any replacement-session policy before collection, with no outcome-informed rescheduling.

## 5. Complete the existing freeze sheet

The amendment does not fill missing empirical inputs. A new named protocol version must still record the apparatus and geometry, beat unit, actual render settings and file hashes, marker file, common-clock/reference verification, phase basis, calibrated tolerances, amplitude/dropout eligibility, output precision, randomized schedule mechanism, exclusions, missing-session handling, and executable analysis identity.

Retain the original blinding, handling of historical reconstruction, fixed levels/durations, and stop rules. No optional exploratory band, alternate tempo, new endpoint, or altered marker definition may enter the confirmatory result after outcomes are viewed. The archive review's arithmetic checks are preparation, not an empirical freeze or run receipt.

The precise remaining status is **NOT_RUN — proposed design repaired on paper; apparatus, marker, randomization and analysis freeze still required**.
