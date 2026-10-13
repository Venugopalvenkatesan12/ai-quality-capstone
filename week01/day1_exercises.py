suites = ['Smoke', 'Regression', 'Sanity', 'Performance', 'Security', 'Usability']

for i, suite in enumerate(suites, start=1):
    print(f'Suite {i}: {suite}')

durations = [120, 450, 80, 2300, 640]
total_duration = sum(durations)
print(f'Total duration: {total_duration} ms')
print(f'Average duration: {total_duration / len(durations):.2f} ms')
print(f'Slowest duration: {max(durations)} ms')

for duration in durations:
    label = 'SLOW' if duration > 1000 else 'OK'
    print(f'{duration} ms - {label}')

input_str = "  Login_Test_Failed  "
print(input_str.strip().lower().replace('_', ' '))

tests = ["login test", "logout", "signup", "reset password", "login with invalid credentials"]
count = sum(1 for test in tests if 'login' in test)
print(f'Number of tests containing "login": {count}')