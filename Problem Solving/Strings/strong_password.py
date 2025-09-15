#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    need_digit = True
    need_lower = True
    need_upper = True
    need_special = True

    for ch in password:
        if ch in numbers:
            need_digit = False
        elif ch in lower_case:
            need_lower = False
        elif ch in upper_case:
            need_upper = False
        elif ch in special_characters:
            need_special = False

    missing = sum([need_digit, need_lower, need_upper, need_special])
    return max(missing, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

