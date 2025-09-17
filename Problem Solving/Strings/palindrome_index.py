#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
        
    n = len(s)
    l = 0
    r = n - 1
    
    while l < r:
        if s[l] != s[r]:
            w1 = s[:l] + s[l+1:]
            w2 = s[:r] + s[r+1:]
            if w1 == w1[::-1]:
                return l
            elif w2 == w2[::-1]:
                return r
                
        l += 1
        r -= 1
        
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
