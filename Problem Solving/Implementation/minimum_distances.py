#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    n = len(a)
    min_dist = n
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                dist = abs(i - j)
                if dist < min_dist:
                    min_dist = dist
    
    if min_dist == n:
        return -1
    
    return min_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
