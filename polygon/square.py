from polygon.quadrilateral import Quadrilateral


class Square(Quadrilateral):
    def __init__(self, side_length):
        super().__init__(width=side_length, height=side_length)

    def __str__(self):
        return f"Square (side length = {self.height})"
