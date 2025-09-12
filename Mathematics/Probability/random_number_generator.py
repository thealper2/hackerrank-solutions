#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a, b, c):
    total = a * b
    result = None
    if c >= a + b:
        result = total
        
    elif c <= a and c <= b:
        result = 0.5 * c * c
        
    elif c <= a:
        result = 0.5 * (2 * c - b) * b
        
    elif c <= b:
        result = 0.5 * (2 * c - a) * a
        
    else:
        result = total - 0.5 * (a + b - c) ** 2
    
    num_int = int(result * 2)
    den_int = total * 2
    g = math.gcd(num_int, den_int)
    num_int //= g
    den_int //= g
    return f'{num_int}/{den_int}'        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()
