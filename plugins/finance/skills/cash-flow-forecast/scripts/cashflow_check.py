#!/usr/bin/env python3
"""Check a simple weekly cash CSV. Local arithmetic only.

CSV columns: week,inflow,outflow
Optional first data dependency: pass opening cash with --opening.
No network. No credentials. Numbers you do not supply are not invented.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys


def money(value):
    text = value.strip().replace(",", "")
    if text == "":
        raise ValueError("blank amount")
    return round(float(text), 2)


def main():
    parser = argparse.ArgumentParser(description="Roll a weekly cash CSV forward.")
    parser.add_argument("csv_path", help="CSV with week,inflow,outflow")
    parser.add_argument("--opening", required=True, type=float, help="Opening cash")
    parser.add_argument("--buffer", type=float, default=0.0, help="Minimum closing cash")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()
    rows = []
    balance = round(args.opening, 2)
    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"week", "inflow", "outflow"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            print("CSV must include week,inflow,outflow", file=sys.stderr)
            return 2
        for raw in reader:
            inflow = money(raw["inflow"])
            outflow = money(raw["outflow"])
            balance = round(balance + inflow - outflow, 2)
            rows.append(
                {
                    "week": raw["week"].strip(),
                    "inflow": inflow,
                    "outflow": outflow,
                    "closing": balance,
                    "below_buffer": balance < args.buffer,
                }
            )
    breaches = [row["week"] for row in rows if row["below_buffer"]]
    result = {"opening": round(args.opening, 2), "buffer": args.buffer, "weeks": rows, "first_breach": breaches[0] if breaches else None}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for row in rows:
            flag = " BREACH" if row["below_buffer"] else ""
            print(f"{row['week']}: close {row['closing']:.2f}{flag}")
        if result["first_breach"]:
            print(f"First week under buffer: {result['first_breach']}")
        else:
            print("No week closes under the buffer.")
    return 1 if breaches else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)
