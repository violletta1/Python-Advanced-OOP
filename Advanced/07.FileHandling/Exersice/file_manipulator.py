import os

while True:
    current_command, *info = input().split("-")

    if current_command == "Create":
        file = open(f"files/{info[0]}", "w")
        file.close()

    elif current_command == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif current_command == "Replace":
        try:
            with open(f"files/{info[0]}", "r") as file:
                text = file.read()

            text = text.replace(info[1], info[2])

            with open(f"files/{info[0]}", "w") as file:
                file.write(text)

        except FileNotFoundError:
            print("An error ocurred!")


    elif current_command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error ocurred!")


    elif current_command == "End":
        break


#  Input
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End