# numb_of_names = int(input())
#
# names_data = {input() for _ in range(numb_of_names)}
#
# for name in names_data:
#     print(name)
#
num_names = int(input())

names = set(input() for name in range(num_names))

# for name in range(num_names):
#     names.add(input())

[print(name) for name in names]


