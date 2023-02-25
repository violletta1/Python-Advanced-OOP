

rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for x in range(rows)]

max_sum = float("-inf")
biggest_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        if sum(first_row + second_row + third_row) > max_sum:
            max_sum = sum(first_row + second_row + third_row)
            biggest_matrix = (first_row, second_row, third_row)

print(f"Sum = {max_sum}")

[print(*biggest_matrix[row]) for row in range(3)]



