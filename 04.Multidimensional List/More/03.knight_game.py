n = int(input())

matrix = [list(input()) for el in range(n)]

positions = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (1, 2),
    (2, -1),
    (1, -2)
)# we give eventualy positions for the knight path

removed_knights = 0

while True:#while we have knights
    max_attacks = 0
    knights_position = []

    for row in range(n):# we check every element in the matrix for knight
        for col in range(n):
            if matrix[row][col] == "K": #if the element is knight
                atacks = 0

                for pos in positions: #we check the positions around the knight
                    row_pos = pos[0] + row
                    col_pos = pos[1] + col

                    if 0 <= row_pos < n and 0<= col_pos < n:# we check if the position is valid
                        if matrix[row_pos][col_pos] == "K": # if the indexes are valid and the elements is knight we increase the attacks
                            atacks += 1

                if atacks > max_attacks: # if the attacks of the current knight is more then maximum atacks
                    knights_position = [row, col] #we give the indexes for the new max knight
                    max_attacks = atacks

    if knights_position: # if the knight list is full we get the positions and remove the knight
        r,c = knights_position
        matrix[r][c] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)



