import numpy as np

n, m = list(map(int, input().split()))

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr, axis=None), 11))