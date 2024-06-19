n, m = map(int, input().split())
data = list(map(int, input().split()))
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

score = 0

for i in data:
    if i in a:
        score += 1

for i in data:
    if i in b:
        score -= 1

print(score)