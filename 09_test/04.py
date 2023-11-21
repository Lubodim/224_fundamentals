num = 5
matrix = []
for i in range(num):
    matrix.append([])
    for j in range(num):
        matrix[i].append(j + i)
print(matrix)
