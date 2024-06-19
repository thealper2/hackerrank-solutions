from itertools import combinations_with_replacement

word, n = input().split()

combs = combinations_with_replacement(sorted(word), int(n))
for comb in combs:
    print(''.join([c for c in comb]))