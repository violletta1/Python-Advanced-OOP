numbers_dictionary = {}

line = input()
while line != "Search":
    try:
        number_as_string = line
        number = int(input())  # if input == str("two") => Value error
        numbers_dictionary[number_as_string] = number
    except ValueError:  # if we get input different then int the error-value come and we print()
        print("The variable number must be an integer")

    line = input()

line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])  # {"one": 1} => nums_dict["two"] => KeyError
    except KeyError: # if we try to print value from a key in dict which not exist we get key error and we print()
        print("Number does not exist in dictionary")

    line = input()

line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched] # {"one": 1} => del nums_dict["two"] => KeyError
    except KeyError: # if we try to delete value with a non existing key in dict we got Key error
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)