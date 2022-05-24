import matplotlib.pyplot as plt
import time


def rotate(a, b, c):
    return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])


def graham_scan(a):
    n = len(a)    # число точек
    p = list(range(n))  # список номеров точек
    for i in range(1, n):
        if a[p[i]][0] < a[p[0]][0]:   # если p[i]-ая точка лежит левее p[0]-ой точки
            p[i], p[0] = p[0], p[i]   # меняем местами номера этих точек
    for i in range(2, n):     # сортировка вставкой
        j = i
        while j > 1 and (rotate(a[p[0]], a[p[j-1]], a[p[j]]) < 0):
            p[j], p[j-1] = p[j-1], p[j]
            j -= 1
    S = [p[0], p[1]]  # создаем стек
    for i in range(2, n):
        while rotate(a[S[-2]], a[S[-1]], a[p[i]]) < 0:
            del S[-1]
        S.append(p[i])
    return S


if __name__ == '__main__':
    points = [[1, 1], [2, 2], [3,3], [4, 4], [5, 5]]
    g = graham_scan(points)
    print(g)
    x = list()
    y = list()
    xp = list()
    yp = list()
    for i in range(len(points)):
        xp.append(points[i][0])
        yp.append(points[i][1])
    for i in g:
        print(points[i])
        x.append(points[i][0])
        y.append(points[i][1])
        plt.plot(x, y, c='r')
        plt.scatter(xp, yp, c='b')
        plt.scatter(x, y, c='b')
        plt.show()
        time.sleep(1)
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, c='r')
    plt.scatter(xp, yp, c='b')
    plt.scatter(x, y, c='b')
    plt.show()
