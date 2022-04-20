from .defaultMethods import *

import matplotlib
import matplotlib.pyplot as plt


def line(line1, line2):
    a = [int(x) for x in line1.split()]
    b = [int(x) for x in line2.split()]
    A = [a[0], b[0]]
    B = [a[1], b[1]]
    oper = []

    #Геом преобразования
    if a[0] != 0 or a[1] != 0:
        dx = -a[0]
        dy = -a[1]
        a = moveX(a, dx)
        b = moveX(b, dx)
        a = moveY(a, dy)
        b = moveY(b, dy)
        A1 = [a[0], b[0]]
        B1 = [a[1], b[1]]
        oper.append({'move': (dx, dy)})

    # Если точка находится в 3/4
    if a[1] < 0 or b[1] < 0:
        reflectionOX(a)
        reflectionOX(b)
        A2 = [a[0], b[0]]
        B2 = [a[1], b[1]]
        oper.append({'ox': 0})

    # Если точка находится в 2/4 или 3/4
    if a[0] < 0 or b[0] < 0:
        reflectionOY(a)
        reflectionOY(b)
        A3 = [a[0], b[0]]
        B3 = [a[1], b[1]]
        oper.append({'oy': 0})

    if not correct_angle(a, b):
        reflection(a)
        reflection(b)
        A4 = [a[0], b[0]]
        B4 = [a[1], b[1]]
        oper.append({'yx': 0})

    #Алгоритм
    d = (b[1] - a[1]) - 0.5 * (b[0] - a[0])
    X = [a[0]]
    Y = [a[1]]
    y = a[1]
    for x in range(a[0], b[0]):
        X.append(x + 1)
        if d <= 0:
            d += b[1] - a[1]
            Y.append(y)
        else:
            d += b[1] - a[1] - b[0] + a[0]
            y += 1
            Y.append(y)
    print(X)
    print(Y)

    yxEnd = []
    for i in range(len(X)):
        yxEnd.append([X[i], Y[i]])

    for i in oper[::-1]:
        for h in i:
            if h == 'yx':
                for j in yxEnd:
                    reflection(j)
            elif h == 'oy':
                for j in yxEnd:
                    reflectionOY(j)
            elif h == 'ox':
                for j in yxEnd:
                    reflectionOX(j)
            elif h == 'move':
                for j in range(len(yxEnd)):
                    yxEnd[j] = moveX(yxEnd[j], -i['move'][0])
                    yxEnd[j] = moveY(yxEnd[j], -i['move'][1])

    xEnd = []
    yEnd = []
    for i in yxEnd:
        xEnd.append(i[0])
        yEnd.append(i[1])

    #Вывод
    fig = plt.figure(1)
    ax = fig.gca()
    locatorX = matplotlib.ticker.MultipleLocator(base=1)
    locatorY = matplotlib.ticker.MultipleLocator(base=1)
    ax.xaxis.set_major_locator(locatorX)
    ax.yaxis.set_major_locator(locatorY)
    ax.grid()
    ax.plot(A, B)
    try:
        ax.plot(A1, B1, c='b')
    except NameError:
        pass
    try:
        ax.plot(A2, B2, c='g')
    except NameError:
        pass
    try:
        ax.plot(A3, B3, c='y')
    except NameError:
        pass
    try:
        ax.plot(A4, B4, c='r')
    except NameError:
        pass
    ax.scatter(X, Y)
    ax.scatter(xEnd, yEnd)
    plt.show()