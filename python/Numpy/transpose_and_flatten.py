import numpy as np

shape = list(map(int, input().split()))
arr = []

for _ in range(shape[0]):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
arr_t = np.array(arr).transpose()
print(arr_t)
print(arr.flatten())