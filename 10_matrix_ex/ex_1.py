number = int(input())

matrix = []

for row in range(number):
    matrix.append([])
    for col in range(number):
        matrix[row].append(col + 1 + row * number)


print(*matrix, sep="\n")
