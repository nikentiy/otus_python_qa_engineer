import math

from src.figure import Figure


class Circle(Figure):
    def __init__(self, r: float):
        self.r = r
        super().__init__('circle')

    @property
    def area(self):
        return math.pi * (self.r ** 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.r
