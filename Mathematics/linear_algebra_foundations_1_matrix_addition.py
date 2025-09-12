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

result = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
        
    result.append(row)
    
for i in range(3):
    for j in range(3):
        print(result[i][j])
