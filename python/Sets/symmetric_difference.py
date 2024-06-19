a_size = map(int, input())
a = set(map(int, input().split()))
b_size = map(int, input())
b = set(map(int, input().split()))

for i in sorted(a.difference(b).union(b.difference(a))):
    print(i)
