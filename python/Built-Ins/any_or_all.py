n = int(input())
arr = list(input().split())
print(all(int(i) > 0 for i in arr) and any(i == i[::-1] for i in arr))