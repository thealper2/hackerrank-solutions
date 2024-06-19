from itertools import combinations

word, n = input().split()


for i in range(int(n)):
    combs = combinations(sorted(word), i+1)
    for comb in combs:
        print(''.join([c for c in comb]))