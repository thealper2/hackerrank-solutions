#!/bin/python3

import math
import os
import random
import re
import sys

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    timeCharged = float(input().strip())
    X, Y = [], []
    with open("trainingdata.txt", "r") as f:
        for line in f:
            x, y = line.strip().split(",")
            X.append(float(x))
            Y.append(float(y.strip()))
          
    #plt.scatter(X, Y)      
    
    X_new, Y_new = [], []
    for i in range(len(X)):
        if X[i] < 4:
            X_new.append(X[i])
            Y_new.append(Y[i])

    X_new = np.array(X_new).reshape((-1, 1))
    Y_new = np.array(Y_new)
    
    lr = LinearRegression()
    lr.fit(X_new, Y_new)
    
    if timeCharged >= 4:
        y_pred = 8
        print(y_pred)
    else:
        y_pred = lr.predict([[timeCharged]])
        print(round(y_pred[0], 2))