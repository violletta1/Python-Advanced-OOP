# presents = [int(input())]
# rows = int(input())
# matrix = [[char for char in input().split()] for row in range(rows)]
# cols, total_nice_kids = len(matrix[0]), [[sum([matrix[row].count("V") for row in range(rows)])] * 2]
# directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
#
#
# def check_valid_index(row, col):
#     if 0 <= row < rows and 0 <= col < cols:
#         return True
#
#
# def find_position():
#     for row in range(rows):
#         if "S" in matrix[row]:
#             col = matrix[row].index("S")
#             matrix[row][col] = "-"
#             return row, col
#
#
# def check_where_he_steps(row, col, cookie=False):
#     if matrix[row][col] == "V":
#         total_nice_kids[0][0] -= 1
#         presents[0] -= 1
#
#     elif cookie and matrix[row][col] == "X":
#         presents[0] -= 1
#
#     elif matrix[row][col] == "C":
#         cookie_time(row, col)
#
#     matrix[row][col] = "-"
#
#
# def cookie_time(row, col):
#     for added_row, added_col in directions.values():
#
#         moving_row, moving_col = row + added_row, col + added_col
#
#         if check_valid_index(moving_row, moving_col):
#             check_where_he_steps(moving_row, moving_col, True)
#
#
# def santa_move(row, col, direction):
#     santa_moving_row, santa_moving_col = row + directions[direction][0], col + directions[direction][1]
#
#     if check_valid_index(santa_moving_row, santa_moving_col):
#         check_where_he_steps(santa_moving_row, santa_moving_col)
#
#     return santa_moving_row, santa_moving_col
#
#
# def check_for_end():
#     if total_nice_kids[0][0] == 0:
#
#         show_result(santa_row, santa_col)
#         print(f"Good job, Santa! {total_nice_kids[0][1]} happy nice kid/s.")
#         exit()
#
#     if presents[0] == 0 and total_nice_kids[0][0] > 0:
#
#         print("Santa ran out of presents!")
#         show_result(santa_row, santa_col)
#         print(f"No presents for {total_nice_kids[0][0]} nice kid/s.")
#         exit()
#     if presents[0] == 0:
#
#         show_result(santa_row, santa_col)
#         print(f"No presents for {total_nice_kids[0][0]} nice kid/s.")
#         exit()
#
#
# def show_result(row, col):
#     matrix[row][col] = "S"
#     [print(*matrix[row]) for row in range(rows)]
#
#
# santa_row, santa_col = find_position()
# command = input()
#
# while command != "Christmas morning":
#     santa_row, santa_col = santa_move(santa_row, santa_col, command)
#     check_for_end()
#     command = input()
#
# show_result(santa_row, santa_col)
# print(f"No presents for {total_nice_kids[0][0]} nice kid/s.")

#222222222222
def eat_cookie(presents_left, nice_kids):  # създаваме фунцкия, първи параметър останалите подаръци и втори добрите деца
    for x, y in directions.values():  # обхождаме всяка посока от посоките
        r = santa_pos[0] + x  # намираме реда като съберем реда на Дядо Коледа и реда от посоката
        c = santa_pos[1] + y  # намираме колоната като съберем колоната на Дядо Коледа и тази от посоката

        if neighborhood[r][c].isalpha():  # проверяваме дали сме стъпили на буква
            if neighborhood[r][c] == 'V':  # проверяваме дали сме в къщата на добро дете
                nice_kids += 1  # увеличаваме броя на посетените добри деца за скоупа на функцията

            neighborhood[r][c] = '-'  # заменяме позицията, на която сме с тире
            presents_left -= 1  # намаляме наличните подаръци с 1, в скоупа на функцията

        if not presents_left:  # проверяваме дали са ни свършили подаръците
            break  # прекратяваме цикъла

    return presents_left, nice_kids  # връщаме наличните подаръци и броя на посетените добри деца


presents = int(input())  # прочитаме броя подаръци
size = int(input())  # прочитаме размера на матрицата

neighborhood = []  # създаваме променлива, в която да пазим матрицата
santa_pos = []  # създаваме променлива, в която да пазим позицията на Дядо Коледа

total_nice_kids = 0  # създаваме променлива, в която да пазим броя на добрите деца
nice_kids_visited = 0  # създаваме променлива, в която да пазим броя на посетените добри деца

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
    line = input().split()  # прочитаме ред от конзолата и го разделяме по спейс

    neighborhood.append(line)  # добавяме реда към матрицата

    if 'S' in line:  # проверяваме дали Дядо Коледа е на този ред
        santa_pos = [row, line.index('S')]  # запазваме позицията на Дядо Коледа
        neighborhood[row][santa_pos[1]] = '-'  # променяме стойността на позицията на Дядо Коледа на тире

    total_nice_kids += line.count('V')  # добавяме броя им от реда, към общия брой добри деца

command = input()  # прочитаме команда, опции - up, down, left, right, Christmas morning

while command != "Christmas morning":  # развъртаме while цикъл, докато командата е различна от Christmas morning
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]  # обновяваме позицията на Дядо Коледа, като събираме текущата му позиция с тази от координатите

    house = neighborhood[santa_pos[0]][santa_pos[1]]  # запазваме стойността на текущата къща

    if house == 'V':  # проверяваме дали в къщата има добро дете
        nice_kids_visited += 1  # увеличаваме броя на посетените добри деца
        presents -= 1  # намаляме броя на подаръците
    elif house == 'C':  # проверяваме дали в къщата има бисквитки
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)  # извикваме функцията eat_cookies()

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'  # заменяме позицията, на която сме с тире

    if not presents or nice_kids_visited == total_nice_kids:
        break  # проверяваме дали са ни свършили подаръците или сме минали през всички добри деца в квартала

    command = input()  # прочитаме команда

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'  # поставяме Дядо Коледа на позицията му

if not presents and nice_kids_visited < total_nice_kids:  # проверка нямаме подаръци и не сме посетили всички добри деца
    print('Santa ran out of presents!')  # принтираме, Santa ran out of presents!

print(*[' '.join(line) for line in neighborhood], sep='\n')  # принтираме матрицата, като джойнваме всеки ред по спейс

if nice_kids_visited == total_nice_kids:  # проверяваме дали всички добри деца са получили подаръци
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')  # принтираме
else:  # ако не всички добри деца са получили подаръци
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')  # принтираме



#input
# 3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up
#output
# Santa ran out of presents!
# - - - -
# V - - -
# - - S -
# - - - -
# No presents for 1 nice kid/s.