import math
import matplotlib.pyplot as plt

DEFAULT_POINT_1 = []
DEFAULT_POINT_2 = []


def preprocess(m1):
    # return [[m1[j][i] for j in range(len(m1))] for i in range(len(m1[0]))]
    return [[i] for i in m1]


def postprocess(m1):
    return [round(i[0], 5) for i in m1]


def matrixmult(m1, m2):
    s = 0  # сумма
    t = []  # временная матрица
    m3 = []  # конечная матрица
    r1 = len(m1)  # количество строк в первой матрице
    c1 = len(m1[0])  # Количество столбцов в 1
    r2 = len(m2)  # и строк во 2ой матрице
    c2 = len(m2[0])  # количество столбцов во 2ой матрице
    if r2 != c1:
        print("Матрицы не могут быть перемножены")
    else:
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s += m1[z][i] * m2[i][j]
                t.append(s)
                s = 0
            m3.append(t)
            t = []
    return m3


def retry():
    return DEFAULT_POINT_1, DEFAULT_POINT_2


def moveX(a, m):
    b = [[1, 0, m], [0, 1, 0], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def moveY(a, m):
    b = [[1, 0, 0], [0, 1, m], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def reflectionX(a):
    b = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def reflectionY(a):
    b = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def reflectionXY(a):
    b = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def scaleX(a, m):
    b = [[m, 0, 0], [0, 1, 0], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def scaleY(a, m):
    b = [[1, 0, 0], [0, m, 0], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def rotation_centre(a, angle):
    angle = angle * math.pi / 180
    b = [[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(b, A)
    return postprocess(res)


def rotation_point(a, b, angle):
    angle = angle * math.pi / 180
    c = [[1, 0, b[0]], [0, 1, b[1]], [0, 0, 1]]
    d = [[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
    e = [[1, 0, -b[0]], [0, 1, -b[1]], [0, 0, 1]]
    A = preprocess(a)
    res = matrixmult(c, d)
    res = matrixmult(res, e)
    res = matrixmult(res, A)
    return postprocess(res)


def select_menu(i):
    return {0: retry, 1: moveX, 2: moveY, 3: reflectionX, 4: reflectionY, 5: reflectionXY,
            6: scaleX, 7: scaleY, 8: rotation_centre, 9: rotation_point}.get(i, 'error')


def one():
    r = float(input('Введите длину стороны многоугольника: '))
    r = r / (2 * math.sin(math.pi / 5))
    X = []
    Y = []
    #####################Вершины 5угльника#####################
    for i in range(5):
        x = r * math.cos(2 * math.pi * i / 5)
        y = r * math.sin(2 * math.pi * i / 5)
        X.append(x)
        Y.append(y)
    X.append(X[0])
    Y.append(Y[0])
    X2 = [(X[4]+X[2])/2, X[3], X[2], X[1], X[4], X[2], (X[1]+X[4])/2]
    Y2 = [(Y[4]+Y[2])/2, Y[3], Y[2], Y[1], Y[4], Y[2], (Y[1]+Y[4])/2]

    ########################################################

    spisok = []
    spisok2 = []
    for i in range(len(X)):
        spisok.append((X[i], Y[i], 1))
    for ind in range(len(spisok)):
        spisok[ind] = rotation_centre(spisok[ind], 90)
    for i in range(len(X2)):
        spisok2.append((X2[i], Y2[i], 1))
    for ind in range(len(spisok2)):
        spisok2[ind] = rotation_centre(spisok2[ind], 90)

    DEFAULT_POINT_1 = list(spisok)
    DEFAULT_POINT_2 = list(spisok2)
    while True:
        print(spisok)
        print(spisok2)
        X = []
        Y = []
        X2 = []
        Y2 = []
        for i in spisok2:
            X2.append(i[0])
            Y2.append(i[1])
        lim = 0
        for i in spisok:
            X.append(i[0])
            Y.append(i[1])
            if abs(i[0]) > lim:
                lim = abs(i[0])
            if abs(i[1]) > lim:
                lim = abs(i[1])
        plt.plot(X, Y, color='black')
        plt.plot(X2, Y2, color='black')
        plt.xlim(-lim - 2, lim + 2)
        plt.ylim(-lim - 2, lim + 2)
        plt.grid()
        plt.show()
        i = int(input("""
0 - retry
1 - moveX
2 - moveY
3 - reflectionX
4 - reflectionY
5 - reflectionXY
6 - scaleX
7 - scaleY
8 - rotation_centre
9 - rotation_point
        """))
        selected = select_menu(i)
        if selected == 'error':
            break
        if selected in [moveX, moveY, scaleX, scaleY, rotation_centre]:
            a = float(input('Введите число: '))
            for ind in range(len(spisok)):
                spisok[ind] = selected(spisok[ind], a)
            for ind in range(len(spisok2)):
                spisok2[ind] = selected(spisok2[ind], a)
        elif selected in [retry]:
            spisok = DEFAULT_POINT_1
            spisok2 = DEFAULT_POINT_2
        elif selected in [reflectionX, reflectionY, reflectionXY]:
            for ind in range(len(spisok)):
                spisok[ind] = selected(spisok[ind])
            for ind in range(len(spisok2)):
                spisok2[ind] = selected(spisok2[ind])
        else:
            a = [float(i) for i in input('Введите точку: ').split()]
            if len(a) < 3:
                a.append(1)
            angle = float(input('Введите угол: '))
            for ind in range(len(spisok)):
                spisok[ind] = selected(spisok[ind], a, angle)
            for ind in range(len(spisok2)):
                spisok2[ind] = selected(spisok2[ind], a, angle)


if __name__ == "__main__":
    one()
