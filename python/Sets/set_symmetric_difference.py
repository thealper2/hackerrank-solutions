n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

print(len(a.symmetric_difference(b)))