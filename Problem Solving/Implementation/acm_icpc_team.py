#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    n = len(topic)
    max_topic = 0
    max_topic_count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            a = topic[i]
            b = topic[j]
            topic_count = 0
            for a_, b_ in zip(a, b):
                if int(a_) + int(b_) >= 1:
                    topic_count += 1
            
            if topic_count > max_topic:
                max_topic = topic_count
                max_topic_count = 1
            elif topic_count == max_topic:
                max_topic_count += 1
                
    return [max_topic, max_topic_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
