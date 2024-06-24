import re
from email.utils import parseaddr

N = int(input().strip())

for _ in range(N):
    email = input()
    email = parseaddr(email)[1].strip()
    pattern = r'(^[A-Za-z][A-Za-z0-9\._-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$'
    if re.match(pattern, email):
        print(email)
