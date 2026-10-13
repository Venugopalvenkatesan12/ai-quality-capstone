name = 'Login Test'
status = 'fail'
duration_ms = 1500

print(f'Test Name: {name}, Status: {status} in Duration: {duration_ms} ms')

if status == 'pass':
    print('OK')
elif status == 'fail':
    print('Needs attention')
else:
    print('Skipped')


tests = ["login", "logout", "signup", "reset password"]
for test in tests:
    print(f'Running test: {test.upper()}')

for i, test in enumerate(tests, start=1):
    print (i, test)

retries = 0
while(retries < 3):
    print(f'Retrying test, attempt {retries + 1}')
    retries += 1