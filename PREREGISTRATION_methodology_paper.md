# Pre-registration: Methodology paper

**Version:** v1.0
**Committed:** (establishes the timestamp for this document)
**Author:** Keishi Takagi
**Repository:** https://github.com/keishi-takagi/tda-monitoring
**Status:** the paper is not written. This document fixes what it will report,
before the material it will report on has accumulated.

---

## 1. Why this document exists

The planned paper is about pre-registration discipline in TDA-based market
analysis. A paper making that argument, which was not itself pre-registered,
invites the obvious objection. This document removes it.

It commits to what will be reported, and to reporting it regardless of how it
turns out, at a point when the outcome is not yet known.

## 2. Planned paper

A methodological paper on operating a pre-registered detection protocol for
topological anomalies in financial markets: how the protocol was specified,
what was fixed in advance, what the implementation got wrong, and what the
record shows. Target timeframe: late 2027. Nothing here commits to a
publication date, a venue, or an outcome.

## 3. What the paper will report, unconditionally

The following will appear in the paper whether or not they favour the
protocol, the detection rules, or the author.

1. **Every severity-3 event** recorded in `public/events_log.csv` from the
   pre-registration commit (`2df4af0d`, 2026-05-16) to the paper's data
   cutoff. Not a selected subset, not a subset chosen by category.
2. **Every comparison against a published prediction interval** that the data
   permits — currently the C1 interval (VIX +20d, +1.86, 95% CI [1.41, 2.31])
   and the B1 interval (QQQ 20d, +4.82%, CI [+1.78%, +7.64%]) — including
   comparisons in which the realized outcome falls outside the interval, and
   including the direction of any discrepancy.
3. **Every entry in `public/tda_events_log.md`**, including entries that
   record the author's own procedural failures and implementation defects.
4. **The complete version history** of both `tda_monitoring_rules.md` and
   `monitor_tda.py`, with the reason for each change and whether it altered
   detection behaviour.
5. **Rules that produced no out-of-sample events at all.** Silence is a
   result. As of this document, B1, A2 and D1 have not fired out of sample.
6. **The sample-size problem**, stated plainly rather than in a limitations
   paragraph: detections cluster into episodes, overlapping forward-return
   windows mean the effective sample is the episode count rather than the day
   count, and the pre-registration-era record is unlikely to support a
   powered test of any rule by the target timeframe.

## 4. What the paper will not claim

1. **No out-of-sample validation claim** unless the accumulated episode count
   supports one on its own terms. The expected outcome is that it will not,
   and the paper is expected to say so.
2. **No use of the 1987–present backfill as validation.** The detection rules
   were derived from that history; event counts over it are in-sample by
   construction and will be presented as such.
3. **No claim that the implementation is proven unmodified.** What is
   demonstrable is stated as fact and left to the reader: that a change to the
   detection logic would necessarily alter the historical rows of
   `public/events_log.csv`, that those rows are byte-identical across every
   commit, and that the released code reproduces the published CSVs. The
   remaining dependencies — on GitHub's push record as a third-party witness,
   and on the fact that non-public intermediate features are only partially
   constrained by the public outputs — will be stated rather than elided.
4. **No claim derived from a pattern first observed after the fact.** In
   particular, the threshold and construction observations recorded in
   `tda_events_log.md` Entries 002 and 005 were identified after seeing the
   data they describe. They may be reported as records of decisions taken;
   they may not be used to support a claim about market behaviour without a
   fresh pre-registration motivated by an independent episode.

## 5. Analyses that are exploratory by declaration

Anything not enumerated in §3 is exploratory and will be labelled as such
in the paper. This includes any subgroup analysis, any alternative horizon,
any alternative outcome ticker, and any construction-sensitivity analysis of
the existing rules.

## 6. Data cutoff

The paper's data cutoff will be stated explicitly and will be a date, not an
event. It will not be chosen after inspecting the outcomes near it. Once the
cutoff is fixed it will be recorded here as an amendment with its own commit.

## 7. Amendments

This document may be amended. Every amendment will be a new commit that
leaves the prior text visible in the git history, with the reason for the
change stated. Amendments that narrow §3 or widen §4 — that is, that reduce
what is promised — will be flagged as such in the paper itself.

## 8. Relationship to `tda_monitoring_rules.md`

This document governs the reporting of a paper. It has no authority over the
detection protocol, does not modify any rule, and does not change the rules
version. `tda_monitoring_rules.md` remains v1.0.
