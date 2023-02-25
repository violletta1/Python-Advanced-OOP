#
# def print_func(data):
#     if data:
#         for car_number in data:
#             print(car_number)
#     else:
#         print("Parking Lot is Empty")
#
# num_of_transactions = int(input())
#
# plate_num_records = [input() for _ in range(num_of_transactions)]
#
# parking_lot_data = set()
#
# for record in plate_num_records:
#     command, plate_number = record.split(", ")
#
#     if command == "IN":
#         parking_lot_data.add(plate_number)
#
#     elif command == "OUT":
#         parking_lot_data.remove(plate_number)
#
# print_func(parking_lot_data)

# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU


n = int(input())

cars = set()

for _ in range(n):
    command, number = input().split(", ")
    if command == "IN":
        cars.add(number)
    else:
        cars.discard(number)

if not cars:
    print("Parking Lot is Empty")
else:
    [print(car) for car in cars]