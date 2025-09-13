#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    negative_rate = 0.0
    positive_rate = 0.0
    zero_rate = 0.0
    for item in arr:
        if item < 0:
            negative_rate += 1 / n
        elif item == 0:
            zero_rate += 1 / n
        elif item > 0:
            positive_rate += 1 / n
            
    print(round(positive_rate, 6))
    print(round(negative_rate, 6))
    print(round(zero_rate, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
