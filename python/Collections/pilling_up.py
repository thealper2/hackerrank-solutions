def can_stack_cubes(cube_lengths):
    left = 0
    right = len(cube_lengths) - 1
    last_picked = float('inf')
    
    while left <= right:
        if cube_lengths[left] >= cube_lengths[right]:
            current_pick = cube_lengths[left]
            left += 1
        else:
            current_pick = cube_lengths[right]
            right -= 1
        
        if current_pick > last_picked:
            return "No"
        
        last_picked = current_pick
    
    return "Yes"

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    result = can_stack_cubes(cubes)
    results.append(result)

for result in results:
    print(result)
