from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_BOOTH ={
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    VALID_DELICACY = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        delicacy = [d for d in self.delicacies if d.name == name]
        if delicacy:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.VALID_DELICACY:
            raise Exception(F"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACY[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = [b for b in self.booths if b.booth_number == booth_number]
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")
        booth = self.VALID_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) ->str:
        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and not b.is_reserved, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."


    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")
        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        self.income += bill
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

shop = ChristmasPastryShopApp()

print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))

print(shop.delicacies[0].details())

print(shop.add_booth("Open Booth", 1, 30))

print(shop.add_booth("Private Booth", 10, 5))

print(shop.reserve_booth(30))

print(shop.order_delicacy(1, "Gingy"))

print(shop.leave_booth(1))

print(shop.reserve_booth(5))

print(shop.order_delicacy(1, "Gingy"))

print(shop.order_delicacy(1, "Gingy"))

print(shop.order_delicacy(1, "Gingy"))

print(shop.leave_booth(1))

print(shop.get_income())
