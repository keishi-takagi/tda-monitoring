#!/usr/bin/env python3
"""
verify_history.py — public/events_log.csv の歴史部分が全コミットで不変かを検査する。

リポジトリのルート（~/monitor_tda）で実行:

    python3 verify_history.py | tee verify_history_output.txt

検査内容:
  1. public/events_log.csv に触れた全コミットを取得
  2. 各コミット時点のファイルから CUTOFF より前の日付の行を抽出
  3. その部分の SHA-256 を計算し、全コミットで一致するかを確認
  4. あわせて行数・列構成・行順序も記録

「初回 vs 最新」の2点比較では、途中で変更して元に戻した場合を検出できない。
全コミットを見ることでその経路を塞ぐ。
"""

import hashlib
import io
import subprocess
import sys

import pandas as pd

PATH = "public/events_log.csv"
CUTOFF = "2026-05-15"   # 初回モニター実行日。これより前 = 事前登録時点で確定していた歴史部分


def sh(args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def main():
    log = sh(["git", "log", "--format=%H %ad", "--date=short", "--", PATH]).strip().splitlines()
    commits = [line.split(None, 1) for line in log]
    commits.reverse()   # 古い順
    print(f"{PATH} に触れたコミット: {len(commits)} 件")
    print(f"カットオフ: {CUTOFF} より前の日付を持つ行を歴史部分とする\n")

    results = []
    for sha, date in commits:
        try:
            blob = sh(["git", "show", f"{sha}:{PATH}"])
        except subprocess.CalledProcessError:
            print(f"  {date} {sha[:8]}  <ファイル無し>")
            continue

        df = pd.read_csv(io.StringIO(blob), parse_dates=["date"])
        hist = df[df.date < CUTOFF]

        # 正規化せず、読み込んだ順序のまま CSV 化してハッシュ。
        # 行順序の変化も検出対象に含める。
        payload = hist.to_csv(index=False).encode("utf-8")
        digest = hashlib.sha256(payload).hexdigest()

        results.append({
            "sha": sha,
            "date": date,
            "n_total": len(df),
            "n_hist": len(hist),
            "cols": ",".join(df.columns),
            "sha256_hist": digest,
        })

    r = pd.DataFrame(results)

    print("=== 歴史部分のハッシュ ===")
    uniq = r.sha256_hist.unique()
    print(f"異なるハッシュの種類: {len(uniq)}")
    if len(uniq) == 1:
        print(f"  全 {len(r)} コミットで一致: {uniq[0]}")
    else:
        for u in uniq:
            sub = r[r.sha256_hist == u]
            print(f"  {u[:16]}...  {len(sub)} 件  {sub.date.min()} 〜 {sub.date.max()}")

    print("\n=== 行数 ===")
    print(f"歴史部分の行数の種類: {sorted(r.n_hist.unique())}")
    print(f"全体行数: {r.n_total.iloc[0]} → {r.n_total.iloc[-1]}  単調増加: {r.n_total.is_monotonic_increasing}")

    print("\n=== 列構成 ===")
    for c in r.cols.unique():
        print(f"  {c}")

    print("\n=== 判定 ===")
    ok_hash = len(uniq) == 1
    ok_rows = r.n_hist.nunique() == 1
    ok_cols = r.cols.nunique() == 1
    ok_mono = bool(r.n_total.is_monotonic_increasing)
    for label, ok in [("歴史部分のハッシュ不変", ok_hash),
                      ("歴史部分の行数不変", ok_rows),
                      ("列構成不変", ok_cols),
                      ("全体行数が単調増加", ok_mono)]:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")

    print("\n" + ("IDENTICAL — 全コミットで歴史部分が不変"
                  if all([ok_hash, ok_rows, ok_cols, ok_mono])
                  else "DIFFER — 下の表を確認すること"))

    if not all([ok_hash, ok_rows, ok_cols, ok_mono]):
        print()
        print(r[["date", "sha", "n_total", "n_hist"]].to_string(index=False))

    r.to_csv("verify_history_detail.csv", index=False)
    print("\n詳細を verify_history_detail.csv に出力しました。")
    return 0 if all([ok_hash, ok_rows, ok_cols, ok_mono]) else 1


if __name__ == "__main__":
    sys.exit(main())
