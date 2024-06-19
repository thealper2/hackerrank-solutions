n, x = map(int, input().split())

arrays = []
for _ in range(x):
    array = list(map(float, input().split()))
    arrays.append(array)

zipped = zip(*arrays)
for zip in zipped:
    avg = sum(zip) / x
    print(round(avg, 1))