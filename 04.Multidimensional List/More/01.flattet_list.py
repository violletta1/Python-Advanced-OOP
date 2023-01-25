numbers = [string.split() for string in input().split("|")]
print(numbers[::-1])
[print(*row) for row in numbers[::-1]]
print(*[' '.join(string) for string in numbers[::-1] if string])
print([' '.join(string) for string in numbers[::-1]])

# numbers = input().split("|")
#
# full_list = []
#
# for string in numbers[::-1]:
#     full_list.extend(string.split())
#
# print(*full_list)