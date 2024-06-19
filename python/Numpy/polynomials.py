import numpy as np

p = np.array(list(map(float, input().split())), dtype=float)
x = float(input())
print(np.polyval(p, x))