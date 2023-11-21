matrix = []

row = 4

for i in range(row):
    matrix.append([])
    for j in range(row):
       matrix[i].append(i + j)
print(*matrix, sep="\n")