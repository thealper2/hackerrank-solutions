#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    result = []
    for n in range(p, q + 1):
        d = len(str(n))
        sq = str(n ** 2)
        r = int(sq[-d:]) if sq[-d:] else 0
        l = int(sq[:-d]) if sq[:-d] else 0
        if l + r == n:
            result.append(n)
            
    if result:
        print(' '.join(map(str, result)))
    else:
        print('INVALID RANGE')
        
            
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
