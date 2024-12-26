import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

n_features, n_rows = map(int, input().split())

X, Y = [], []
for _ in range(n_rows):
    row = [0]
    items = list(map(float, input().split()))
    for i in range(len(items)):
        if i == n_features:
            Y.append(items[i])
        else:
            row.append(items[i])
    
    X.append(row)

X = np.array(X)
Y = np.array(Y)

poly = PolynomialFeatures(degree=n_features + 1)
X_poly = poly.fit_transform(X)

lr = LinearRegression()
lr.fit(X_poly, Y)

n_test_rows = int(input())
X_test = []
for _ in range(n_test_rows):
    row = [0]
    items = list(map(float, input().split()))
    for i in range(len(items)):
        row.append(items[i])

    X_test.append(row)

X_test = np.array(X_test)
X_test_poly = poly.fit_transform(X_test)
y_pred = lr.predict(X_test_poly)
for i in range(len(y_pred)):
    print(round(y_pred[i], 2))