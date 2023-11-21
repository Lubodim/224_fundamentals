row = int(input())
matrix = []
for i in range(row):
    column = [int(x) for x in input().split(', ')]
    matrix.append(column)

print(matrix)