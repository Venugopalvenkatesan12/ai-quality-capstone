# list
suites = ["Smoke", "Regression", "Sanity", "Performance", "Security", "Integration", "Functional", "End-to-End", "Acceptance", "Exploratory"]
print (f'Indexed: {suites[1]}, {suites[-1]}')
print (f'Forward Slicing: {suites[1:8]}')
print (f'Backward Slicing 1: {suites[8:2:-1]}')
print (f'Forward Slicing with step2: {suites[::2]}')
print (f'Backward Slicing with step2: {suites[::-2]}')

# list comprehension
durations = [1200, 1500, 1800, 2000, 2500, 2200, 1250, 3000, 650]
slow_suites = [ d for d in durations if d > 2000 ]
print (f'Slow suites: {slow_suites}')

# operations on collections
doubled_durations = [ d * 2 for d in durations ]
print (f'Doubled durations: {doubled_durations}')

dup_list = ["Smoke", "Regression", "Sanity", "Performance", "Security", "Integration", "Functional", "End-to-End", "Acceptance", "Exploratory", "Smoke", "Sanity", "Performance", "Functional", "End-to-End", "Acceptance"]

# dict (like Dictionary<string,int>)
counts = {}
for suite in dup_list:
    counts[suite] = counts.get(suite, 0) + 1
print (f'Counts: {counts}')

#dict comprehension
by_name = {f"test_{i}": d for i, d in enumerate(durations)}
print(f'By Name: {by_name}')

# Set
print (f'Unique items: {set(dup_list)}')

# tuple (immutable)
suites_tuple = ("Smoke", 1200) #packing
name, duration = suites_tuple #unpacking
print (f'Unpacking: Name: {name}, Duration: {duration}')