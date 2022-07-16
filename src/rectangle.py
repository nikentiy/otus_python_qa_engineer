from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        super().__init__('rectangle')

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2*(self.a + self.b)
