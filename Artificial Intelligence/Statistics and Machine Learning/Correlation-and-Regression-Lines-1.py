def calculate_correlation(X, Y):
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    var_X = sum((item - mean_X) ** 2 for item in X)
    var_Y = sum((item - mean_Y) ** 2 for item in Y)

    cov = 0
    for a, b in zip(X, Y):
        cov += (a - mean_X) * (b - mean_Y)
    
    std = (var_X * var_Y) ** 0.5
    correlation = cov / std
    return round(correlation, 3)


physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

output = calculate_correlation(physics, history)
print(output)