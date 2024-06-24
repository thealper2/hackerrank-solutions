import re

N = int(input().strip())
pattern = r'^[789]\d{9}$'

for _ in range(N):
    number = input().strip()
    if re.match(pattern, number):
        print("YES")
    else:
        print("NO")
    
