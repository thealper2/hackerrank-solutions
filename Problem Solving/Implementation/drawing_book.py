#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    if p == 0:
        return 1
        
    l, r = 0, n
    l_p = 0
    r_p = 0
    
    while l < r:
        if l < p:
            if l % 2 == 1:
                l_p += 1
            l += 1
    
        if r > p:
            if r % 2 == 0:
                r_p += 1
            r -= 1
        
    return min(l_p, r_p)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
