rows, cols = [int(el) for el in input().split(", ")]


matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = 0
position = None

for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, -1):
        current_sum = matrix[row][col] + matrix[row][col-1] + matrix[row - 1][col] + matrix[row - 1][col-1]

        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position
print(matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row][col - 1], matrix[row][col])
print(max_sum)





#2222222222222222222222
# def read_matrix():
#     data = input().split(', ')
#     size = int(data[0])
#     matrix = []
#
#     for _ in range(size):
#         row_data = list(map(int, input().split(', ')))
#         matrix.append(row_data)
#
#     return matrix
#
#
# def submatrix_sum_func(matrix, row_index, column_index, matrix_size):
#     total_sum = 0
#     for row in range(row_index, row_index + matrix_size):
#         for col in range(column_index, column_index + matrix_size):
#             total_sum += matrix[row][col]
#
#     return total_sum
#
#
# def get_data_for_best_submatrix(matrix, size_of_submatrix):
#     current_largest_row_index = 0
#     current_largest_column_index = 0
#     best_total_sum = submatrix_sum_func(matrix, 0, 0, size_of_submatrix)
#
#     for row_index in range(len(matrix) - size_of_submatrix + 1):
#         for col_index in range(len(matrix[row_index]) - size_of_submatrix + 1):
#             current_sum = submatrix_sum_func(matrix, row_index, col_index, size_of_submatrix)
#
#             if current_sum > best_total_sum:
#                 best_total_sum = current_sum
#                 current_largest_row_index = row_index
#                 current_largest_column_index = col_index
#
#     return current_largest_row_index, current_largest_column_index
#
#
# def print_function(submatrix_data, size):
#     row_index, column_index = submatrix_data
#     for row in range(row_index, row_index + size):
#         data = []
#         for col in range(column_index, column_index + size):
#             data.append(matrix[row][col])
#         print(' '.join(str(x) for x in data))
#     print(submatrix_sum_func(matrix, row_index, column_index, size))
#
#
# matrix = read_matrix()
# size_of_submatrix = 2
# submatrix_data = get_data_for_best_submatrix(matrix, size_of_submatrix)
# print_function(submatrix_data, size_of_submatrix)