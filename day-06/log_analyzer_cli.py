import argparse
import json
import sys

class LogChecker:
    def __init__(self, log_file, out_file, level_filter=None):
        self.log_file = log_file
        self.out_file = out_file
        self.level_filter = level_filter.upper() if level_filter else None
        self.lines = []

    def read_logs(self):
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            print(f"ERROR: {self.log_file} not found.", file=sys.stderr)
            raise SystemExit("Check the file name or path.")
        if not self.lines:
            print(f"ERROR: {self.log_file} is empty.", file=sys.stderr)
            raise SystemExit("Provide a log file with content.")

    def count_levels(self):
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for line in self.lines:
            if self.level_filter:
                if self.level_filter in line:
                    self.counts[self.level_filter] += 1
                continue
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
    def save_counts(self):
        with open(self.out_file, "w", encoding="utf-8") as f:
            json.dump(self.counts, f, indent=2)

    def log_summary(self):
        filter_text = self.level_filter if self.level_filter else "None"
        return (
            "Log Analysis Summary\n"
            "\n"
            f"File: {self.log_file}\n"
            f"Filter Level: {filter_text}\n"
            f"Total lines: {len(self.lines)}\n"
            f"INFO: {self.counts['INFO']}\n"
            f"WARNING: {self.counts['WARNING']}\n"
            f"ERROR: {self.counts['ERROR']}\n"
        )
    def run(self):
        self.read_logs()
        self.count_levels()
        summary = self.log_summary()
        print(summary)
        self.save_counts()

def build_parser():
    parser = argparse.ArgumentParser(description="CLI Log Checker for DevOps")
    parser.add_argument("--file", required=True, help="Log file path (required)")
    parser.add_argument("--out", default="output.json", help="Output JSON file path ")
    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter only one level ",
    )
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    checker = LogChecker(
        log_file=args.file,
        out_file=args.out,
        level_filter=args.level,
    )
    checker.run()
if __name__ == "__main__":
    main()
