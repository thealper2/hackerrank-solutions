matrix1 = [
    [1, 2, 3],
    [2, 3, 4],
    [1, 1, 1]
]

matrix2 = [
    [4, 5, 6],
    [7, 8, 9],
    [4, 5, 7]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]   
]

for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
            
for i in range(3):
    for j in range(3):
        print(result[i][j])
