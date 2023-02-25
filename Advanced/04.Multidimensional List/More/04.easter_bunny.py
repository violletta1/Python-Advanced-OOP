# import sys
#
#
# def up():
#     global eggs
#     global direction
#     global max_eggs_sum
#
#     bunny = [row, column]
#
#     eggs_sum = 0
#     coordinates = []
#
#     try:
#
#         while bunny[0] >= 1 and field[bunny[0]-1][bunny[1]] != "X":
#
#             bunny[0] -= 1
#             coordinates.append([bunny[0], bunny[1]])
#             eggs_sum += int(field[bunny[0]][bunny[1]])
#
#     except IndexError:
#         ''' The Index is out of the columns range, do nothing. '''
#
#     if eggs_sum >= max_eggs_sum:
#
#         eggs = coordinates
#         coordinates = []
#         max_eggs_sum = eggs_sum
#         direction = 'up'
#
#     else:
#
#         coordinates = []
#
#
# def left():
#     global eggs
#     global direction
#     global max_eggs_sum
#
#     bunny = [row, column]
#
#     eggs_sum = 0
#     coordinates = []
#
#     try:
#
#         while bunny[1] >= 1 and field[bunny[0]][bunny[1]-1] != "X":
#
#             bunny[1] -= 1
#             coordinates.append([bunny[0], bunny[1]])
#             eggs_sum += int(field[bunny[0]][bunny[1]])
#
#     except IndexError:
#         ''' The Index is out of the columns range, do nothing. '''
#
#     if eggs_sum >= max_eggs_sum:
#
#         eggs = coordinates
#         coordinates = []
#         max_eggs_sum = eggs_sum
#         direction = 'left'
#
#     else:
#
#         coordinates = []
#
#
# def right():
#     global eggs
#     global direction
#     global max_eggs_sum
#
#     bunny = [row, column]
#
#     eggs_sum = 0
#     coordinates = []
#
#     try:
#
#         while bunny[1] < len(field[row]) and field[bunny[0]][bunny[1]+1] != "X":
#
#             bunny[1] += 1
#             coordinates.append([bunny[0], bunny[1]])
#             eggs_sum += int(field[bunny[0]][bunny[1]])
#
#     except IndexError:
#         ''' The Index is out of the columns range, do nothing. '''
#
#     if eggs_sum >= max_eggs_sum:
#
#         eggs = coordinates
#         coordinates = []
#         max_eggs_sum = eggs_sum
#         direction = 'right'
#
#     else:
#
#         coordinates = []
#
#
# def down():
#     global eggs
#     global direction
#     global max_eggs_sum
#
#     bunny = [row, column]
#
#     eggs_sum = 0
#     coordinates = []
#
#     try:
#
#         while bunny[0] < len(field) and field[bunny[0]+1][bunny[1]] != "X":
#
#             bunny[0] += 1
#             coordinates.append([bunny[0], bunny[1]])
#             eggs_sum += int(field[bunny[0]][bunny[1]])
#
#     except IndexError:
#         ''' The Index is out of the columns range, do nothing. '''
#
#     if eggs_sum >= max_eggs_sum:
#
#         eggs = coordinates
#         coordinates = []
#         max_eggs_sum = eggs_sum
#         direction = 'down'
#
#     else:
#
#         coordinates = []
#
#
# rows = int(input())
#
# field = []
# eggs = []
# direction = ''
# max_eggs_sum = -sys.maxsize
#
# for row in range(rows):
#     columns = input().split()
#     field.append(columns)
#
# find_bunny = False
#
# for row in range(len(field)):
#
#     for column in range(len(field[row])):
#
#         if field[row][column] == "B":
#
#             up()
#             left()
#             right()
#             down()
#
#             find_bunny = True
#             break
#
#     if find_bunny:
#         break
#
# if direction != '':
#     print(direction)
#     [print(egg) for egg in eggs]
#     print(max_eggs_sum)
#

#222222222222222222
size = int(input())  # прочитаме размера на матрицата

matrix = []  # създаваме променлива, в която да пазим матрицата
bunny_pos = []  # създаваме променлива, в която да пазим позицията на заека
best_path = []  # създаваме променлива, в която да пазим най-добрия път

best_direction = None  # създаваме променлива, в която да пазим най-добрата посока
max_collected_eggs = 0  # създаваме променлива, в която да пазим максималния брой яйца

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
    matrix.append(input().split())  # прочитаме ред от конзолата, разделяме по спейс и го добавяме към матрицата

    if 'B' in matrix[row]:  # проверяваме дали заека е на този ред
        bunny_pos = [row, matrix[row].index('B')]  # ако да, запазваме реда и колоната, на които е заека

for direction, positions in directions.items():  # развъртаме цикъл за всяка посока и нейните позиции
    row, col = [  # запазваме новата позиция, като събираме текущата позиция с тази от речника
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]
    path = []  # създаваме променлива, в която да пазим текущия път
    collected_eggs = 0  # създаваме променлива, в която да пазим броя на събраните яйца за текущата посока

    while 0 <= row < size and 0 <= col < size:  # развъртаме цикъл с условие докато позицията на яйцето е валидна
        if matrix[row][col] == 'X':  # проверяваме дали имаме капан на текущата позиция
            break  # прекратяваме цикъла

        collected_eggs += int(matrix[row][col])  # събираме яйцата на текущата позиция с текущите яйца
        path.append([row, col])  # добавяме текущата позиция към текущия път

        row += positions[0]  # събираме текущия ред с реда от посоката, в която се движим
        col += positions[1]  # събираме текущата колона с колоната от посоката, в която се движим

    if collected_eggs >= max_collected_eggs:  # EDGE: проверяваме дали текущите яйца са повече или равни на максималните
        max_collected_eggs = collected_eggs  # обновяваме максималния брой яйца
        best_direction = direction  # обновяваме най-добрата посока
        best_path = path  # обновяваме най-добрия път

print(best_direction)  # принтираме най-добрата посока
print(*best_path, sep='\n')  # принтираме най-добрия път
print(max_collected_eggs)  # принтираме максималния брой яйца

#input
# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
#output
# right
# [3, 1]
# [3, 2]
# [3, 3]
# [3, 4]
# 87