n = int(input())

matrix = []

for row in range(n):
    matrix.append(list(input()))

symbol = input()
position = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = (row, col)
            break
    if position:
        break

# print(position if position else f"{symbol} does not occur in the matrix")

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")


#2222222222222222222
# def read_matrix_func():
#     number_of_rows = int(input())
#     current_matrix = []
#
#     for row in range(number_of_rows):
#         row_data = list(input())
#         current_matrix.append(row_data)
#
#     return current_matrix
#
#
# def check_func_for_special_symbol(matrix, symbol):
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             current_element = matrix[row][col]
#             if current_element == symbol:
#                 return row, col
#
#
# def print_func(data, symbol):
#     if data:
#         print(data)
#     else:
#         print(f'{symbol} does not occur in the matrix')
#
#
# matrix = read_matrix_func()
# special_symbol = input()
# print_func(check_func_for_special_symbol(matrix, special_symbol), special_symbol)