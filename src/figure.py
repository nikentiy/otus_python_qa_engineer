class Figure:
    def __init__(self, name: str):
        self.name: str = name
        self.area: float
        self.perimeter: float

    def add_area(self, figure):
        return self.area + figure.area
