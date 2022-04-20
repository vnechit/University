# 3. В пространстве. Треугольник задан координатами своих вершин.
# Определить вид треугольника (остроугольный, тупоугольный или прямоугольный)
import math
from .Point import *


def OnOneLine(a, b, c):
    return c.x * (b.y - a.y) - c.y * (b.x - a.x) == a.x * b.y - b.x * a.y


def ScalarProduct(ax, ay, bx, by):
    return ax * bx + ay * by


def Corner(_a, _b, _c):
    return _a / (_b * _c)


def Revector(_vector):
    vector = [_vector[0] * (-1), _vector[1] * (-1)]
    return vector


a = Point.Point()
b = Point.Point()
c = Point.Point()

if not OnOneLine(a, b, c):

    dAB = a.distance(b)
    dBC = b.distance(c)
    dAC = a.distance(c)

    vectorAB = a.vector(b)
    vectorAC = a.vector(c)
    vectorCB = c.vector(b)
    vectorBA = Revector(vectorAB)
    vectorCA = Revector(vectorAC)
    vectorBC = Revector(vectorCB)

    scA = ScalarProduct(vectorAB[0], vectorAB[1], vectorAC[0], vectorAC[1])
    scB = ScalarProduct(vectorBA[0], vectorBA[1], vectorBC[0], vectorBC[1])
    scC = ScalarProduct(vectorCA[0], vectorCA[1], vectorCB[0], vectorCB[1])

    cornerA = math.acos(Corner(scA, dAB, dAC)) * 180/math.pi
    cornerB = math.acos(Corner(scB, dAB, dBC)) * 180/math.pi
    cornerC = math.acos(Corner(scC, dAC, dBC)) * 180/math.pi

    print(f'Угол А = {cornerA}, угол В = {cornerB}, угол С = {cornerC}')

    if cornerA == 90 or cornerB == 90 or cornerC == 90:
        print('Треугольник прямоугольный')
    elif cornerA > 90 or cornerB > 90 or cornerC > 90:
        print('Треугольник тупоугольный')
    else:
        print('Треугольник остроугольный')