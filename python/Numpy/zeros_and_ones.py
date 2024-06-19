import numpy as np

arr = list(map(int, input().split()))

arr1 = np.zeros(tuple((arr)), dtype=np.int_)
arr2 = np.ones(tuple((arr)), dtype=np.int_)
print(arr1)
print(arr2)