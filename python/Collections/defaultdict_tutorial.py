from collections import defaultdict

n_a, n_b = map(int, input().split())
a = defaultdict(list)

for i in range(n_a):
    k = input()
    a[k].append(str(i+1))

for i in range(n_b):
    k = input()
    if k in a:
        print(' '.join(a[k]))
    else:
        print(-1)