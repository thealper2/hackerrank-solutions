#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    n = min(steps, len(path))
    result = 0
    valley = 0
    is_down = False
    for i in range(n):
        if path[i] == 'U':
            valley += 1
        else:
            valley -= 1
            
        if valley < 0:
            is_down = True
        
        if valley == 0 and is_down:
            result += 1
            is_down = False
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
