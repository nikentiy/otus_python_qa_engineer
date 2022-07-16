import math

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        super().__init__('triangle')

    @property
    def area(self):
        half = self.perimeter / 2
        return math.sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
