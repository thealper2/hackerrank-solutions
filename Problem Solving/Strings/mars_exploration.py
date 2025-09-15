#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    diff = 0
    n = len(s)
    a = n // 3
    b = n % 3
    original = 'SOS' * a + 'SOS'[:b]
    for s_c, original_c in zip(s, original):
        if s_c != original_c:
            diff += 1
            
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
