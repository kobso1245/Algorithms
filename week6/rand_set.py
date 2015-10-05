import random


class Hash:
    self.arr = []
    self.elems = []
    self.last_pos = -1

    def __init__(self):
        for i in range(1000000):
            self.arr.append(0)

    def insert(self, elem):
        self.last_pos += 1
        self.arr[1000000 - elem] = self.last_pos
        self.elems.append(elem)

    def remove(self, elem):
        last_elem = self.elems.pop()
        self.last_pos -= 1
        self.arr[1000000 - last_elem] = self.arr[1000000 - elem]
        self.arr[1000000 - last_elem] = last_elem
        self.arr[1000000 - elem] = False

    def contains(self, elem):
        if self.arr[1000000 - elem] is not False:
            return True
        else:
            return False

    def random(self):
        return random.choice(self.elems)
