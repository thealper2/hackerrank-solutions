from itertools import groupby

word = input().strip()

groups = []
keys = []

for k, g in groupby(word):
    groups.append(list(g))
    keys.append(k)

for k, g in zip(keys, groups):
    print((len(g), int(k)), end=' ')