from collections import deque

parenthesis = deque(input())
open_parenthesis = deque()

while parenthesis:
    left_parenthesis = parenthesis.popleft()

    if left_parenthesis in "{([":
        open_parenthesis.append(left_parenthesis)
    elif not open_parenthesis:
        print("NO")
        break
    else:
        if f"{open_parenthesis.pop() + left_parenthesis}" not in "{}()[]":
            print("NO")
            break
else:
    print("YES")