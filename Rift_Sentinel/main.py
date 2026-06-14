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
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "data/matches.json"

    matches = load_matches(file_path)
    analysis = analyze_matches(matches)
    report = build_report(analysis)

    print(report)


if __name__ == "__main__":
    main()
