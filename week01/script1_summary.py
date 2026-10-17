import json
from collections import Counter

#Loads the file with json.load (use with open(...) as f:)
with open("week01/results.json") as f:
	file_loaded = json.load(f)

#Counts pass, fail and skipped using a dict
#Treats a missing status as "unknown" (hint: entry.get("status", "unknown"))
# counts = {}
# for entry in file_loaded:
#     status = entry.get("status", "unknown")
#     counts[status] = counts.get(status, 0) + 1
# print(f'Counts: {counts}')

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