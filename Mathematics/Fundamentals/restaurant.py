#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'restaurant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER b
#

def restaurant(l, b):
    if l == b:
        return 1
    
    else:
        return ((l * b) // pow(math.gcd(l, b), 2))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)
        print(result)