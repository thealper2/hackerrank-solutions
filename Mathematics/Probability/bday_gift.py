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
# The function accepts INTEGER_ARRAY balls as parameter.
#

def solve(balls):
    return sum(balls) / 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    balls_count = int(input().strip())

    balls = []

    for _ in range(balls_count):
        balls_item = int(input().strip())
        balls.append(balls_item)

    result = solve(balls)

    fptr.write(str(result) + '\n')

    fptr.close()
