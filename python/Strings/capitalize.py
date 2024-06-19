import math
import os
import random
import re
import sys

def solve(s):
    sp = s.split(' ')
    return ' '.join([s.capitalize() for s in sp])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
