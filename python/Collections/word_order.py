from collections import Counter

n = int(input())

words = []
for _ in range(n):
    words.append(input())

c = Counter(words)
print(len(c))
for val in c.values():
    print(val, end=' ')