#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    # Write your code here
    high = max(coordinates, key=lambda x: x[1])
    low = min(coordinates, key=lambda x: x[1])
    left = min(coordinates, key=lambda x: x[0])
    right = max(coordinates, key=lambda x: x[0])

    pts = [low, high, left, right]
    maxdist = max( math.sqrt(pow((pts[i][0] - pts[j][0]), 2) +  pow((pts[i][1] - pts[j][1]), 2)) for i in range(4) for j in range(i+1, 4))
    return maxdist

if __name__ == '__main__':
    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)
    print(result)