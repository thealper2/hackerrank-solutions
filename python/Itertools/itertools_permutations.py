from itertools import permutations

word, n = input().split()

perms = permutations(word, int(n))
for perm in sorted(perms):
    print(''.join([p for p in perm]))