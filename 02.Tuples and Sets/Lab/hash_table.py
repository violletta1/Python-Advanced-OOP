class Set:
    MIN_SIZE = 10


    def __init__(self, size = 10):
        self._size = size
        self.filled = 0
        self.elements = [[] for _ in range(size)]

    def hash_function(self, value):
        return hash(value) % self._size

    def _contains(self, value):
        for i, e in enumerate(self.elements[self.hash_function(value)]):
            if value == e: return 1
        return -1

    def contains(self, value):
        return self._contains(value) >= 0

    def add(self, value):
        self.elements[self.hash_function(value)].append(value)

    def delete(self,value):
        index = self._contains(value)
        if index >= 0:
            self.filled -=1
            self.elements[self.hash_function(value)].pop(index)

    def __str__(self):
        return f"size: {self._size} elements: {self.elements}"

aa = Set()
aa.add(5)
aa.add(55)
aa.add(555)
aa.add(14)


print(aa.__str__())