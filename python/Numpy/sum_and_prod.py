import numpy as np

n, m = list(map(int, input().split()))

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


arr = np.array(arr)
s = np.sum(arr, axis=0)
print(np.prod(s, axis=None))