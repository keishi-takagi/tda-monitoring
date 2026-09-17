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

## Entry 003 — 2026-09-05 — Correction and required cross-check for Entry 002

**Date of discovery:** 2026-09-05
**Refers to:** Entry 002 (2026-09-03)
**Observed period:** 2026-08-03 through 2026-09-02 (unchanged from Entry 002)
**Status:** `exploratory`

This entry corrects the status field of Entry 002 and supplies a required
field that Entry 002 omitted. Per §7.2-1 and §7.2-2, Entry 002 is left
unmodified and this transition is recorded as a new entry.

### 1. Status correction

Entry 002 was filed with the status string
`Exploratory — no rule change made`.

That string is not one of the four permitted values enumerated in §7.2-4
(`exploratory`, `re-validation pending`, `false positive confirmed`,
`promoted to vX.X`). The correct value for the observation recorded in
Entry 002 is **`exploratory`**.

`re-validation pending` was considered and rejected: it implies an
intention to promote the pattern to a rule, and no such intention exists.
The substantive decision described in Entry 002 is unchanged —
`tda_monitoring_rules.md` remains at v1.0 and the strict inequality
`dcnt < −12` in §2.4 remains exactly as pre-registered.

### 2. Cross-check against existing frameworks (required by §7.2-3)

Entry 002 omitted this field. It is supplied here.

**Paper #6 zone classification** (Fear Habituation and Structural
Collapse), computed over the same 23 trading days:

| Component | Range over the window | Score |
|---|---|---|
| Drawdown from 252-day rolling peak (SPY) | −2.07% to 0.00% | dd_score = 0 |
| SMA50/200 ratio | 1.063 – 1.065 | sma_score = 0 |
| VIX level | 14.2 – 16.5 | vix_score = 0 |
| Realised volatility, 20d annualised | 7.2% – 14.5% | vol_score = 0 |

structural_risk = 0, fear_risk = 0 for all 23 days → **SAFE zone
throughout**. SAFE is the baseline regime in that framework (33-year mean
250-day forward S&P 500 return +11.03%).

**Other detection categories in the same window:**

| Category | Count |
|---|---|
| A1, A2, B1, D1 | 0 |
| G1 (VIX > 30) | 0 |
| C1 | 1 (2026-08-19) |
| F1 (RSI extreme) | 21 |
| F2 (Bollinger 2σ) | 13 |

F1/F2 are classical controls and fired across seven tickers (RSP 10,
SPY 8, HYG 5, IWM 4, QQQ 3, TNX 3, VIX 1) at ordinary rates.

**Interpretation.** The window was unremarkable under the Paper #6
two-axis framework and under every TDA rule except C1. The near-threshold
persistence documented in Entry 002 occurred in a period that no other
framework in this protocol flagged. This is the inverse of Entry 001,
where three classical divergences fired simultaneously and the TDA
features did not corroborate them.

### 3. Commit hygiene failure

Entry 002 was committed as `4c9fc167` (2026-09-04) with the message
`Daily update 2026-09-04` and without a signature.

Cause: the daily driver stages the entire `public/` directory before
committing. `public/tda_events_log.md` is a hand-written file governed by
§7.2, but it sits inside that directory, so the automated run picked up
the manually placed Entry 002 and committed it under the daily-update
message. This violates §7.2-6 (commit message format) and §7.2-7 (GPG
signing).

The commit had already been pushed, and a later commit was built on top of
it. Amending would require a force-push, which §7.2-7 prohibits and which
would invalidate the commit hashes that currently carry the protocol's
integrity evidence. The failure is therefore recorded rather than erased.

Remediation: `public/tda_events_log.md` is excluded from the automated
staging path, and commits to it are made manually with the §7.2-6 message
format and a signature.

### 4. No rule change

No change to `tda_monitoring_rules.md`. This entry corrects a metadata
field and supplies an omitted required field; it makes no claim about
market behaviour and modifies no detection rule.

---

## Entry 004 — 2026-09-05 — Three documented behaviours that were not implemented

**Date of discovery:** 2026-09-05
**Type:** implementation record (see §5)
**Code versions:** `monitor_tda.py` v1.2 → v1.4. `tda_monitoring_rules.md` remains v1.0.

This entry does not record a market pattern. It records three cases in which
`tda_monitoring_rules.md` describes a behaviour that the code did not perform,
and the corrections made. It is filed here because the third case changes
15,941 previously published values in `public/forward_returns_tracking.csv`,
and a change of that size to already-public data should not be made without a
contemporaneous record.

### 1. §4 forward returns were never computed

`tda_monitoring_rules.md` §4 states that realized values are computed on
subsequent monitor runs. Through v1.2 the code built tracking rows —
`signal_date`, `signal_category`, `signal_event`, `signal_ticker`,
`horizon_d`, `target_date`, `status` — and computed no returns at all.
`public/forward_returns_tracking.csv` held 94,015 rows, 93,940 of them marked
`ready`, none carrying a value.

The consequence is that no detection had ever been compared against a
published prediction interval. The C1 interval (VIX +20d, +1.86, 95% CI
[1.41, 2.31]) and the B1 interval (QQQ 20d, +4.82%, CI [+1.78%, +7.64%]) had
been in print without a single realized observation measured against them.

Corrected in v1.3. Outcomes are now recorded mechanically for every outcome
ticker at every horizon — `ret_pct_{HYG,SPY,QQQ,IWM,RSP}` and
`diff_{VIX,VIX9D,TNX}` — so that no ticker or horizon is selected after the
fact. The eight columns were appended; the seven pre-existing columns are
unchanged (verified by exact frame comparison against the prior commit), and
the `status` vocabulary (`ready` / `pending`) was deliberately left alone
rather than renamed, which would have rewritten 93,940 published rows.

The computation was applied retroactively to all existing events. Prices are
not revised, so retroactive computation introduces no look-ahead. The reason
for doing it now rather than later is that the measurement rule can still be
shown to have been fixed before the outcomes were examined; that claim would
not be available a year from now.

### 2. §5.2 `run_metadata.json` did not exist in the daily pipeline

§5.2 states that source failures are logged in `run_metadata.json`. That file
was written only by `monitor_tda.py` in standalone mode. The daily driver
wrote a DB row and no JSON, and the DB is not public. The `notes` column was
hard-coded to `None`: all 83 recorded runs carry NULL.

The clause therefore had never been satisfied by the daily pipeline. Concrete
instances that should have been recorded and were not: Brent (EIA
PET.RBRTE.D) was unavailable on 2026-08-31 and 2026-09-02, which set
`cond_brent_30 = 0` and suppressed a possible C1 on 2026-09-02 (see Entry 002).

Corrected in v1.3. `detect_source_gaps()` flags any ticker whose most recent
observation is more than four days before the target date, and the full
`run_metadata` table is regenerated to JSON on every run so that the two
cannot diverge.

### 3. Horizon calendar did not match §4 "trading days"

Implementing §1 exposed a defect that had been present all along and that was
invisible while no values were computed.

Horizons were counted on the merged price index — the union of every ticker's
dates. Brent trades on the ICE calendar, which includes sessions when the US
equity market is closed. Of 10,080 days in the merged index, **188** are days
on which Brent traded and every outcome ticker was absent: MLK Day,
Presidents' Day, Independence Day, Labor Day, Thanksgiving.

Two consequences:

- Where a target date landed on one of those 188 days, every outcome was NaN.
  1,793 rows were affected.
- Where the interval merely spanned one, "20 trading days" was 19 market
  sessions. At h=20 this affected roughly a third of all rows.

Corrected in v1.4: horizons are counted on market sessions only (9,892 of the
10,080). Effects:

| | before | after |
|---|---|---|
| all-NaN `ready` rows | 1,793 | 0 |
| C1 → VIX +20d, n | 432 | 444 |
| C1 → VIX +20d, mean | +1.737 | +1.697 |
| `target_date` values changed | — | 15,941 (17.0%) |

By horizon, the share of `target_date` values that changed: h=1 2.0%,
h=5 8.9%, h=10 16.9%, h=15 24.4%, h=20 32.6%.

**Detection is unaffected.** TDA features and control indicators are computed
on each ticker's own `dropna()` index, not on the merged index. Event counts
after the correction are unchanged from v1.2: A1 148, A2 4, B1 24, C1 445,
D1 23, F1 12,216, F2 5,207, G1 736. `verify_history.py` continues to report
the historical portion of `public/events_log.csv` as byte-identical across all
prior commits.

This defect could not have been found by inspection of the outputs, because
the affected column was empty. It became visible only when the values it
governed were computed. A protocol clause that is documented but not executed
does not merely fail to produce evidence — it conceals defects in the
machinery around it.

### 4. Three decisions recorded

**`tda_monitoring_rules.md` was not edited.** The natural place for an
implementation note is §4 itself. That file currently has exactly one commit,
`2df4af0d` (2026-05-16), and that fact — the pre-registration document has
never been modified — is the strongest single piece of evidence this protocol
has. Adding a note would make it two commits. The note is recorded here
instead. The detection rules and the §6 frozen parameters are untouched in
either case.

**The 188 stale rows in `decoupling_status.csv` were not removed.** Those
dates appear as rows in which `vix_sma10` and `delta_cnt` are both NaN, since
VIX did not trade. `decoupling_active` is therefore necessarily 0 and no
detection is affected. Removing them would delete published rows, which is a
worse outcome than leaving a harmless artefact in place. They remain.

**Code version was bumped, rules version was not.** `monitor_tda.py` went
v1.2 → v1.3 → v1.4 so that each change is traceable in `run_metadata`. These
are code versions. `tda_monitoring_rules.md` governs the detection rules and
remains v1.0, because no detection rule and no frozen parameter changed.

### 5. This entry's type is outside the §7.2-4 status vocabulary

§7.2-4 permits four status values: `exploratory`, `re-validation pending`,
`false positive confirmed`, `promoted to vX.X`. All four describe the standing
of an observed market pattern. None applies to an implementation record: the
findings here are not exploratory (they are settled), and they were acted upon
rather than left pending.

Rather than coerce one of the four or invent a fifth — the error corrected in
Entry 003 — this entry carries no status value from that list, and the gap is
recorded as something the README and §7.2 need to address. The log's stated
purpose is the recording of exploratory market observations; this entry, and
part of Entry 003, widen that purpose to operational and implementation
records. That widening is deliberate and is noted here so that it is not
mistaken for drift.

---

## Entry 005 — 2026-09-06 — Brent YoY variance in C1: measurement asymmetry, not a defect

**Date of discovery:** 2026-09-06
**Observed period:** 2026-08-03 through 2026-09-02 (23 trading days); historical
context 1987-05-20 through 2026-09-01
**Status:** `exploratory`

### Origin

Entry 002 recorded that the C1 conditions were near-satisfied for most of
August 2026 without firing. While reviewing that window, the `brent_yoy`
series was observed to move by 3.7 percentage points per day on average, with
a maximum single-day change of 8.4 points. For a 252-observation trailing
return that appeared implausibly large, and a data-quality fault was
suspected.

### Hypothesis tested and rejected

The initial hypothesis was a calendar mismatch: `brent_yoy` is computed as
`brent.pct_change(252)` on Brent's own index, and Brent (EIA PET.RBRTE.D)
follows a different calendar from the US equity market, so 252 Brent
observations need not span one year.

This was measured and is not the cause. Over the last five years, 252 Brent
observations span a mean of 365.2 calendar days (sd 3.0, range 359–374). The
window is an accurate year.

### Actual cause

Decomposing the day-over-day change in `brent_yoy` into the current-day return
and the return of the observation rolling off the back of the window, over the
August window:

| | mean \|return\| | max \|return\| |
|---|---|---|
| current day | 2.67% | 8.30% |
| base day (t−252) | 1.24% | 2.82% |

The variance originates almost entirely at the front of the window, in the
current day's oil move.

That in turn reflects the regime rather than the data. Mean absolute daily
Brent return by year:

| year | mean \|r\| |
|---|---|
| 2024 | 1.27% |
| 2025 | 1.48% |
| **2026** | **3.25%** |
| 2020 (reference) | 3.47% |

2026 is running at a volatility comparable to 2020. March 5.43%, April 4.43%,
July 4.01%. The largest single move in the August window (−8.30% on
2026-08-03) sits near the 99th percentile of the full 1987–2026 distribution
(8.09%), which is extreme but within it.

No data-quality fault was found. Repeated identical closes number 5 in the
last 758 observations. Every gap longer than three days in 2026 (2026-04-07,
05-05, 05-26, 09-01) corresponds to a holiday weekend.

### The observation worth recording

`brent_yoy` is a point-to-point comparison of two single-day prices. It
therefore inherits the current day's oil volatility in full. The other
continuous C1 input, `vix_sma10`, is a ten-day moving average and does not.
The C1 construction (§2.4) mixes a smoothed input and an unsmoothed one
against fixed thresholds.

In the August window `brent_yoy` ranged from 25.07% to 43.04%. Against the
30% threshold, `cond_brent_30` was satisfied on 17 of the 21 days for which
Brent data was available, with three value-driven crossings of the threshold
(2026-08-05→06 up, 08-25→26 down, 08-26→27 up) and three further transitions
caused by missing data (2026-08-31 and 2026-09-02 NaN, and the return from
NaN on 2026-09-01). Two days sat within half a point of the threshold:
30.45% (08-07) and 30.24% (08-25).

**The binding constraint in August was not Brent.** It was `dcnt`, as recorded
in Entry 002. On 2026-08-19, the one day C1 fired, `brent_yoy` was 36.62% —
comfortably clear of the threshold — and `dcnt` was −13. The Brent condition's
variance did not determine the August outcome; it is recorded here as a
property of the construction, not as an explanation of what happened.

### Cross-check against existing frameworks (§7.2-3)

Same window as Entry 002, and the cross-check is unchanged: Paper #6 places
all 23 trading days in the SAFE zone (structural_risk = 0, fear_risk = 0).
Among detection categories, only C1 fired (once, 2026-08-19); A1, A2, B1, D1
and G1 did not; F1 (21) and F2 (13) fired at ordinary rates across seven
tickers.

### No rule change

`tda_monitoring_rules.md` remains v1.0. §2.4 and the §6 frozen parameters are
untouched.

The smoothing asymmetry described above is a plausible design criticism, and
smoothing `brent_yoy` would plausibly reduce the variance of the Brent
condition. It is not being done. The asymmetry was noticed while examining the
August window, which makes any change motivated by it post-hoc under §7.1 —
the same reasoning that governed the `dcnt` inequality in Entry 002. A future
change would require a fresh pre-registration motivated by an episode
independent of this window.

The distinction to preserve when this material is used: *a point-to-point
threshold input inherits the full daily volatility of its series, while a
smoothed input against a fixed threshold does not* is a statement about
construction. *Brent volatility caused C1 to behave in a particular way in
August 2026* is a statement about the market, and this entry does not support
it — the August outcome was determined by `dcnt`.

---

## Entry 006 — 2026-09-08 — VIX observations on non-market days; calendar left unchanged

**Date of discovery:** 2026-09-08
**Observed period:** 1990-01-02 through 2026-09-07
**Status:** `exploratory`

### Observation

On 2026-09-07, a US market holiday (Labor Day), the price table received a VIX
observation while every equity and yield ticker was absent. The monitor
therefore treated the date as a session: TDA features were computed, and
`decoupling_status.csv` gained a row.

| date | brent_yoy | vix_sma10 | dcnt | cond_brent | cond_vix | cond_dcnt | active |
|---|---|---|---|---|---|---|---|
| 2026-09-07 | NaN | 15.021 | **−14** | 0 | 1 | **1** | 0 |

Two of the three C1 conditions were satisfied on a day the US equity market
was closed. C1 did not fire only because Brent was unavailable — Brent
publishes weekly and its last observation at the time of the run was
2026-09-01, seven days before the target date.

The VIX value is not a carried-forward duplicate. VIX closed at 14.53 on the
prior session (2026-09-04) and the 2026-09-07 observation is 15.30, a 5.3%
change.

### Frequency

Days on which VIX has an observation and all of SPY, QQQ, IWM, RSP, HYG and
TNX are absent, over the full history:

| period | count |
|---|---|
| 1990–1993 | 10 |
| 1994–2025 | **0** |
| 2026 | 3 |

Twelve days in 10,082. The 2026 dates are 05-25 (Memorial Day), 07-03
(Independence Day observed) and 09-07 (Labor Day). The 1990–1993 dates are
MLK Day, Columbus Day and Veterans Day observations from the early years of
the VIX series.

A gap of thirty-two years followed by three occurrences in one year indicates
a change on the data-acquisition side in 2026 rather than a long-standing
property of the series. The run log for 2026-09-08 shows `^VIX` returning ten
rows through 2026-09-07 while every other ticker returned nine rows through
2026-09-04.

No event of any category has ever fired on one of these twelve dates. On the
two prior 2026 occurrences `dcnt` was −11 (05-25) and −12 (07-03), neither
satisfying the strict `< −12` threshold. 2026-09-07 is the first occurrence at
which a non-market day satisfied that condition.

On 2026-07-03 Brent also reported (68.68). A day on which both VIX and Brent
report while the equity market is closed is therefore not hypothetical, and on
such a day all three C1 conditions could in principle be satisfied. On
2026-07-03 `brent_yoy` was −3.31% and the question did not arise.

### Relation to the v1.4 calendar correction

Entry 004 records a correction to the forward-return horizon calendar: 188
days on which Brent traded and no outcome ticker did were excluded from the
session count. That correction defined a session as a day on which **at least
one outcome ticker** has data. VIX is an outcome ticker, so the twelve days
described here were not excluded by it and are not excluded now.

The two cases are not comparable in scale. The Brent-only days numbered 188
and left every outcome column empty, producing 1,793 tracking rows with no
measurable outcome at all. These twelve leave seven of eight outcome columns
empty but `diff_VIX` populated, and produce no all-empty rows.

### Why the calendar is not being changed

**Technical.** The defect cannot be corrected at its source. `dcnt` is
computed on VIX's own index; removing the twelve dates from that series would
shift every W=20 and W=60 window that follows them. Ten of the twelve fall in
1990–1993, so the change would propagate through thirty-three years of
detection output. The historical portion of `public/events_log.csv` is
currently byte-identical across every commit, and that fact is the strongest
verifiable evidence this protocol has. It would not survive the correction.
Two events — an F2 in 1990 and an F1 in 1992 — also sit on non-market dates
and would have to be deleted.

A narrower change was considered: leaving the input series alone and
redefining the forward-return calendar to exclude VIX. That is technically
possible and would alter only `target_date`. It would not close the exposure
that prompted this entry, because `decoupling_status.csv` is generated over
the full index and a holiday on which both VIX and Brent report would still
satisfy the C1 conditions. A change that does not address the concern used to
justify it should not be made.

**Procedural.** The exposure was identified on 2026-09-07, and the C1 status
of 2026-09-07 is at this moment undetermined, pending Brent publication. Two
of three conditions are satisfied. Modifying the calendar while a detection
hangs on it — however the modification is scoped — is the situation Entry 002
was written to avoid. The v1.4 correction was made when nothing turned on it;
this one would not be.

`tda_monitoring_rules.md` remains v1.0. `monitor_tda.py` remains v1.4. No
detection rule, no frozen parameter, and no calendar definition is changed by
this entry.

### Cross-check against existing frameworks (§7.2-3)

For 2026-09-07 no Paper #6 zone classification is computable: the
classification requires SPY drawdown, the SMA50/200 ratio and 20-day realised
volatility, none of which exists for a day the equity market did not trade.
This is itself consistent with the observation — the date is not a session by
any measure other than the presence of a VIX print.

Across the twelve dates, no rule in any category has fired: A1, A2, B1, C1,
D1 and G1 zero, F1 one (1992), F2 one (1990).

### Follow-up

This entry will require a follow-up when Brent publishes and the C1 status of
2026-09-02 through 2026-09-07 is resolved. Four consecutive dates
(2026-09-02, 09-03, 09-04, 09-07) currently satisfy `cond_vix_20` and
`cond_delta_neg12` with `brent_yoy` unavailable, and `dcnt` has deepened from
−13 to −14 across them. Whatever those dates receive will be produced by the
rules as pre-registered, under the calendar as it stands today.

---

## Entry 007 — 2026-09-17 — C1 resolution for 2026-09-02 through 2026-09-15 (follow-up to Entry 006)

**Date of discovery:** 2026-09-17
**Observed period:** 2026-09-02 through 2026-09-16
**Status:** `exploratory`

### Origin

Entry 006 closed with a commitment to a follow-up once Brent published and the
C1 status of 2026-09-02 through 2026-09-07 was resolved. This entry discharges
that commitment. Reporting is unconditional under §3-1 of
`PREREGISTRATION_methodology_paper.md`; it would have been written in the same
form had the dates resolved to no detection.

### Outcome

| date | brent_yoy | vix_sma10 | dcnt | cond_brent | cond_vix | cond_dcnt | active |
|---|---|---|---|---|---|---|---|
| 2026-09-01 | 41.02% | 15.274 | −12 | 1 | 1 | 0 | 0 |
| 2026-09-02 | 44.02% | 15.305 | −13 | 1 | 1 | 1 | **1** |
| 2026-09-03 | 51.36% | 15.136 | −13 | 1 | 1 | 1 | **1** |
| 2026-09-04 | 57.49% | 15.076 | −13 | 1 | 1 | 1 | **1** |
| 2026-09-07 | 59.64% | 15.021 | −14 | 1 | 1 | 1 | **1** |
| 2026-09-08 | 56.13% | 15.048 | −14 | 1 | 1 | 1 | **1** |
| 2026-09-09 | 61.95% | 15.173 | −15 | 1 | 1 | 1 | **1** |
| 2026-09-10 | 79.90% | 15.506 | −15 | 1 | 1 | 1 | **1** |
| 2026-09-11 | 73.95% | 15.647 | −15 | 1 | 1 | 1 | **1** |
| 2026-09-14 | 78.62% | 15.865 | −16 | 1 | 1 | 1 | **1** |
| 2026-09-15 | 87.69% | 15.951 | −17 | 1 | 1 | 1 | **1** |
| 2026-09-16 | NaN | 16.202 | −17 | 0 | 1 | 1 | 0 |

C1 fired on ten consecutive sessions, 2026-09-02 through 2026-09-15. The four
dates suspended at the time of Entry 006 (09-02, 09-03, 09-04, 09-07) all
resolved to a detection, as did 09-08 and 09-09, which were in the same
suspended state by the time Brent published.

As of 2026-09-16 the series is in the suspended state again: `cond_vix_20` and
`cond_delta_neg12` are satisfied and `brent_yoy` is unavailable. The same
resolution is expected at the next Brent publication and is not assumed here.

### How the dates were resolved

Brent published between the run of 2026-09-10 and the run of 2026-09-11. The
former carries the note `Brent: last observation 2026-09-01 (9d before
target)`; the latter carries no gap note. Because `monitor_tda.py` regenerates
the full history on every run, the suspended dates were assigned by the ordinary
daily execution, in a single pass, under the rules as pre-registered.

Across every run in the window `run_metadata_public.csv` records
`monitor_version = v1.4`, `date_range_start = 1987-05-20`, and the §6 frozen
parameter block byte-identical. `tda_monitoring_rules.md` remains v1.0. No code
change, no version bump, and no manual intervention was made in anticipation of
the resolution or after it.

The handoff notes written on 2026-09-08 recorded the expectation that Brent
would resolve these dates in the firing direction, on the grounds that a fall
from 41% to below 30% inside one week would require a large decline in Brent
itself. The expectation was correct. It is recorded here because the useful
fact is not that the expectation held, but that nothing was done with it: the
correct response to a foreseeable detection was to leave the system alone, and
that is what happened.

### 2026-09-07: a C1 on a day the US equity market was closed

Entry 006 described this as a live exposure rather than a hypothetical, and it
materialised. 2026-09-07 is Labor Day. VIX has an observation; SPY, QQQ, IWM,
RSP, HYG and TNX do not. All three C1 conditions were satisfied and the event
was written to `events_log.csv` with `ticker = VIX`.

The consequence is visible in `forward_returns_tracking.csv`:

- Rows with `signal_date = 2026-09-07` have `diff_VIX` populated at every
  resolved horizon and all seven remaining outcome columns empty, because the
  return base date has no equity or yield price.
- The row `signal_date = 2026-09-04, horizon_d = 1` targets 2026-09-07 and is
  likewise `diff_VIX`-only.

No all-empty tracking rows are produced, which is the distinction Entry 006
drew against the 188 Brent-only dates corrected in v1.4.

This is not being corrected. The technical and procedural reasoning is
unchanged from Entry 006, and the procedural half is now stronger rather than
weaker: a detection is attached to the date, so any calendar change made now
would be a change made after seeing which way the detection went.

### Magnitudes

`brent_yoy` moved from 44.02% to 87.69% across the window. That level is at the
96.9th percentile of the 1987–2026 distribution. It is not a record: the series
maximum is 629.61% (2021-04-19), a base effect from the 2020 collapse.

`dcnt` deepened monotonically from −13 to −17. Days at or below −17 number 248
of 9,182 observations. The series minimum is −22 (2001-09-05/06).

`vix_sma10` remained between 15.02 and 16.20, never within four points of the
20.0 threshold. The VIX condition was not binding at any point in the window;
it was satisfied throughout with a wide margin, as it was in August (Entry 002,
Entry 005).

Ten consecutive active days is not a record. The longest runs in the history
are 25 days (2004-09-30 to 2004-11-03), 23 days (2005-03-15 to 2005-04-15) and
23 days (2006-04-18 to 2006-05-18).

### Decomposition of the brent_yoy move (Entry 005 method)

The day-over-day change in `brent_yoy` was decomposed into the current-day
Brent return and the return of the observation leaving the back of the window,
by the same method as Entry 005.

| | mean \|return\| | max \|return\| |
|---|---|---|
| current day | 3.68% | 10.47% (2026-09-10) |
| base day (t−252) | 1.41% | 3.87% |

Over the window Brent rose from 96.02 (2026-09-01) to 130.80 (2026-09-15), a
cumulative +36.22% across ten sessions. The corresponding t−252 base prices
moved from 67.09 to 69.69, +2.35%. **The `brent_yoy` move is a front-of-window
move in the level of Brent, not a base effect**, which is the same conclusion
Entry 005 reached for August 2026 and the opposite of the 2021 maximum
(629.61%), which was a base effect from the 2020 collapse.

The window is calendrically sound: 252 Brent observations ending 2026-09-15
span 364 calendar days.

No data-quality fault was found. Repeated closes number 5 in the last 758
observations, unchanged from the Entry 005 measurement. Every gap longer than
three days in 2026 (04-07, 05-05, 05-26, 09-01) corresponds to a holiday
weekend; no new gap appeared in this window.

The single-day move of +10.47% on 2026-09-10 is exceeded on 47 of 9,977
observations (99.5th percentile 10.33%). The level of 130.80 sits at the
99.69th percentile of the 1987–2026 Brent series; the all-time maximum is
143.95 (2008-07-03). Mean absolute daily Brent return for 2026 now stands at
3.28%, against 1.48% in 2025 and 1.27% in 2024; for 2026-09-01 through 09-15 it
is 3.98%.

This is recorded as a measurement of the input series. Whether the size of the
underlying oil move bears on the interpretation of the detection is not a
question this entry answers, and the ten-day window is far too short to be
treated as evidence about C1 either way.

### The 2026-08-19 episode reached its 20-day horizon

The single-day C1 episode of 2026-08-19 completed its +20d horizon on
2026-09-16, inside this window, and §3-1 requires it to be reported here.

| | published | observed |
|---|---|---|
| C1 → VIX +20d | +1.86, 95% CI [1.41, 2.31] | **+2.82** |

The observed value lies **above** the published interval. The direction matches
the prediction; the magnitude does not fall inside it.

Complete out-of-sample record for C1 at +20d, pre-registration onward:

| signal date | episode | diff_VIX +20d |
|---|---|---|
| 2026-06-08 | 1 | −2.79 |
| 2026-06-09 | 1 | −2.97 |
| 2026-06-10 | 1 | −6.38 |
| 2026-08-19 | 2 | **+2.82** |
| 2026-09-02 … 2026-09-15 | 3 | pending |

Two completed episodes. In-sample mean is +1.74 (n = 441 signal-days). §4-1 of
the pre-registration commits to not claiming validation unless the number of
episodes supports it, and two episodes do not. No claim is made, in either
direction, and the fact that the first directionally-consistent out-of-sample
outcome arrived in this window does not change that.

### Cross-check against existing frameworks (§7.2-3)

**A1 co-fired.** A1 (HHH cell activated, Paper #8) fired on 2026-09-10
(`cnt_z=1.90 ent_z=2.01 euler_z=1.04`) and 2026-09-11 (`cnt_z=1.88 ent_z=2.03
euler_z=1.03`), on VIX, on two dates that were also C1. The previous A1 was
2026-07-07. A1 has no published prediction interval: the justifying paper
(*Compression-Release*) is unwritten, and §7.3 leaves the interval undetermined
until it exists. The co-firing is recorded as a fact; it is not offered as
corroboration, since A1 and C1 are computed from overlapping TDA features on
the same ticker and are not independent tests.

**Classical controls.** F1 and F2 fired at an elevated rate across the window,
concentrated in credit and rates rather than in volatility: HYG RSI 12.3
(09-15) and 14.8 (09-16), TNX RSI 89.4 (09-15) and 89.0 (09-16), SPY Bollinger
z −2.20 (09-16). B1, A2, D1 and G1 did not fire.

**Paper #6 zone classification.** All eleven market sessions in
2026-09-01 through 2026-09-16 classify as **SAFE**, with
`structural_risk = 0` and `fear_risk = 0` on every date — the same
classification Entry 005 reported for the 23 trading days of August.

| date | SPY dd | sma50/200 | RV20d | VIX | str | fear | zone |
|---|---|---|---|---|---|---|---|
| 2026-09-02 | −1.64% | 1.0638 | 7.38 | 15.20 | 0 | 0 | SAFE |
| 2026-09-03 | −0.61% | 1.0642 | 8.27 | 14.32 | 0 | 0 | SAFE |
| 2026-09-04 | −0.99% | 1.0644 | 8.10 | 14.53 | 0 | 0 | SAFE |
| 2026-09-08 | −1.53% | 1.0646 | 8.32 | 15.72 | 0 | 0 | SAFE |
| 2026-09-09 | −1.99% | 1.0644 | 8.40 | 16.46 | 0 | 0 | SAFE |
| 2026-09-10 | −2.58% | 1.0639 | 8.53 | 17.84 | 0 | 0 | SAFE |
| 2026-09-11 | −1.75% | 1.0636 | 8.74 | 15.84 | 0 | 0 | SAFE |
| 2026-09-14 | −2.19% | 1.0634 | 8.82 | 17.10 | 0 | 0 | SAFE |
| 2026-09-15 | −2.63% | 1.0629 | 8.81 | 17.20 | 0 | 0 | SAFE |
| 2026-09-16 | −3.06% | 1.0625 | 8.65 | 17.71 | 0 | 0 | SAFE |

Drawdown is measured against the trailing 252-session maximum of SPY close; at
a maximum drawdown of 3.06% no alternative reference window changes `dd_score`.
Every component is well inside its lowest bucket: SPY is within 3% of its high,
the SMA50/200 ratio is above 1.06 throughout, realised volatility is under 9
against a 15 cut-off, and VIX stays under 18 on every date including its
window maximum of 17.84.

2026-09-07 receives no classification. SPY has no observation on that date, so
drawdown, the SMA ratio and realised volatility do not exist for it — the same
result Entry 006 reported, and consistent with the date not being a session by
any measure other than the presence of a VIX print.

### No rule change

`tda_monitoring_rules.md` remains v1.0. `monitor_tda.py` remains v1.4. The §6
frozen parameters, the C1 strict inequality `dcnt < −12`, the threshold values
and the session calendar are all unchanged by this entry.

The review of the `detect_source_gaps` warning threshold, noted as pending once
the C1 status resolved, is **not** being carried out now. 2026-09-16 is again
suspended on Brent availability with two of three conditions satisfied, which
is the same configuration that made the change inadvisable in the first place.
The threshold is a warning mechanism and not a detection rule, so the objection
is weaker than it was for the calendar in Entry 006 — but the review is
postponed rather than argued down.

### Follow-up

The +20d horizons for 2026-09-02 through 2026-09-15 complete between late
September and mid-October 2026. Episode 3 is the largest out-of-sample C1
episode recorded so far, and its outcome will be reported here unconditionally
and in full, regardless of where it falls relative to the published interval.

---
