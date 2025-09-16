#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    unique_chars = set(s)
    max_length = 0
    
    for pair in combinations(unique_chars, 2):
        a, b = pair
        filtered = [c for c in s if c == a or c == b]
        valid = True
        for i in range(1, len(filtered)):
            if filtered[i] == filtered[i - 1]:
                valid = False
                break
                
        if valid:
            max_length = max(max_length, len(filtered))
            
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
