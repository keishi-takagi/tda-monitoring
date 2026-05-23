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
