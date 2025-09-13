#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    t = arr.copy()
    min_ = min(t)
    t.remove(min_)
    max_sum = sum(t)
    max_ = max(t)
    t.remove(max_)
    min_sum = sum(t) + min_
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
