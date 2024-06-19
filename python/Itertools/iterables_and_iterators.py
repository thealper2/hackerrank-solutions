from itertools import combinations

n = int(input())
arr = list(input().split())
k = int(input())

combs = list(combinations(arr, k))
print(round(len([comb for comb in combs if 'a' in comb]) / len(combs), 4))