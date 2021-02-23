class Road:
    WEIGHT1M2 = 25 # масса асфальта 1кв см.

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, depth):
        return depth * self.WEIGHT1M2 * self._width * self._length


if __name__ == '__main__':
    road_to_village = Road(1500, 20)
    print(road_to_village.weight(5))
    print(road_to_village._length)
    print(road_to_village._width)