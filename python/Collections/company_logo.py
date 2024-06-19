import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    a = Counter(s)
    items = list(a.items())
    items.sort(key=lambda item: item[0])
    items.sort(key=lambda item: item[1], reverse=True)
    for item in items[:3]:
        print(item[0], item[1])