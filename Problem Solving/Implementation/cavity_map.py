#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    n = len(grid)
    grid = [list(row) for row in grid]
    
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            val = grid[i][j]
            if (val > grid[i - 1][j] and
                val > grid[i + 1][j] and
                val > grid[i][j - 1] and
                val > grid[i][j + 1]):
                grid[i][j] = 'X'
                
    return [''.join(row) for row in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
