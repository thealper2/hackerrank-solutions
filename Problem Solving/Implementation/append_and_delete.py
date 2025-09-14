#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    n = len(s)
    m = len(t)
    common = 0
    
    for i in range(min(n, m)):
        if s[i] == t[i]:
            common += 1
        else:
            break
        
    total_ops = (n - common) + (m - common)
    if k >= n + m:
        return 'Yes'
    elif total_ops <= k and (k - total_ops) % 2 == 0:
        return 'Yes'
    else:
        return 'No'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
