import json
import sys
from pathlib import Path

from Rift_Sentinel.analyzer import analyze_matches
from Rift_Sentinel.report import build_report


def load_matches(file_path):
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        matches = json.load(file)

    return matches


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 -m Rift_Sentinel.main data/matches.json")
        return

    file_path = sys.argv[1]

    try:
        matches = load_matches(file_path)
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        return

    analysis = analyze_matches(matches)
    report = build_report(analysis)

    print(report)

if __name__ == "__main__":
    main()
