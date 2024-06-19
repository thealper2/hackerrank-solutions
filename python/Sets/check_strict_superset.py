arr = set(map(int, input().split()))
n = int(input())
strict_superset = True

for _ in range(n):
    sub = set(map(int, input().split()))
    if not arr.issuperset(sub):
        strict_superset = False

print(strict_superset)