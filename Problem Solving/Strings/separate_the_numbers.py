#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    for length in range(1, n // 2 + 1):
        first_num = s[:length]
        if first_num[0] == '0':
            continue
            
        num = int(first_num)
        current = num
        index = length
        valid = True
        
        while index < n:
            next_num = current + 1
            next_str = str(next_num)
            if s.startswith(next_str, index):
                index += len(next_str)
                current = next_num
            else:
                valid = False
                break
                
        if valid and index == n:
            print(f"YES {first_num}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
