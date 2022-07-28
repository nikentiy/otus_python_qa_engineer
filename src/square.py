from src.figure import Figure


class Square(Figure):
    def __init__(self, a: float):
        self.a = a
        super().__init__('square')

    @property
    def area(self):
        return self.a * self.a

    @property
    def perimeter(self):
        return 4 * self.a
