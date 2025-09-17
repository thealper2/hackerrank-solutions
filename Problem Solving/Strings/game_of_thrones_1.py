#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    count = Counter(s)
    odd_count = 0
    for freq in count.values():
        if freq % 2:
            odd_count += 1
        
        if odd_count > 1:
            return 'NO'
            
    return 'YES'
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
