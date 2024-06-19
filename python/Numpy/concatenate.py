import numpy as np

n, m, p = list(map(int, input().split()))

arr = []
for _ in range(n + m):
    i = list(map(int, input().split()))
    arr.append(i)

arr = np.array(arr).reshape(n+m, p)
print(arr)