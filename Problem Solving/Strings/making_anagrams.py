#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    result = 0
    count_a = Counter(s1)
    count_b = Counter(s2)
    
    for k_a, v_a in count_a.items():
        if k_a in count_b:
            if v_a > count_b[k_a]:
                result += v_a - count_b[k_a]
        else:
            result += v_a
            
    for k_b, v_b in count_b.items():
        if k_b in count_a:
            if v_b > count_a[k_b]:
                result += v_b - count_a[k_b]
        else:
            result += v_b
            
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
