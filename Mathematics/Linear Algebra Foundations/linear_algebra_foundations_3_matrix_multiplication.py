matrix1 = [
    [1, 2],
    [2, 3]
]

matrix2 = [
    [4, 5],
    [7, 8]
]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = (matrix1[i][0] * matrix2[0][j]) + \
                       (matrix1[i][1] * matrix2[1][j])
                       
for i in range(2):
    for j in range(2):
        print(result[i][j])
