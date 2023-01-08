import random
import collections

class GuitarString():
    def __init__(self, f):
        self.f = f
        self.table = collections.deque([0] * int(44100//self.f))
    def pluck(self):
        self.table.clear()
        for i in range(int(44100//self.f)):
            self.table.append(random.uniform(-0.5, 0.5))
    def tick(self):
        new = 0.996 * 0.5 * (self.table.popleft() + self.table[0])
        self.table.append(new)
        return new

a_string = GuitarString(440.00)