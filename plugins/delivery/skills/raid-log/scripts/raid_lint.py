#!/usr/bin/env python3
"""Lint a RAID CSV for missing owners and dates. Local file only.

Columns: type,item,owner,date,status
type is risk, assumption, issue, or dependency.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys

TYPES = {"risk", "assumption", "issue", "dependency"}


def main():
    parser = argparse.ArgumentParser(description="Lint a RAID log CSV.")
    parser.add_argument("csv_path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    findings = []
    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"type", "item", "owner", "date", "status"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            print("CSV must include type,item,owner,date,status", file=sys.stderr)
            return 2
        for index, raw in enumerate(reader, start=2):
            kind = raw["type"].strip().lower()
            if kind not in TYPES:
                findings.append({"line": index, "issue": "type must be risk, assumption, issue, or dependency"})
            if not raw["owner"].strip():
                findings.append({"line": index, "issue": "missing owner"})
            if raw["status"].strip().lower() != "closed" and not raw["date"].strip():
                findings.append({"line": index, "issue": "open item missing date"})
    if args.json:
        print(json.dumps({"findings": findings}, indent=2))
    elif findings:
        for finding in findings:
            print(f"line {finding['line']}: {finding['issue']}")
    else:
        print("RAID log has owners and dates on open items.")
    return 1 if findings else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)
