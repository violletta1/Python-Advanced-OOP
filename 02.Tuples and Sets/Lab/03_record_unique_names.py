numb_of_names = int(input())

names_data = {input() for _ in range(numb_of_names)}

for name in names_data:
    print(name)

