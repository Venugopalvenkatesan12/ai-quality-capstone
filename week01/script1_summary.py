import json
from collections import Counter

#Loads the file with json.load (use with open(...) as f:)
with open("week01/results.json") as f:
    file_loaded = json.load(f)

counts = Counter(entry.get("status", "unknown") for entry in file_loaded)
print(f'Counts: {dict(counts)}')

#Prints the pass rate as a percentage
total = sum(counts.values())
pass_percentage = (counts.get("pass", 0) / total) * 100 if total else 0.0
print(f'Pass rate: {pass_percentage:.2f}%')

#Lists the failed test names with their errors
for entry in file_loaded:
    if entry.get("status") == "fail":
        print(f'Failed test: {entry.get("name", "Unknown Name")}, Error: {entry.get("error", "No error message")}')

names = Counter(e.get("name") for e in file_loaded)
print(f"Duplicate names: {[n for n, c in names.items() if c > 1]}")