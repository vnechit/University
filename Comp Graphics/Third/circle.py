from .defaultMethods import *

import matplotlib
import matplotlib.pyplot as plt


def circle(inp, R):
    center = [float(x) for x in inp.split()]
    # Перенос в начало координат
    dx = center[0]
    dy = center[1]
    moveX(center, -dx)
    moveY(center, -dy)

    R = float(R)
    d = 1 - R
    x = 0
    y = R
    X = [x]
    Y = [y]

    c = plt.Circle(center, R, color='r', fill=False)
    ax = plt.gca()
    ax.add_patch(c)
    # Алгоритм
    while x < y:
        if d < 0:
            d += 2 * x + 3
            x += 1
        else:
            d += 2 * x - 2 * y + 5
            x += 1
            y -= 1
        X.append(x)
        Y.append(y)

    # Отражение точек
    tmp = list(X)
    X.extend(Y)
    Y.extend(tmp)
    X1 = X.copy()
    X2 = X.copy()
    X3 = X.copy()
    Y1 = Y.copy()
    Y2 = Y.copy()
    Y3 = Y.copy()

    for i in range(len(X)):
        X1[i] = -X1[i]
        Y2[i] = -Y2[i]
        X3[i] = -X3[i]
        Y3[i] = -Y3[i]


    # Объединение точек
    Xe = X + X1 + X2 + X3
    Ye = Y + Y1 + Y2 + Y3

    for i in range(len(Xe)):
        Xe[i] += dx
        Ye[i] += dy

    fig = plt.figure(1)
    ax = fig.gca()
    locatorX = matplotlib.ticker.MultipleLocator(base=1)
    locatorY = matplotlib.ticker.MultipleLocator(base=1)
    ax.xaxis.set_major_locator(locatorX)
    ax.yaxis.set_major_locator(locatorY)
    ax.grid()
    ax.scatter(Xe, Ye)
    m = abs(max(center)) + (2*R)
    plt.xlim(-1*m, m)
    plt.ylim(-1*m, m)
    plt.show()
