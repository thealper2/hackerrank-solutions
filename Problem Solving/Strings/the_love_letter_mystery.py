#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        a, b = s[:mid], s[mid+1:][::-1]
    else:
        a, b = s[:mid], s[mid:][::-1]

    result = 0
    for i, j in zip(a, b):
        if i != j:
            ord_i = ord(i) - ord('a') + 1
            ord_j = ord(j) - ord('a') + 1
            result += abs(ord_i - ord_j)

    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
