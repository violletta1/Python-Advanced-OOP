# from _collections import deque
#
# text = deque(input().split())
# text.reverse()
# print(" ".join(text))

print(*input().split()[::-1], sep=" ")
