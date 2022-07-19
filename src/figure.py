class Figure:
    def __init__(self, name: str):
        self.name: str = name
        self.area: float
        self.perimeter: float

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Make sure you pass a figure to add area')
        return self.area + figure.area
