from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, _color: str, _filled: bool, _side: float = 1.0):
        super().__init__(_color, _filled)
        self._side = _side

    def getSide(self):
        return self._side

    def setSide(self, side: float):
        self._side = side

    def setWidth(self, side: float):
        self._side = side

    def setLength(self, side: float):
        self._side = side

    def toString(self):
        return "Square[Rectangle[Shape[color=" + self._color + ", filled=" + str(self._filled) + "], width=" + str(
            self._width) + ", length=" + str(self._length) + "]]"


if __name__ == "__main__":
    sq = Square("yellow", True)
    print(sq.toString())
    print(sq.getArea())
    print(sq.getPerimeter())


