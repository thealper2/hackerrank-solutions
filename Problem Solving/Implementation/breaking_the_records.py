#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_ = scores[0]
    max_ = scores[0]
    c_min = 0
    c_max = 0
    
    for score in scores[1:]:
        if score > max_:
            max_ = score
            c_max += 1
            
        elif score < min_:
            min_ = score
            c_min += 1
        
    return [c_max, c_min]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
