import math

from shape import Shape


class Circle(Shape):

    def __init__(self, _color: str, _filled: bool, _radius: float = 1.0):
        super().__init__(_color, _filled)
        self._radius = _radius

    def getRadius(self):
        return self._radius

    def setRadius(self, radius: float):
        self._radius = radius

    def getArea(self):
        return math.pi * math.pow(self._radius, 2)

    def getPerimeter(self):
        return 2 * math.pi * self._radius

    def toString(self):
        return "Circle[Shape[color=" + self._color + ", filled=" + str(self._filled) + "], radius=" + str(
            self._radius) + "]"


if __name__ == "__main__":
    circle = Circle("yellow", True)
    print(circle.toString())
    print(circle.getArea())
    print(circle.getPerimeter())
