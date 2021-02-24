from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def get_material_size(self):
        pass

    @property
    def size(self):
        return self.get_material_size()


class Suit(Cloth):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_material_size(self):
        return self.w * self.h


class Coat(Cloth):
    def __init__(self, s, length):
        self.s = s
        self.length = length

    def get_material_size(self):
        return self.s * self.length * 2


suit = Suit(10, 5)
coat = Coat(5, 3)

clothes = [suit, coat]
for cloth in clothes:
    print(cloth.size)