#
# def collect_data_for_arrived_guest():
#     arrived_guests_list = []
#     while True:
#         data = input()
#         if data == "END":
#             break
#         else:
#             arrived_guests_list.append(data)
#
#     return arrived_guests_list
#
# def print_func(not_arrived_guests_data):
#     print(len(not_arrived_guests_data))
#     for guest_num in sorted(not_arrived_guests_data):
#         print(guest_num)
#
# n = int(input())
#
# guest_reservations_list = [input() for _ in range(n)]
# arrived_guests = collect_data_for_arrived_guest()
# not_arrived_guests = set(guest_reservations_list).difference(arrived_guests)
# print_func(not_arrived_guests)

# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END


n = int(input())
all_guest = set()
for _ in range(n):
    all_guest.add(input())

ticket = input()
arrived = set()

while not ticket == "END":
    arrived.add(ticket)

    ticket = input()

print(len(all_guest.difference(arrived)))
[print(x) for x in sorted(all_guest.difference(arrived))]