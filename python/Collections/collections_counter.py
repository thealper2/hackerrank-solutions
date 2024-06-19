x = int(input())
shop = list(map(int, input().split()))
n = int(input())

sells = 0
for _ in range(n):
    size, amount = list(map(int, input().split()))
    if size in shop:
        sells = sells + amount
        shop.remove(size)

print(sells)