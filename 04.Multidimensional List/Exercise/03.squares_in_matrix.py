rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for x in range(rows)]

equals_blocks = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        char = matrix[row][col]

        if char == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            equals_blocks += 1

print(equals_blocks)