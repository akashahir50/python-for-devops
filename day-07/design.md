# Log Checker Script

## What problem am I solving?
-DevOps engineers need quick counts of INFO/WARNING/ERROR levels from large log files during incidents.

-Auto-counting all three log levels.

-Saving JSON output.

-Handling missing files.

## What input does my script need?
- --file : Path to log file
- --out  : Output JSON file
- --level : Filter one level INFO/WARNING/ERROR

## What output should it give?
- **Terminal Output:** Log level counts + total lines
- **Output file:** Counts in JSON format
- **If --level provided:** Only selected level count

## What are the main steps?
- Parse command line arguments using argparse
- Initialize LogChecker class with file paths and filter level
- Read log file into memory and validate existence/content
- Process each line to count INFO/WARNING/ERROR occurrences
- Generate and display formatted console summary
- Write log level counts to JSON output file
