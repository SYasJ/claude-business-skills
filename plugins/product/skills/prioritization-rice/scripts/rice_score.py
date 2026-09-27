#!/usr/bin/env python3
"""Score RICE items from a local CSV. Does not invent reach or confidence.

Columns: item,reach,impact,confidence,effort
confidence is 0 to 1. effort must be greater than zero.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys


def main():
    parser = argparse.ArgumentParser(description="Compute RICE scores from a CSV you supply.")
    parser.add_argument("csv_path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    scored = []
    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"item", "reach", "impact", "confidence", "effort"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            print("CSV must include item,reach,impact,confidence,effort", file=sys.stderr)
            return 2
        for raw in reader:
            reach = float(raw["reach"])
            impact = float(raw["impact"])
            confidence = float(raw["confidence"])
            effort = float(raw["effort"])
            if effort <= 0 or not 0 <= confidence <= 1:
                print(f"invalid row: {raw['item']}", file=sys.stderr)
                return 2
            score = round((reach * impact * confidence) / effort, 2)
            scored.append({"item": raw["item"].strip(), "score": score, "confidence": confidence})
    scored.sort(key=lambda item: item["score"], reverse=True)
    if args.json:
        print(json.dumps(scored, indent=2))
    else:
        for item in scored:
            print(f"{item['score']:8.2f}  {item['item']}  (confidence {item['confidence']})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)
