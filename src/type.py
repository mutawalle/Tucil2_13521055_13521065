class Point:
    def __init__(self, dimension: int, values: list[int]):
        self.dimension = dimension
        self.values = values

class TwoPointDistance:
    def __init__(self, distance: float, index1: int, index2: int):
        self.distance = distance
        self.index1 = index1
        self.index2 = index2