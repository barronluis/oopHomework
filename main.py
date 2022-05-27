# Shape Class
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, __color="red", __filled=True):
        self.__color = __color
        self.__filled = __filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass

    def __str__(self):
        return "Shape[Color=" + self.color + ", filled=" + self.__filled + "]"


sh = Shape()
print(sh.getColor())
print(sh.isFilled())
