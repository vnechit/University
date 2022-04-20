import math


def moveX(a, n):
    return [a[0] + n, a[1]]


def moveY(a, n):
    return [a[0], a[1] + n]


def dist2bis(a):
    # подставляем координаты точки в уравнение прямой -1x+y+0=0. берем по модулю. и делим на sqrt(a^2+b^2)
    return abs(-a[0] + a[1]) / math.sqrt(2)


def reflection(a):
    a.reverse()


def correct_angle(a, b):
    return -abs(a[0] - b[0]) + abs(a[1] - b[1]) <= 0


def reflectionOX(a):
    a[1] = -a[1]


def reflectionOY(a):
    a[0] = -a[0]