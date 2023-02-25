
def operate(operation, *args):
    result = args[0]

    if operation == "+":
        result = sum(args)

    elif operation == "-":
        for num in args[1:]:
            result -= num

    elif operation == "/":
        for num in args[1:]:
            result /= num

    elif operation == "*":
        for num in args[1:]:
            result *= num

    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 17, 12, 3))
print(operate("/", 20, 5, 2))