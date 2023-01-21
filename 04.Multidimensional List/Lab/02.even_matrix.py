# number_of_rows = int(input())
# matrix = []
#
# for _ in range(number_of_rows):
#     current_row = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
#     matrix.append(current_row)
#
# print(matrix)


matrix = []
for colums in range(int(input())):
    matrix.append([int(x) for x in input().split(", ") if int(x) % 2 ==0])

print(matrix)