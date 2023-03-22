import math


class Number:
    def __init__(self, number):
        self.number = number

    def increase_with_root(self):   #Instance method
        self.number += self.get_root(self.number)

    @staticmethod
    def get_root(number):
        return math.sqrt(number)

    @classmethod                    # Create new object from this class
    def from_float(cls, float_number):
        return cls(int(float_number))

    def __repr__(self):
        return f"{self.number}"


print(Number.get_root(49))
a= Number.from_float(121.5)
print(a)

print(a.get_root(49))
a.increase_with_root()
print(a)
