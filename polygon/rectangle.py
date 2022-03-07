from polygon.quadrilateral import Quadrilateral



class Rectangle(Quadrilateral):
    def __init__(self, width, height):
        super().__init__(width=width, height=height)

    def __str__(self):
        return f"Rectangle (width = {self.width}, height = {self.height})"
