# TDA Real-Time Monitoring

Pre-registered real-time monitoring of topological anomalies in financial
markets. Companion to the Takagi (2026) TDA paper series.

## Public release schedule

This repository is divided into a **pre-registration phase** and a
**reproduction-code release phase**:

- **Now (pre-registration phase)**:
  - `tda_monitoring_rules.md` — pre-registered detection rules
  - `public/*.csv` — accumulated event and tracking data (updated regularly)
- **Upon publication of the companion methodological paper**:
  - `monitor_tda.py` — the public reproduction code

Pre-registration is established by the commit history of
`tda_monitoring_rules.md` and the running record of `public/*.csv`. The
reproduction code is held back until the companion paper is published, at
which point this repository will include the full reproducible pipeline.

## Detection categories (from `tda_monitoring_rules.md`)

### Main (TDA, paper-based)

| Category | Detection | Reference paper |
|---|---|---|
| A1 | HHH cell activation | Paper #8 (Compression-Release) |
| A2 | HHH → HHL transition | Paper #8 (Compression-Release) |
| B1 | HLM cell activation | Chemical Potential (Takagi 2026c) |
| C1 | Decoupling 3-condition fire | Energy TDA (Takagi 2026 Energy) |
| D1 | dcnt z-score spike | Energy TDA / Paper #8 secondary |

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
| `public/events_log.csv` | One row per detected event (date, category, ticker, severity, details). Accumulates over time. |
| `public/decoupling_status.csv` | Per-day Energy TDA 3-condition status (Brent YoY, VIX SMA10, Δcnt). |
| `public/forward_returns_tracking.csv` | Forward-return tracking for each detected event at horizons {1, 5, 10, 15, 20} trading days. |

The git history of these files serves as the running timestamp record:
each commit records the state of detection at that point in time. Anyone
can verify when a given event first appeared in the log via
`git blame public/events_log.csv`.

## Pre-registration

The detection rules in `tda_monitoring_rules.md` are pre-registered as of
the initial commit of this repository. Any subsequent change is recorded
as an explicit version bump (e.g. v1.0 → v1.1) with a commit. The git
history establishes the timestamp.

### Citing in derived papers

When a paper is written using events from this monitor, it must:

1. Cite the commit hash of `tda_monitoring_rules.md` corresponding to
   the version of rules in force when the event was detected.
2. Cite the paper(s) corresponding to the detection category.
3. If the paper analyzes features beyond the current detection rules,
   either declare the analysis as exploratory pending re-validation, or
   issue a new pre-registered protocol committed before the paper's
   data cutoff.

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
