# 1. На плоскости. Даны точки A, B, C своими координатами,
# найти уравнение прямой проходящей
# через точку С и параллельную прямой АВ

from .Point import *


def EquationC(equationAB, c):
    k = equationAB[0]
    b = -1 * k * c.x + c.y
    print(f'Уравнение прямой проходящей через точку С {c} имеет вид: y = {k}x + {b}')


a = Point.Point()
b = Point.Point()
c = Point.Point()

equationAB = []

if a.parallel0(b) == 1:
    print(f'Уравнение прямой проходящей через точку С {c} имеет вид: x = {c.x}')
    exit()
elif a.parallel0(b) == 2:
    print(f'Уравнение прямой проходящей через точку С {c} имеет вид: y = {c.y}')
    exit()
else:
    equationAB = a.equationab(b)

if a.oneline(b, c):
    print('Точки на одной прямой')
else:
    EquationC(equationAB, c)
