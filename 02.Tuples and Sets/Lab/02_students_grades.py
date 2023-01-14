
n = int(input())

students_data = {}#create dict

for _ in range(n):
    student_name, grade = input().split(" ")
    if student_name not in students_data:#check if the key = name is not in dict
        students_data[student_name] = []#create new key

    students_data[student_name].append(float(grade)) # add value to the key

for student, grades in students_data.items():
    convert_grades_to_str = " ".join(map(lambda grade: f"{grade:.2f}", grades))

    average_sum = sum(grades)/ len(grades)
    print(f"{student} -> {convert_grades_to_str} (avg: {average_sum:.2f})")