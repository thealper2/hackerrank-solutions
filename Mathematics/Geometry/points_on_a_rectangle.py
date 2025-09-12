#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    xs = [coord[0] for coord in coordinates]
    ys = [coord[1] for coord in coordinates]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)  
    max_y = max(ys)

    valid = True
    for (x, y) in coordinates:
        if not ((x == min_x or x == max_x) and (min_y <= y <= max_y) or (y == min_y or y == max_y) and (min_x <= x <= max_x)):
            valid = False
            break
        
    if valid:
        return 'YES'
    else:
        return 'NO'    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        coordinates = []

        for _ in range(n):
            coordinates.append(list(map(int, input().rstrip().split())))

        result = solve(coordinates)

        fptr.write(result + '\n')

    fptr.close()
