import math

from shape import Shape


class EquilateralTriangle(Shape):

    def __init__(self, _color: str, _filled: bool, _sideLength: float = 1.0):
        super().__init__(_color, _filled)
        self._sideLength = _sideLength

    def getSideLength(self):
        return self._sideLength

    def setSideLength(self, sideLength: float):
        self._sideLength = sideLength

    def getArea(self):
        return (math.sqrt(3) / 4) * math.pow(self._sideLength, 2)

    def getPerimeter(self):
        return self._sideLength * 3

    def toString(self):
        return "Equilateral Triangle[Shape[color=" + self._color + ", filled=" + str(self._filled) + "], sideLength=" + str(self._sideLength) + "]"


if __name__ == "__main__":
    eqt = EquilateralTriangle("orange", True)
    print(eqt.toString())
    print(eqt.getArea())
    print(eqt.getPerimeter())
