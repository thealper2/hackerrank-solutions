n = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1]
arr = set(arr)
n_of_commands = int(input())

for _ in range(n_of_commands):
    command = input().split()
    if command[0] == 'pop':
        arr.pop()
    elif command[0] == 'remove':
        arr.remove(int(command[1]))
    elif command[0] == 'discard':
        arr.discard(int(command[1]))

print(sum(arr))