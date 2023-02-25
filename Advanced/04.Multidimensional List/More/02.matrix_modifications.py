rows = int(input())

matrix = [[int(n) for n in input().split()] for _ in range(rows)]

command = input().split()

while command[0] != "END":
    current_command, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0<= row < rows and 0 <= col < rows):
        print("Invalid coordinates")
    elif current_command == "Add":
        matrix[row][col] += value
    elif current_command == "Subtract":
        matrix[row][col] -= value

    command = input().split()

[print(*row) for row in matrix]