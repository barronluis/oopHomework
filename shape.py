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






