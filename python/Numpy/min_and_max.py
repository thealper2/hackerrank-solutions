import numpy as np

n, m = list(map(int, input().split()))

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
print(np.max(np.min(arr, axis=1)))