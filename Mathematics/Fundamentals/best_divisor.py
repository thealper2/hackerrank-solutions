#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    digit_sum = lambda num: sum(int(d) for d in str(num))
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
            
    best = divisors[0]
    best_sum = digit_sum(best)
    
    for d in divisors[1:]:
        d_sum = digit_sum(d)
        if d_sum > best_sum:
            best = d
            best_sum = d_sum
        elif d_sum == best_sum:
            if d < best:
                best = d
                best_sum = d_sum
                
    print(best)
