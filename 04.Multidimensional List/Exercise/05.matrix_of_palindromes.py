# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for row in range(97, rows + 97):
#     current_row = []
#     for col in range(cols):
#         first_letter = chr(row)
#         second_letter = chr(col + row)
#         last_letter = chr(row)
#         char = first_letter + second_letter + last_letter
#         current_row.append(char)
#     matrix.append(current_row)
#
# # [print(*matrix[row]) for row in range(rows)]
# [print(*row) for row in matrix]


rows, cols = [int(x) for x in input().split()]

for row in range(97, rows + 97):
    for col in range(cols):
        print(f"{chr(row)}{chr(col + row)}{chr(row)}", end=" ")

    print()