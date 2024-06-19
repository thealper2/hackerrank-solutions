import numpy as np

n, m = list(map(int, input().split()))

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for _ in range(n):
    b.append(list(map(int, input().split())))


a = np.array(a)
b = np.array(b)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)