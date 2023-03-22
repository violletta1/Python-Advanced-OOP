class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.element = element
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):     # if len(self.data) == 0 return True else False
        return len(self.data) == 0

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print(stack)
print(stack.top())
stack.pop()
print(stack)
