#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    chars = [0 for _ in range(26)]
    for c in s.lower():
        if c.isalpha():
            ord_c = ord(c)
            idx = ord_c - ord('a')
            chars[idx] = 1
        
    return 'pangram' if sum(chars) == 26 else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
