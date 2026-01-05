import json

class LogChecker:
    def __init__(self, log_file, out_file):
        self.log_file = log_file
        self.out_file = out_file

    def get_lines(self):
        with open(self.log_file) as f:
            return f.readlines()

    def count_levels(self, lines):
        counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for line in lines:
            if "INFO" in line:
                counts["INFO"] += 1
            elif "WARNING" in line:
                counts["WARNING"] += 1
            elif "ERROR" in line:
                counts["ERROR"] += 1
        return counts

    def save_counts(self, counts):
        with open(self.out_file, "w") as f:
            json.dump(counts, f)

if __name__ == "__main__":
    checker = LogChecker("app.log", "output.json")
    lines = checker.get_lines()
    counts = checker.count_levels(lines)
    checker.save_counts(counts)
    print(counts)
