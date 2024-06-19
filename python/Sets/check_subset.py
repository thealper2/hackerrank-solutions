n = int(input())

for _ in range(n):
    m = int(input())
    s1 = set(map(int, input().split()))
    k = int(input())
    s2 = set(map(int, input().split()))
    print(s1.issubset(s2))