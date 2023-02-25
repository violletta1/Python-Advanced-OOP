# from collections import deque
# colors = deque(input().split())
#
# complete_colors = []
#
# all_colors = {
#     'colors': ('red', 'blue', 'yellow', 'orange', 'purple', 'green')
# }
# secondary_colors = {
#     'orange': ('red', 'yellow'),
#     'purple': ('red', 'blue'),
#     'green': ('yellow', 'blue')
# }
#
# while colors:
#
#         second = ''
#         if len(colors) > 1:
#             second = colors.pop()
#         first = colors.popleft()
#         for check in (first + second, second + first):
#             if check in all_colors['colors']:
#                 complete_colors.append(check)
#                 break
#         else:
#             for item in (first[:-1], second[:-1]):
#                 if item:
#                     colors.insert(len(colors) // 2, item)
#
# for color, req_colors in secondary_colors.items():
#     if any(x not in complete_colors and color in complete_colors for x in req_colors):
#         complete_colors.remove(color)
#
#
#
# print(complete_colors)

from collections import deque

substring = deque(input().split())

colors = {
    "all colors": ("red", "yellow", "blue", "orange", "purple", "green"),
    "required colors": {
        "orange": ("red", "yellow"),
        "purple": ("red", "blue"),
        "green": ("yellow", "blue")
    }
}

result = []

while substring:

    last_part = ""

    if len(substring) > 1:

        last_part = substring.pop()

    first_part = substring.popleft()

    for color in (first_part + last_part, last_part + first_part):

        if color in colors["all colors"]:

            result.append(color)

            break
    else:

        for item in (first_part[:-1], last_part[:-1]):

            if item:

                substring.insert(len(substring) // 2, item)

for color, req_colors in colors["required colors"].items():

    if any(x not in result and color in result for x in req_colors):

        result.remove(color)

print(result)
