nums = [int(el) for el in input().split()]

positive_nums = 0
negative_num = 0


for num in nums:
    if num < 0:
        negative_num += num
    else:
        positive_nums += num

print(negative_num)
print(positive_nums)

if abs(negative_num) > positive_nums:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


#22222222
# def sum_negative():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num < 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def sum_positive():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num > 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def print_result(positive, negative):
#     print(negative)
#     print(positive)
#
#     if positive > abs(negative):
#         print(f"The positives are stronger than the negatives")
#     else:
#         print(f"The negatives are stronger than the positives")
#
#
# numbers = [int(x) for x in input().split()]
#
# positive_numbers = sum_positive()
# negative_numbers = sum_negative()
#
# print_result(positive_numbers, negative_numbers)