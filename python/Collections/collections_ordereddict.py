from collections import OrderedDict

n = int(input())

items = OrderedDict()


for _ in range(n):
    word = input()
    val = int(word.split()[-1])
    item = ' '.join(word.split()[:-1])
    if item not in items:
        items[item] = val
    else:
        items[item] = items[item] + val


for item in items:
    print(f'{item} {items[item]}')