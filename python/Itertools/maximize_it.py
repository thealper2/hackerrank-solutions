from itertools import product

n, mode = map(int, input().split())

groups = []
for _ in range(n):
    group = list(map(int, input().split()))
    groups.append(group[1:])

combs = product(*groups)

res = 0
for comb in combs:
    res = max(sum(x * x for x in comb) % mode, res)

print(res)