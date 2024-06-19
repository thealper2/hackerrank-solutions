import re

n = int(input())

for _ in range(n):
    r = input()
    try:
        re.compile(r)
        print("True")
    except:
        print("False")
