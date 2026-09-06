# TDA Real-Time Monitoring

Pre-registered real-time monitoring of topological anomalies in financial
markets. Companion to the Takagi (2026) TDA paper series.

## Two version numbers

They are separate and must not be conflated:

| | Current | Governs | Change policy |
|---|---|---|---|
| **Rules version** | `v1.0` | The detection rules and frozen parameters in `tda_monitoring_rules.md` | A change requires an explicit version bump and re-starts out-of-sample accumulation. `tda_monitoring_rules.md` has one commit and has never been modified. |
| **Code version** | `v1.4` | The implementation in `monitor_tda.py` | Bumped whenever the code changes, including fixes that bring the implementation into line with rules the document already specified. Recorded per run in `public/run_metadata_public.csv`. |

A code version bump does **not** imply a rules change. Every code change to
date has left the detection rules and the frozen parameters untouched; see
`public/tda_events_log.md` Entry 004 for the cases where the code did not
implement what the rules document described, and what was done about them.

## Public release schedule

This repository is divided into a **pre-registration phase** and a
**reproduction-code release phase**:

- **Now (pre-registration phase)**:
  - `tda_monitoring_rules.md` — pre-registered detection rules
  - `public/tda_events_log.md` — append-only log (see §7.2 of the rules
    document, and "Scope of the log" below)
  - `public/*.csv` — accumulated event, tracking and run data
  - `verify_history.py` — third-party verification script (see below)
- **Upon publication of the companion methodological paper**:
  - `monitor_tda.py` — the public reproduction code

`main_live.py`, the operational driver, is **not** scheduled for release. It
contains scheduling, retry, credential and push logic specific to one
deployment and carries no detection logic. Everything that determines what is
detected, and everything that determines the recorded outcomes, is in
`monitor_tda.py`. Reproducing the published CSVs from raw prices requires only
that file.

Pre-registration is established by the commit history of
`tda_monitoring_rules.md`, the running record of `public/*.csv`, and the
append-only history of `public/tda_events_log.md`.

## Verification

`verify_history.py` checks that the portion of `public/events_log.csv` dated
before the first monitor run is byte-identical across every commit that has
touched the file. Because the monitor regenerates the full 1987–present
history on each run, any change to the detection logic would necessarily alter
those rows.

```
python3 verify_history.py
```

The check is over every commit, not the two endpoints, so a change made and
later reverted would also be detected.

## Detection categories (from `tda_monitoring_rules.md`)

### Main (TDA, paper-based)

| Category | Detection | Reference paper |
|---|---|---|
| A1 | HHH cell activation | *Compression-Release* — **in preparation, not yet public** |
| A2 | HHH → HHL transition | *Compression-Release* — **in preparation, not yet public** |
| B1 | HLM cell activation | *Chemical Potential* (Takagi 2026c) |
| C1 | Decoupling 3-condition fire | *Energy TDA* (Takagi 2026 Energy) |
| D1 | dcnt z-score spike | *Energy TDA*; *Compression-Release* secondary |

A1 and A2 are pre-registered against a paper that has not been written. That
ordering is deliberate — the rule is fixed before the theory is published,
rather than after — but it means two of the five main rules currently have no
public theoretical justification, and their prediction intervals in §4 of the
rules document are still blank. Papers are cited here by title rather than by
series number, because the series numbering does not extend to unpublished
work.

### Control (classical, non-TDA)

| Category | Indicator |
|---|---|
| F1 | RSI 14-day extreme |
| F2 | Bollinger Band breach (2σ) |
| G1 | VIX > 30 |

See `tda_monitoring_rules.md` for full details, including computation
parameters and recorded feature set.

## Public data files

| File | Description |
|---|---|
| `public/events_log.csv` | One row per detected event (date, category, ticker, severity, details). Accumulates over time. **Automatically generated.** |
| `public/decoupling_status.csv` | Per-day Energy TDA 3-condition status (Brent YoY, VIX SMA10, Δcnt). **Automatically generated.** |
| `public/forward_returns_tracking.csv` | Forward-return tracking for each detected event at horizons {1, 5, 10, 15, 20} trading days, with realized outcomes for every outcome ticker at every horizon. **Automatically generated.** |
| `public/run_metadata_public.csv` | One row per monitor run: code version, history range recomputed, frozen parameters in force, event count, and any data-source gaps detected. **Automatically generated.** |
| `public/tda_events_log.md` | Append-only prose log. **Hand-written**, follows the discipline in §7.2 of `tda_monitoring_rules.md`. Never staged by the automated pipeline. |

Outcomes are recorded for every outcome ticker at every horizon, so that no
ticker or horizon is selected after the fact. Price tickers carry percent
returns (`ret_pct_*`); index and yield levels carry level differences
(`diff_*`). Horizons are counted in market sessions.

The git history of these files serves as the running timestamp record: each
commit records the state of detection at that point in time.

### `events_log.csv` vs `tda_events_log.md`

Despite similar names, these two files have **different roles** and must not
be confused:

| Aspect | `events_log.csv` | `tda_events_log.md` |
|---|---|---|
| Authorship | Automatically generated by the monitor | Hand-written by the author |
| Content | One row per rule-triggered detection | Prose entries on observations not covered by any rule, and on the operation of the protocol itself |
| Update cadence | Daily (per monitor run) | Append-only, as entries arise |
| Citable as evidence in papers | Yes (rule-based, pre-registered) | **No** — only citable as evidence that the §7.2 discipline is being exercised |
| Schema | Fixed CSV columns | Free-form Markdown entries with required metadata fields |

## Pre-registration

The detection rules in `tda_monitoring_rules.md` are pre-registered as of the
initial commit of this repository. Any subsequent change to the rules is
recorded as an explicit version bump (e.g. v1.0 → v1.1) with a commit. The git
history establishes the timestamp.

### Discipline for the log (§7.2 of the rules)

1. **Append-only.** Past entries are not edited or deleted.
2. **Follow-ups and status transitions.** Both forms are permitted and both
   are in use. A follow-up may be appended within the original entry as a
   dated sub-section (Entry 001), or recorded as a new entry that references
   the original by number (Entry 003). What is never permitted is rewriting
   what an earlier entry already said.
3. **Required fields per entry.** Date of discovery, observed period,
   observation (with numeric values), current status or entry type, and
   cross-check against existing frameworks (rule categories from this
   protocol, relevant zone classifications from the paper series, etc.).
4. **Status values.** For entries recording an observed pattern:
   `exploratory` (just observed), `re-validation pending` (promising but not
   yet rule-ified), `false positive confirmed` (follow-up disproved the
   signal), `promoted to vX.X` (incorporated into a new rules-document
   version). Entries that record the operation of the protocol rather than a
   market pattern — an implementation defect, a procedural failure, an
   investigation that found nothing — carry a `Type:` line instead of a
   status, since none of the four values applies to them. Inventing a fifth
   status value is not permitted; Entry 002 did so and Entry 003 corrects it.
5. **Not citable as a paper-claim source.** An entry cannot serve as evidence
   for a published claim. To make a claim, the pattern must first be
   pre-registered as a new rule in `tda_monitoring_rules.md` vX.X, and
   subsequent out-of-sample events must accumulate under that new rule.
6. **Commit message format.**
   `docs: add tda_events_log.md entry NNN (<date>, <short title>, <status or type>)`
7. **Signed commits.** Commits to `public/tda_events_log.md` are signed.
   Signing is via the GitHub web interface, so `git log --format='%G?'`
   reports `E` — the signature is GitHub's web-flow key, which the author
   cannot backdate, rather than a local key. Automated daily commits to the
   CSVs are unsigned (`N`) and are outside the scope of this clause.
   Commits made before this clause was being observed have **not** been
   rewritten to add signatures, because doing so would require a force-push.
8. **Force-push is never used.** The integrity evidence this protocol relies
   on is bound to specific commit hashes; rewriting history to correct a
   procedural lapse would destroy more than the lapse costs. Lapses are
   recorded instead.

### Scope of the log

The log's original purpose was exploratory market observations. It now also
carries records of the protocol's own operation: procedural failures (Entry
003), implementation defects (Entry 004), and investigations that found
nothing (Entry 005). That widening is deliberate. A record of the occasions
on which the discipline was tested is the point of keeping the log at all,
and an investigation that comes back empty belongs in it for the same reason
one that finds something does.

### Citing in derived papers

When a paper is written using events from this monitor, it must:

1. Cite the commit hash of `tda_monitoring_rules.md` corresponding to the
   version of rules in force when the event was detected.
2. Cite the paper(s) corresponding to the detection category.
3. If the paper analyzes features beyond the current detection rules, either
   declare the analysis as exploratory pending re-validation, or issue a new
   pre-registered protocol committed before the paper's data cutoff.
4. Do **not** cite entries in `public/tda_events_log.md` as evidence for paper
   claims. They may be cited only as evidence that the §7.2 discipline is
   being exercised.

## References

- Takagi, K. (2026a). "Topological structure changes in credit markets lead
  equity returns: Why the HYG TDA three-axis framework works." SSRN Working
  Paper, Abstract ID 6453878.
- Takagi, K. (2026c). "The Energy Landscape of Credit Markets: Chemical
  Potential as a Topological Measure of Financial Market Structure." SSRN
  Working Paper.
- Takagi, K. (2026). "Topological Pre-Signaling of Energy Shocks: Evidence
  from Brent Crude and VIX Persistent Homology." SSRN Working Paper.
- Gidea, M., & Katz, Y. (2018). "Topological data analysis of financial
  time series: Landscapes of crashes." Physica A 491, 820–834.

## License

Code is released under the MIT License; data files under `public/` are
released under CC BY 4.0. See `LICENSE`. For citation metadata, see
`CITATION.cff`.
