from polygon import Rectangle
from polygon import Square


def example_code() -> None:
    square = Square(side_length=10)
    rectangle = Rectangle(width=10, height=10)

    print(f"Square area : {square.area}")
    print(f"Rectangle area : {rectangle.area}")


if __name__ == "__main__":
    example_code()
