n = int(input())
arr = list(map(int, input().split()))

import numpy as np
from scipy import stats

mean = np.mean(arr)
print(round(mean, 1))

median = np.median(arr)
print(round(median, 1))

mode = int(stats.mode(arr)[0])
print(round(mode, 1))

std_dev = np.std(arr)
print(round(std_dev, 1))

confidence_interval = 1.96 * (std_dev / (n ** 0.5))
min_confidence = mean - confidence_interval
max_confidence = mean + confidence_interval
print(round(min_confidence, 1), round(max_confidence, 1))