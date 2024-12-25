def calculate_prob(X, Y):
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    var_X = sum((item - mean_X) ** 2 for item in X)

    cov = 0
    for a, b in zip(X, Y):
        cov += (a - mean_X) * (b - mean_Y)
    
    slope = cov / var_X
    a = mean_Y - slope * mean_X
    result = slope * 10 + a
    return round(result, 1)

physics = [15.0, 12.0, 8.0, 8.0, 7.0, 7.0, 7.0, 6.0, 5.0, 3.0]
history = [10.0, 25.0, 17.0, 11.0, 13.0, 17.0, 20.0, 13.0, 9.0, 15.0]

output = calculate_prob(physics, history)
print(output)