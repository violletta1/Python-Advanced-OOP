first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())




for current_command in range(int(input())):
    first_command, *data = input().split()

    final_command = first_command + " " + data.pop(0)

    if final_command == "Add First":
        [first_set.add(int(el)) for el in data]

    elif final_command == "Add Second":
        [second_set.add(int(el)) for el in data]

    elif final_command == "Remove First":
        [first_set.discard(int(n)) for n in data]

    elif final_command == "Remove Second":
        [second_set.discard(int(n)) for n in data]

    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print(True)
        else:
            print(False)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")


