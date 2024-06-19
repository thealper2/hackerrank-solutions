import numpy as np

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(float, input().split())))

arr = np.array(arr)
print(round(np.linalg.det(arr), 2))