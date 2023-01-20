# names_count = int(input())
#
# unique_names = set()
#
# for _ in range(names_count):
#     unique_names.add(input())
#
# print(*unique_names, sep="\n")
#
print(*{input() for _ in range(int(input()))}, sep="\n")