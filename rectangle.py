from shape import Shape


class Rectangle(Shape):

    def __init__(self, _color: str, _filled: bool, _width: float = 1.0, _length: float = 1.0):
        super().__init__(_color, _filled)
        self._width = _width
        self._length = _length

    def getWidth(self):
        return self._width

    def setWidth(self, width: float):
        self._width = width

    def getLength(self):
        return self._length

    def setLength(self, length: float):
        self._length = length

    def getArea(self):
        return self._width * self._length

    def getPerimeter(self):
        return (self._length * 2) + (self._width * 2)

    def toString(self):
        return "Rectangle[Shape[color=" + self._color + ", filled=" + str(self._filled) + "], width=" + str(
            self._width) + ", length=" + str(self._length) + "]"


if __name__ == "__main__":
    rectangle = Rectangle("yellow", False)
    print(rectangle.toString())
    print(rectangle.getArea())
    print(rectangle.getPerimeter())


