#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    ciphertext = ''
    for c in s:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            new_c = chr((ord(c) - base + k) % 26 + base)
            ciphertext += new_c
        else:
            ciphertext += c
            
    return ciphertext


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
