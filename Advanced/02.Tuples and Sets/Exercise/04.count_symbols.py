#1111111111111111111111111111
#occurrences = {}
#
# for letter in input():
#     if letter not in occurrences:
#         occurrences[letter] = 0
#     occurrences[letter] += 1
#
#
# for k, v in sorted(occurrences.items()):
#     print(f"{k}: {v} time/s")


#222222222222222222222222222222222222222222222
# list_input = list(input())
# symbols = {symbol: list_input.count(symbol) for symbol in list_input}
#
# for k, v in sorted(symbols.items()):
#     print(f"{k}: {v} time/s")


#Example input
# SoftUni rocks

#Output
#  : 1 time/s
# S: 1 time/s
# U: 1 time/s
# c: 1 time/s
# f: 1 time/s
# i: 1 time/s
# k: 1 time/s
# n: 1 time/s
# o: 2 time/s
# r: 1 time/s
# s: 1 time/s
# t: 1 time/s

#3333333333333333
text = input()

symbols = {}

for char in text:
    symbols[char] = text.count(char)

for k, v in sorted(symbols.items(), key= lambda x: x[0]): # we use key= to sort the items in dict by key
    print(f"{k}: {v} time/s")