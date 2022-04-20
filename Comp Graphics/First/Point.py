import math


class Point:
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            self.__x = float(input('X = '))
            self.__y = float(input('Y = '))
        else:
            self.__x = float(x)
            self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return f'({self.__x};{self.__y})'

    def parallel0(self, b):
        if self.__x == b.__x:
            return 1
        elif self.__y == b.__y:
            return 2
        else:
            return 0

    def equationab(self, b):
        k = (self.__y - b.__y) / (self.__x - b.__x)
        b = b.__y - k * b.__x
        equation = [k, b]
        return equation

    def oneline(self, b, c):
        equation = self.equationab(b)
        if c.__y == equation[0] * c.__x + equation[1]:
            return True
        else:
            return False

    def distance(self, b):
        return math.sqrt(math.pow(self.__x - b.__x, 2) + math.pow(self.__y - b.__y, 2))

    def vector(self, b):
        vector = [b.x - self.__x, b.y - self.__y]
        return vector
