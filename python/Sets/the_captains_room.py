from collections import Counter
k = int(input())
rooms = list(map(int, input().split()))

c = Counter(rooms)

for room, room_count in c.items():
    if room_count != k:
        print(room)
        break