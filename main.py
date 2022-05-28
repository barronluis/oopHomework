# Shape Class
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, _color: str = "red", _filled: bool = True):
        self._color = _color
        self._filled = _filled

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def isFilled(self):
        return self._filled

    def setFilled(self, filled):
        self._filled = filled

    @abstractmethod
    def getArea(self):
        ...

    @abstractmethod
    def getPerimeter(self):
        ...

    def toString(self):
        return "Shape[color=" + self._color + ", filled=" + str(self._filled) + "]"


class Circle(Shape):

    def __init__(self, _color: str, _filled: bool, _radius: float = 1.0):
        super(Circle, self).__init__(_color, _filled)
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


class Rectangle(Shape):

    def __init__(self, _color: str, _filled: bool, _width: float = 1.0, _length: float = 1.0):
        super(Rectangle, self).__init__(_color, _filled)
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
        return "Rectangle[Shape[color=" + self._color + ", filled=" + str(self._filled) + "], width=" + str(self._width) + ", length=" + str(self._length) + "]"


class Square(Rectangle):

    def __init__(self, _color: str, _filled: bool, _side: float = 1.0):
        super(Square, self).__init__(_color, _filled)
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
        return "Square[Rectangle[Shape[color=" + self._color + ", filled=" + str(self._filled) + "], width=" + str(self._width) + ", length=" + str(self._length) + "]]"



cr = Square("white", False)
cr.getArea()
print(cr.toString())
