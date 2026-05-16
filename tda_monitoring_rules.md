# TDA Real-Time Monitoring Rules (v1.0)

**Author:** Keishi Takagi
**Companion implementation:** `monitor_tda.py` v1.2
**Repository:** `https://github.com/keishi-takagi/tda-monitoring`
**Pre-registration:** This document is pre-registered via its initial commit
to the public repository above. The commit history of this file constitutes
the registration record.

---

## 0. Purpose and Design Philosophy

This document defines the **pre-registered** detection rules and recorded
features for a real-time monitor of topological anomalies in financial
markets. The companion implementation (`monitor_tda.py`) computes all
features following the equations published in:

- Takagi (2026a), Paper #1, SSRN 6453878
- Takagi (2026c), Chemical Potential
- Takagi (2026), Energy TDA
- Gidea & Katz (2018), Physica A 491, 820-834

The monitor is designed to operate continuously and accumulate evidence for
subsequent papers in the series.

The design follows two principles:

1. **All recorded features must appear in a published or working paper of
   the author, or be widely used in the TDA × finance literature.** No
   feature is added speculatively.

2. **Detection is narrow.** Only a small set of paper-based rules trigger
   events. The recorded feature set is wider than the detection set; the
   gap is intentional and serves as a continuing observation record of
   features that prior papers tested and rejected.

---

## 1. Recorded Features

For each trading day and each TDA ticker (HYG, VIX), the following features
are computed and recorded in `daily_features.csv`. All receive a 252-day
rolling z-score (column suffix `_z`).

### 1.1 TDA features — paper-adopted

| Column | Definition | Reference |
|---|---|---|
| `cnt` | Number of finite H1 generators in W=20 PD | Paper #1 |
| `dcnt` | cnt(W=20) − cnt(W=60) | Energy TDA |
| `ent` | Shannon entropy of H1 persistence distribution | Paper #1, Chem Pot |
| `euler` | β₀(ε=0.5) − β₁(ε=0.5) at ε=0.5 in W=20 PD | Chem Pot §3.2 |
| `chem` | Mean birth-death midpoint of finite H1 generators in W=20 PD | Chem Pot Definition 1 |
| `dchem` | chem(W=20) − chem(W=60) | Chem Pot §3.2 |
| `corr` | Mean persistence of top-3 H1 generators in W=20 PD | Chem Pot §3.2 |
| `wasserstein` | Wasserstein-2 distance between today's and yesterday's H1 PDs | Gidea & Katz 2018 |
| `bottleneck` | Bottleneck distance between today's and yesterday's H1 PDs | Gidea & Katz 2018 |

### 1.2 TDA features — paper-rejected, recorded for continued observation

These features appear in published papers explicitly tested and **rejected**
as predictive signals. They are recorded here for continued observation in
case future data alters the original conclusion. They do **not** trigger
any detection rule in this protocol.

| Column | Definition | Reference for rejection |
|---|---|---|
| `free_energy` | chem − ent | Chem Pot §4.3 (r=−0.938 with entropy) |
| `h1_mean_persistence` | Mean of (d − b) over finite H1 generators | Paper #1 §5.2 (count outperforms) |
| `h1_max_persistence` | Maximum of (d − b) over finite H1 generators | Paper #1 §5.2 (count outperforms) |
| `h1_total_persistence` | Sum of (d − b) over finite H1 generators | Paper #1 §5.2 (count outperforms) |

### 1.3 Classical control indicators

Recorded for the ticker(s) where each indicator applies. These provide a
non-TDA comparison set in eventual methodological papers.

| Column | Definition | Tickers |
|---|---|---|
| `rsi_14` | RSI 14-day | All price tickers |
| `bb_z_20` | Bollinger Band 20-day z-score | All price tickers |
| `sma_ratio_50_200` | SMA(50) / SMA(200) | All price tickers |
| `realized_vol_20d` | Annualized 20-day realized vol from log returns | All price tickers |
| `vix_level` | VIX close | Macro |
| `vix_sma10` | VIX SMA(10) | Macro |
| `brent_yoy` | Brent 252-day return | Macro |

### 1.4 Recording auxiliary: feature_extremes.csv

A long-format CSV is also written, containing one row per (date, ticker,
feature) tuple where |z| ≥ 2.0. This is a convenience view of
`daily_features.csv` and contains no information not already in the wide
table.

---

## 2. Detection Rules — Main (Paper-based, severity 3)

Five rules. Each corresponds to a specific paper in the series.

### 2.1 A1: HHH cell activation

**Source:** Paper #8 (Compression-Release, in preparation)
**Framework:** cnt × ent × euler (Paper #1 framework)
**Trigger:** On day t and ticker ∈ {HYG, VIX}, all three of `cnt_z`,
`ent_z`, `euler_z` are simultaneously ≥ +1.0.

### 2.2 A2: HHH → HHL transition

**Source:** Paper #8 (Compression-Release, in preparation)
**Framework:** cnt × ent × euler
**Trigger:** On consecutive trading days, the Paper #1 cell for the same
ticker transitions from `HHH` to `HHL`.

### 2.3 B1: HLM cell activation (Chemical Potential)

**Source:** Takagi (2026c), Chemical Potential, best cell
**Framework:** chem × ent × euler
**Trigger:** On day t with ticker = HYG, `chem_z` ≥ +1.0 and `ent_z` ≤ −1.0
and −1.0 < `euler_z` < +1.0, AND `VIX_SMA10` ≥ 20.0.

### 2.4 C1: Topological Decoupling 3-condition

**Source:** Takagi (2026), Energy TDA
**Trigger:** On day t, all three conditions simultaneously hold:

- `brent_yoy` > 30%
- `vix_sma10` < 20.0
- `dcnt` (on VIX) < −12

### 2.5 D1: dcnt z-score spike

**Source:** Energy TDA / Paper #8 secondary
**Trigger:** On day t with ticker = VIX, |`dcnt_z`| ≥ 3.0.
Severity 2 for 3.0 ≤ |z| < 4.0, severity 3 for |z| ≥ 4.0.

---

## 3. Detection Rules — Classical Controls (severity 2)

Three rules. Non-TDA classical indicators, included for comparison purposes
under the same pre-registered framework.

### 3.1 F1: RSI 14-day extreme

**Trigger:** RSI(14) ≤ 30 (oversold) OR RSI(14) ≥ 70 (overbought), on any
price ticker.

### 3.2 F2: Bollinger Band breach (2σ)

**Trigger:** |bb_z_20| ≥ 2.0, on any price ticker.

### 3.3 G1: VIX above 30

**Trigger:** VIX close ≥ 30.0.

---

## 4. Forward-Return Tracking

Every detected event (severity ≥ 2) is logged to
`forward_returns_tracking.csv` with placeholder rows for horizons
{1, 5, 10, 15, 20} trading days. As target dates arrive, realized values
are computed on subsequent monitor runs.

For categories tied to specific papers, the published prediction interval
is the comparison target:

- C1 (Decoupling): mean VIX +10d ≈ +1.10, +20d ≈ +1.86 (95% CI [1.41, 2.31]);
  Takagi (2026, Energy TDA).
- B1 (HLM): mean QQQ 20d ≈ +4.82% (95% CI [+1.78%, +7.64%]);
  Takagi (2026c).
- A1, A2: Paper #8 prediction intervals will be added upon publication.

---

## 5. Data Sources

### 5.1 Tickers

| Ticker | Source | Role |
|---|---|---|
| HYG | yfinance | TDA computation (Paper #1, Chem Pot) |
| VIX (^VIX) | yfinance | TDA computation (Energy TDA), control input |
| SPY | yfinance | Predicted-asset, control |
| QQQ | yfinance | Predicted-asset (Paper #1, Chem Pot) |
| IWM | yfinance | Predicted-asset (size factor) |
| RSP | yfinance | Predicted-asset (equal weight) |
| VIX9D | yfinance | Control |
| TNX (^TNX) | yfinance | Control (10y Treasury proxy) |
| Brent | EIA (PET.RBRTE.D) | Macro (Energy TDA) |

### 5.2 Source policy

- Brent uses EIA series `PET.RBRTE.D` (Europe Brent Spot Price FOB),
  identical to the source in Takagi (2026, Energy TDA).
- Other tickers use yfinance.
- Source failures are logged in `run_metadata.json` but the monitor does
  **not** silently substitute alternative sources.

---

## 6. Computation Parameters (frozen)

Any change to these parameters requires a version bump and an entry in §8.

| Parameter | Value | Reference |
|---|---|---|
| Takens dimension d | 3 | Paper #1, Gidea & Katz 2018 |
| Takens delay τ | 3 | Paper #1, Gidea & Katz 2018 |
| Short window W_short | 20 | Paper #1 |
| Long window W_long | 60 | Energy TDA |
| Normalization | [0,1]^3 global min/max | Chem Pot §3.2 |
| Ripser maxdim | 1 | (H0, H1 only) |
| Euler ε | 0.5 | Chem Pot §3.2 |
| Euler formula | β0(ε) − β1(ε) | Chem Pot §3.2 |
| corr top-N | 3 | Chem Pot §3.2 |
| Z-score window | 252 trading days | Paper #1, Chem Pot |
| Z-score min observations | 30 | Paper #1, Chem Pot |
| Cell threshold low | z ≤ −1 | Paper #1 |
| Cell threshold high | z ≥ +1 | Paper #1 |
| Decoupling Brent YoY threshold | > 30% | Energy TDA |
| Decoupling VIX SMA10 threshold | < 20.0 | Energy TDA |
| Decoupling dcnt threshold | < −12 | Energy TDA |
| Brent YoY window | 252 trading days | Energy TDA |
| VIX SMA window | 10 trading days | Energy TDA |
| RSI window | 14 | classical |
| RSI extremes | ≤ 30, ≥ 70 | classical |
| Bollinger Band window | 20 | classical |
| Bollinger Band σ | 2.0 | classical |
| SMA short / long | 50 / 200 | classical |
| Realized vol window | 20 | classical |
| VIX fear level | ≥ 30.0 | classical |
| Feature-extreme z threshold | |z| ≥ 2.0 | this protocol |
| Forward-return horizons | {1, 5, 10, 15, 20} trading days | this protocol |

---

## 7. Post-hoc Analysis Discipline

Any analysis of recorded features beyond the rules in §§ 2-3 is permitted
as exploratory work. However:

1. **A paper claim derived from post-hoc analysis must be re-validated under
   a fresh pre-registered protocol** that fixes detection rules before
   observing future data.
2. Exploratory findings should be documented separately
   (e.g. `tda_events_log.md`) with the date of discovery, the data range
   analyzed, and an explicit statement that the finding is exploratory
   pending re-validation.
3. Adding new detection rules to this protocol requires a version bump
   (e.g. v1.0 → v1.1) and a commit. The commit hash establishes the
   pre-registration timestamp for the new rule.

---

## 8. Versioning and Change History

| Version | Date | Changes |
|---|---|---|
| v1.0 | (initial commit) | Initial pre-registration. Five main rules (A1, A2, B1, C1, D1), three control rules (F1, F2, G1). Recorded features: 9 paper-adopted TDA + 4 paper-rejected TDA + 7 classical control. |

Prior versions' rules continue to apply to in-flight analyses; new rules
apply from their version's commit date forward.

---

*End of pre-registration protocol.*
