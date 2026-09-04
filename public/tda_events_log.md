# TDA Events Log — Exploratory Observations

**Author:** Keishi Takagi
**Companion protocol:** `tda_monitoring_rules.md` v1.0
**Repository:** `https://github.com/keishi-takagi/tda-monitoring`
**Repository path:** `public/tda_events_log.md`

---

## Purpose

This log records **exploratory observations** about market patterns that are
not yet covered by the pre-registered detection rules in
`tda_monitoring_rules.md`. It exists to satisfy §7.2 of the monitoring
protocol, which requires that exploratory findings be documented separately
from the pre-registered rule set, with explicit acknowledgement that any
finding here is *pending re-validation* under a fresh pre-registered
protocol.

## Discipline

Entries in this log:

1. Are **not** detection rules. They do not trigger events in
   `events_log.csv`.
2. **Cannot be cited as evidence in a paper** without prior re-validation.
   Re-validation requires a version bump of `tda_monitoring_rules.md`
   (v1.0 → v1.1, etc.) that pre-registers the pattern as a new rule, plus
   accumulation of out-of-sample events under that new rule.
3. Are append-only. Once written, entries are not deleted; outcomes are
   appended as follow-up notes.
4. Should always state the date of discovery, the data range analyzed,
   the observation, and the current status (exploratory / re-validation
   pending / false positive confirmed / promoted to vX.X).

---

## Entry 001 — 2026-05-23 — Triple classical divergence on 2026-05-18/19

**Date of discovery:** 2026-05-23
**Observed period:** 2026-05-18, 2026-05-19
**Status:** **False positive confirmed** (as of 2026-05-23 follow-up)

### Observation

On 2026-05-18 and 2026-05-19, the following classical control indicators
simultaneously took extreme values:

| Date | Indicator (ticker) | Value | Threshold |
|---|---|---|---|
| 2026-05-18 | RSI 14d (QQQ) | 76.1 | ≥ 70 (F1) |
| 2026-05-18 | RSI 14d (SPY) | 73.1 | ≥ 70 (F1) |
| 2026-05-18 | RSI 14d (TNX) | 71.5 | ≥ 70 (F1) |
| 2026-05-18 | BB z-score 20d (HYG) | −2.06 | |z| ≥ 2.0 (F2) |
| 2026-05-18 | BB z-score 20d (TNX) | +2.44 | |z| ≥ 2.0 (F2) |
| 2026-05-19 | RSI 14d (QQQ) | 71.5 | ≥ 70 (F1) |
| 2026-05-19 | RSI 14d (TNX) | 70.6 | ≥ 70 (F1) |
| 2026-05-19 | BB z-score 20d (HYG) | −2.42 | |z| ≥ 2.0 (F2) |
| 2026-05-19 | BB z-score 20d (TNX) | +2.37 | |z| ≥ 2.0 (F2) |

The composite pattern — **equity overbought (QQQ/SPY) × credit weakness
(HYG BB negative) × rates spike (TNX BB positive)** — is not covered by
any rule in `tda_monitoring_rules.md` v1.0. Each F1/F2 event was
recorded individually, but their co-occurrence was not.

### Why this caught attention

The same two trading days showed **no TDA-side warning**:

- A1 (HHH cell, HYG and VIX): not triggered
- A2 (HHH → HHL transition): not triggered
- B1 (HLM cell, HYG): not triggered
- C1 (Topological Decoupling): had ceased on 2026-05-13, four trading
  days earlier
- D1 (dcnt z-score spike): not triggered

The textbook reading of equity-up × credit-down × rates-up is a
divergence-of-opinion sign that has preceded major corrections in some
historical episodes (1987-08, 2007-07, 2018-01). The fact that the TDA
side was silent while classical indicators showed this pattern was the
specific feature worth noting.

### Follow-up observation (2026-05-23)

The pattern dissipated within two trading days:

| Indicator | 2026-05-19 | 2026-05-22 |
|---|---|---|
| HYG BB z-score | −2.42 | +0.21 |
| TNX BB z-score | +2.37 | +0.93 |
| TNX (10y) | 4.67% | 4.56% |
| VIX | 18.06 | 16.70 |
| SPY | 733.73 | 745.64 |
| QQQ | 701.53 | 717.54 |

Equity continued higher, credit (HYG) fully recovered, rates eased, and
VIX declined. None of the conditions associated with the original
divergence remained.

### Paper #6 (*Fear Habituation*) cross-check

For 2026-05-15 through 2026-05-22, the Paper #6 zone classification was
computed and yielded **SAFE** on every day:

- Structural risk score = 0 throughout (SPY drawdown ≤ −1.93%, far from
  the −15% threshold; SMA50/200 ratio ≈ 1.03, above 1.00)
- Fear risk score = 0–1 throughout

The HABITUATED regime (the only adverse regime in Paper #6) requires
structural collapse (str_risk ≥ 3), which is structurally impossible
when drawdown is within −2% of the 252-day peak. The 2026-05-18/19
observation is therefore disjoint from the Paper #6 framework as well.

### Status

**False positive confirmed.** The observation does not warrant promotion
to a v1.1 detection rule. No paper claim derives from it.

### What this entry is for

This entry is filed under §7.2 of `tda_monitoring_rules.md` as the
**first explicit instance of the post-hoc analysis discipline being
exercised**. The pattern was observed, examined, cross-checked against
the existing TDA and Paper #6 frameworks, and confirmed as a false
positive within five trading days. No rule was added; no paper was
written; the protocol was preserved.

If a similar triple-divergence pattern later coincides with a major
correction in a future episode, the present entry is the documented
record that the pattern was previously observed and rejected, so any
subsequent claim must be made under a freshly pre-registered v1.1+ rule
and validated on subsequent out-of-sample events.

---

*End of log. Future entries appended below this line.*

## Entry 002 — 2026-09-03 — C1 threshold adhesion without activation, 2026-08

**Date of discovery:** 2026-09-03
**Observed period:** 2026-08-03 through 2026-09-02 (23 trading days)
**Status:** **Exploratory — no rule change made**

### Observation

Over the 23 trading days from 2026-08-03 to 2026-09-02, the three C1
conditions (`tda_monitoring_rules.md` §2.4) held as follows:

| Condition | Days satisfied (of 23) |
|---|---|
| `vix_sma10` < 20.0 | 23 |
| `brent_yoy` > 30% | 17 |
| `dcnt` (VIX) < −12 | 2 |
| **All three simultaneously (C1 fired)** | **1** (2026-08-19) |

Seventeen of the 23 days satisfied exactly two of the three conditions.
The binding constraint was almost always `dcnt`.

The specific feature worth noting is the distribution of `dcnt` relative to
its threshold:

| `dcnt` value | Days |
|---|---|
| −13 | 2 (2026-08-19, 2026-09-02) |
| **−12 (exactly)** | **7** |
| −11 | 3 |
| −6 to −9 | 11 |

`dcnt` is a discrete count (finite H1 generators at W=20 minus W=60), and
the detection rule uses a strict inequality (`< −12`). Seven of 23 days sat
exactly on the threshold value and therefore did not trigger.

### Counterfactual under a non-strict inequality

Substituting `≤ −12` for `< −12`, holding all other conditions and all
frozen parameters (§6) unchanged, the same 23-day window would have
produced the following C1 days:

2026-08-19, 08-21, 08-24, 08-27, 08-28, 09-01 — six events instead of one.

(2026-08-26 would still fail on `brent_yoy` = 27.9%; 2026-08-31 and
2026-09-02 would still fail on missing Brent data — see below.)

A single character in the inequality changes the August event count by a
factor of six. This is a property of the rule's interaction with a discrete
feature whose mass concentrates at the threshold, not a property of the
market.

### Ancillary: Brent data availability

Two days in the observed window (2026-08-31 and 2026-09-02) have
`brent_yoy = NaN` in `decoupling_status.csv`, and consequently
`cond_brent_30 = 0`. This is the EIA `PET.RBRTE.D` publication lag, a known
limitation, and §5.2 correctly prohibits silent substitution.

2026-09-02 is the material case: `dcnt` = −13 and `vix_sma10` = 15.31 both
satisfied, with `brent_yoy` unavailable. The prior trading day (2026-09-01)
recorded 41.0%, but 2026-08-26 recorded 27.9%, so the value on 2026-09-02
cannot be assumed above threshold.

This is a data-availability matter rather than an exploratory market
observation. It is noted here only because it falls inside the observed
window; the primary record belongs in `run_metadata.json` per §5.2.

No protocol change is required to resolve it. `events_log.csv` is
regenerated over the full history on each run, so once EIA publishes the
missing observations, an ordinary monitor run re-evaluates 2026-08-31 and
2026-09-02 under the unmodified v1.0 rules. Whatever C1 status those days
receive is produced by the rules as pre-registered, not by any intervention
made after seeing the outcome.

### Relation to existing rules and papers

No rule in `tda_monitoring_rules.md` v1.0 covers near-threshold persistence.
C1 is binary and records only simultaneous satisfaction, so a regime in
which the decoupling conditions are continuously near-satisfied is, by
construction, indistinguishable in `events_log.csv` from a regime in which
they are far from satisfied.

The observation is directly adjacent to the construction-sensitivity
analysis in Paper #5. **It cannot be used as evidence there.** The pattern
was identified after observing the August data, which makes any claim
derived from it post-hoc under §7.1.

### Status

**Exploratory — no rule change made.** The strict inequality `dcnt < −12`
in §2.4 remains exactly as pre-registered. The counterfactual recorded
above was computed after observing the August data; it is documented here
and deliberately not acted upon. `tda_monitoring_rules.md` remains at v1.0.

Any future use of this pattern requires a fresh pre-registration motivated
by a subsequent, independent episode — not by the window described in this
entry — followed by accumulation of out-of-sample events under that new
rule.

### What this entry is for

Entry 001 recorded a pattern that was observed and rejected. This entry
records a different case: a rule modification that was available,
identifiable in advance, and would have increased the August C1 event count
sixfold — and was not made.

Parameter freedom in TDA-based market analysis is large (window lengths,
embedding dimension, delay, normalization, cell thresholds, ticker
selection, and inequality strictness among them). Absence of specification
search cannot be proven directly. What can be shown is that specific
opportunities to search existed and were documented at the time they arose
rather than after the fact. An empty change history in §8 carries evidential
weight only alongside a record of the temptations that were declined.

This entry is filed as one such record.

---
