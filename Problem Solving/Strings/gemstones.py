#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    freq = defaultdict(int)
    n = len(arr)
    for word in arr:
        seen = set()
        for c in word:
            if c not in seen:
                freq[c] += 1
                seen.add(c)
                
    result = 0
    for k, v in freq.items():
        if v == n:
            result += 1
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
