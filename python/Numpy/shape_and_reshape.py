import numpy as np

arr = input().strip().split(' ')
arr = np.array(arr, int)
print(np.reshape(arr, (3, 3)))