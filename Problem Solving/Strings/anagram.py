#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 == 1:
        return -1
        
    mid = len(s) // 2
    a, b = s[:mid], s[mid:]
    result = 0
    
    count_a = Counter(a)
    count_b = Counter(b)
    for k_a, v_a in count_a.items():
        if k_a in count_b:
            if v_a > count_b[k_a]:
                result += v_a - count_b[k_a]
        else:
            result += v_a    
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
