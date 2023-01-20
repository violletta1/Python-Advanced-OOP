# from collections import deque
#
# chocolate = deque(int(x) for x in input().split(', '))   # pop
# milk = deque(int(x) for x in input().split(', '))     # popleft
# milkshake = 0
#
#
# while chocolate and milk and milkshake != 5:
#     if chocolate[-1] <= 0 and milk[0] <= 0:
#         milk.popleft()
#         chocolate.popleft()
#         continue
#     elif chocolate[-1] <= 0:
#         chocolate.pop()
#         continue
#     elif milk[0] <= 0:
#         milk.popleft()
#         continue
#
#     if chocolate[-1] == milk[0]:
#         chocolate.pop()
#         milk.popleft()
#         milkshake += 1
#
#     else:
#         milk.append(milk.popleft())
#         chocolate.append(chocolate.pop() - 5)
#
#
# if milkshake == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# if chocolate:
#     print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
# else:
#     print("Chocolate: empty")
#
# if milk:
#     print(f"Milk: {', '.join(str(x) for x in milk)}")
# else:
#     print("Milk: empty")
from collections import deque


class Stack:

    def __init__(self, items):
        self.stack = list(items)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def count(self):
        return len(self.stack)

    def __repr__(self):
        return ', '.join([str(item) for item in self.stack])


chocolates = Stack(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolates.count() and cups_of_milk and milkshakes < 5:

    current_chocolate = chocolates.pop()
    current_cup = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup <= 0:
        continue

    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup)
        continue

    elif current_cup <= 0:
        chocolates.push(current_chocolate)
        continue

    if current_chocolate == current_cup:
        milkshakes += 1

    else:
        cups_of_milk.append(current_cup)
        chocolates.push(current_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")

else:
    print("Not enough milkshakes.")

if chocolates.count():
    print(f"Chocolate: {chocolates}")

else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(num) for num in cups_of_milk])}")

else:
    print("Milk: empty")