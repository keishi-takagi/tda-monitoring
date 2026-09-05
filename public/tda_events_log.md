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
