number = int(input())

matrix = []

for row in range(number):
    matrix.append([])
    for col in range(number):
        matrix[row].append(col + 1 + row * number)
print(*matrix, sep="\n")
flat_matrix = []
for row in range(len(matrix)):
    for col in range(number):
        flat_matrix.append(matrix[row][col])
print(flat_matrix)