import os

def save_extensions(dir_name, firstlevel=False):
    all_files = os.listdir(dir_name)

    for file_name in all_files:
        file = os.path.join(dir_name, file_name)


        if os.path.isfile(file):
            extension = file.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(file_name)

        elif os.path.isdir(file) and not firstlevel:
            save_extensions(file)


directory = input()
extensions = {}
result = []

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")
    for file in sorted(files):
        result.append(f"- - -{file}")

print(*result, sep="\n")

with open(f"files/report.txt", "w") as file:
    file.write("\n".join(result))

