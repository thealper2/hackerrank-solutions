#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    freq = {}
    result = 0
    
    for num in a:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    for num in freq:
        l = freq[num] + freq.get(num + 1, 0)
        if l > result:
            result = l
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
