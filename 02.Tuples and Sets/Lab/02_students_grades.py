#
# n = int(input())
#
# students_data = {}#create dict
#
# for _ in range(n):
#     student_name, grade = input().split(" ")
#     if student_name not in students_data:#check if the key = name is not in dict
#         students_data[student_name] = []#create new key
#
#     students_data[student_name].append(float(grade)) # add value to the key
#
# for student, grades in students_data.items():
#     convert_grades_to_str = " ".join(map(lambda grade: f"{grade:.2f}", grades))
#
#     average_sum = sum(grades)/ len(grades)
#     print(f"{student} -> {convert_grades_to_str} (avg: {average_sum:.2f})")
#

number = int(input())

students_grades = {}

for _ in range(number):
    student, grade = input().split(" ")
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student, grades in students_grades.items():

    average_grades = sum(grades) / len(grades)
    grades_str = " ".join(map(lambda grade: f"{grade:.2f}", grades))

    print(f"{student} -> {grades_str} (avg: {average_grades:.2f})")


# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00