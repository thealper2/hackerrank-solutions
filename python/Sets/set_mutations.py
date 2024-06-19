n = int(input())
first_set = list(map(int, input().split()))
first_set = set(first_set)
number_of_sets = int(input())

for _ in range(number_of_sets):
    command = input().split()
    arr = set(map(int, input().split()))
    if command[0] == 'difference_update':
        first_set.difference_update(arr)
    elif command[0] == 'intersection_update':
        first_set.intersection_update(arr)
    elif command[0] == 'symmetric_difference_update':
        first_set.symmetric_difference_update(arr)
    elif command[0] == 'update':
        first_set.update(arr)

print(sum(first_set))