import math
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

intersect = True


def code(point, x1, x2, y1, y2):
    answer = [0] * 4
    answer[0] = 1 if point[1] > y2 else 0
    answer[1] = 1 if point[0] > x2 else 0
    answer[2] = 1 if point[1] < y1 else 0
    answer[3] = 1 if point[0] < x1 else 0
    return answer


def Or(A, B):
    answer = False
    for i in range(len(A)):
        if A[i] or B[i]:
            answer = True
    return answer


def And(A, B):
    answer = False
    for i in range(len(A)):
        if A[i] and B[i]:
            answer = True
    return answer


def CK(PointA, PointB, PointC, PointD):
    x1, y1 = map(int, PointA.split())
    x2, y2 = map(int, PointB.split())
    a = [int(x) for x in PointC.split()]
    b = [int(x) for x in PointD.split()]
    X = [x1, x1, x2, x2, x1]
    Y = [y1, y2, y2, y1, y1]
    plt.plot(X, Y)
    plt.plot([a[0], b[0]], [a[1], b[1]])
    X_A = []
    Y_A = []
    while True:
        A = code(a, x1, x2, y1, y2)
        B = code(b, x1, x2, y1, y2)
        if Or(A, B) == False:
            print('Внутри')
            X_A = [a[0], b[0]]
            Y_A = [a[1], b[1]]
            plt.scatter(X_A, Y_A)
            break
        elif And(A, B) != False:
            print('Снаружи')
            X_A = [a[0], b[0]]
            Y_A = [a[1], b[1]]
            plt.scatter(X_A, Y_A)
            break
        elif A == [0, 0, 0, 0]:
            b, a = a, b
        elif A[3] != 0:
            a[1] += ((b[1] - a[1]) * (x1 - a[0])) / (b[0] - a[0])
            a[0] = x1
        elif A[2] != 0:
            a[0] += ((b[0] - a[0]) * (y1 - a[1])) / (b[1] - a[1])
            a[1] = y1
        elif A[1] != 0:
            a[1] += ((b[1] - a[1]) * (x2 - a[0])) / (b[0] - a[0])
            a[0] = x2
        elif A[0] != 0:
            a[0] += ((b[0] - a[0]) * (y2 - a[1])) / (b[1] - a[1])
            a[1] = y2
    plt.plot(X_A, Y_A, 'black')
    plt.grid()
    plt.show()


def lenAB(A, B):
    return math.sqrt(pow(A[0] - B[0], 2) + pow(A[1] - B[1], 2))


def CP_calc(a, b, x1, x2, y1, y2, X_A, Y_A):
    A = code(a, x1, x2, y1, y2)
    B = code(b, x1, x2, y1, y2)
    if Or(A, B) == False:
        print('Внутри')
        X_A.append(a[0])
        X_A.append(b[0])
        Y_A.append(a[1])
        Y_A.append(b[1])
        # X_A = [a[0], b[0]]
        # Y_A = [a[1], b[1]]
        # plt.scatter(X_A, Y_A)
        # plt.plot(X_A, Y_A)
        # plt.grid()
        # plt.show()
        return
    elif And(A, B) != False:
        print('Снаружи')
        # X_A = [a[0], b[0]]
        # Y_A = [a[1], b[1]]
        # plt.scatter(X_A, Y_A)
        # plt.plot(X_A, Y_A)
        # plt.grid()
        # plt.show()
        return
    elif lenAB(a, b) < 0.00001:
        print('Длина мала')
        # X_A = [a[0], b[0]]
        # Y_A = [a[1], b[1]]
        # plt.scatter(X_A, Y_A)
        # plt.plot(X_A, Y_A)
        # plt.grid()
        # plt.show()
        return
    else:
        c = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]
        CP_calc(a, c, x1, x2, y1, y2, X_A, Y_A)
        CP_calc(c, b, x1, x2, y1, y2, X_A, Y_A)


def CP(PointA, PointB, PointC, PointD):
    x1, y1 = map(int, PointA.split())
    x2, y2 = map(int, PointB.split())
    a = [int(x) for x in PointC.split()]
    b = [int(x) for x in PointD.split()]
    X = [x1, x1, x2, x2, x1]
    Y = [y1, y2, y2, y1, y1]
    plt.plot(X, Y)
    X_A = []
    Y_A = []
    CP_calc(a, b, x1, x2, y1, y2, X_A, Y_A)
    plt.scatter(X_A, Y_A)
    plt.plot(X_A, Y_A)
    plt.grid()
    plt.show()


def CB(N, PointA, PointB, sides):
    n = int(N)
    # Многоугольник sides,
    X = []
    Y = []
    print(sides)
    for i in sides:
        x, y = map(int, i.split())
        X.append(x)
        Y.append(y)

    t0 = -9999
    t1 = 9999

    # n = 4
    # X = [2, 2, 7, 7]
    # Y = [2, 8, 8, 2]

    X.append(X[0])
    Y.append(Y[0])
    p1 = [int(x) for x in PointA.split()]
    p2 = [int(x) for x in PointB.split()]

    plt.plot(X, Y, 'black')
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'green')
    plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], c='green')

    # Точки входа
    X_Vh = []
    Y_Vh = []
    # Точки выхода
    X_Vy = []
    Y_Vy = []
    global intersect
    intersect = True

    def check(i, j, t0, t1):
        norm = [Y[j] - Y[i], X[i] - X[j]]
        tzn = (p2[0] - p1[0]) * norm[0] + (p2[1] - p1[1]) * norm[1]
        tch = (p1[0] - X[i]) * norm[0] + (p1[1] - Y[i]) * norm[1]

        if tzn == 0:
            if tch > 0:
                global intersect
                intersect = False
                return t0, t1
        # Входящая
        elif tzn < 0:
            t = -1 * tch / tzn
            tmp = [p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t]
            # Добавляем точки входа
            X_Vh.append(tmp[0])
            Y_Vh.append(tmp[1])
            if t > t0:
                t0 = t
        # Выходящая
        elif tzn > 0:
            t = -1 * tch / tzn
            tmp = [p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t]
            # Добавляем точки выхода
            X_Vy.append(tmp[0])
            Y_Vy.append(tmp[1])
            if t < t1:
                t1 = t
        return t0, t1

    newP1 = []
    newP2 = []
    t0, t1 = check(0, n - 1, t0, t1)
    for i in range(n - 1, 0, -1):
        t0, t1 = check(i, i - 1, t0, t1)

    # Прямая частично или полностью в многоугольнике
    if t0 <= t1:
        if t0 < 0:
            newP1.append(p1[0])
            newP1.append(p1[1])
        else:
            newP1.append(p1[0] + (p2[0] - p1[0]) * t0)
            newP1.append(p1[1] + (p2[1] - p1[1]) * t0)
        if t1 > 1:
            newP2.append(p2[0])
            newP2.append(p2[1])
        else:
            newP2.append(p1[0] + (p2[0] - p1[0]) * t1)
            newP2.append(p1[1] + (p2[1] - p1[1]) * t1)
        if t0 < 0 and t1 > 1:
            print("Внутри")
        # Рисование искомого отрезка
        plt.plot([newP1[0], newP2[0]], [newP1[1], newP2[1]], 'red')
        if intersect:
            list_X = []
            list_Y = []
            list1_X = []
            list1_Y = []
            if newP1[0] == newP2[0] and newP1[1] == newP2[1]:
                list1_X.append(newP1[0])
                list1_Y.append(newP1[1])
                plt.plot(list1_X, list1_Y, 'red')
                plt.scatter(list1_X, list1_Y)
            else:
                list_X.append(newP1[0])
                list_Y.append(newP1[1])
                list_X.append(newP2[0])
                list_Y.append(newP2[1])
                plt.scatter(list_X, list_Y)
        else:
            print("Снаружи")
    else:
        print("Снаружи")

    # Рисуем все входящие и покидающие точки
    plt.scatter(X_Vh, Y_Vh, c='blue')
    plt.scatter(X_Vy, Y_Vy, c='orange')

    plt.axis('equal')
    plt.grid()
    plt.show()


def button_clicked():
    if choice.get() == 1:
        pointA = simpledialog.askstring(title="Введите данные", prompt='Координаты левого нижнего угла окна: ')
        if pointA is None:
            root.destroy()
            return
        pointB = simpledialog.askstring(title="Введите данные", prompt='Координаты правого верхнего угла окна:')
        if pointB is None:
            root.destroy()
            return
        pointC = simpledialog.askstring(title="Введите данные", prompt='Точка A: ')
        if pointC is None:
            root.destroy()
            return
        pointD = simpledialog.askstring(title="Введите данные", prompt='Точка B: ')
        if pointD is None:
            root.destroy()
            return
        CK(pointA, pointB, pointC, pointD)
    elif choice.get() == 2:
        pointA = simpledialog.askstring(title="Введите данные", prompt='Координаты левого нижнего угла окна: ')
        if pointA is None:
            root.destroy()
            return
        pointB = simpledialog.askstring(title="Введите данные", prompt='Координаты правого верхнего угла окна:')
        if pointB is None:
            root.destroy()
            return
        pointC = simpledialog.askstring(title="Введите данные", prompt='Точка A: ')
        if pointC is None:
            root.destroy()
            return
        pointD = simpledialog.askstring(title="Введите данные", prompt='Точка B: ')
        if pointD is None:
            root.destroy()
            return
        CP(pointA, pointB, pointC, pointD)
    elif choice.get() == 3:
        n = simpledialog.askstring(title="Введите данные", prompt='Введите количество вершин многоугольника: ')
        if n is None:
            root.destroy()
            return
        sides = []
        for i in range(int(n)):
            point = simpledialog.askstring(title="Введите данные", prompt=f'Вершина {i + 1}: ')
            if point is None:
                root.destroy()
                return
            sides.append(point)
        pointA = simpledialog.askstring(title="Введите данные", prompt='Точка P1: ')
        if pointA is None:
            root.destroy()
            return
        pointB = simpledialog.askstring(title="Введите данные", prompt='Точка P2: ')
        if pointB is None:
            root.destroy()
            return
        CB(n, pointA, pointB, sides)
    else:
        messagebox.showinfo("Неправильный выбор", "Выберите задачу")


if __name__ == '__main__':
    root = Tk()
    root.title("Отсечение отрезка многоугольником")
    root.geometry(f'250x120+{root.winfo_screenwidth()//2-125}+{root.winfo_screenheight()//2-60}')

    choice = IntVar()
    choice.set(0)
    lineCheckButton = Radiobutton(text="Алгоритм Цируса-Бека", variable=choice, value=1)
    lineCheckButton.grid(row=0, column=0, sticky=W)

    circleCheckButton = Radiobutton(text="Алгоритм Сазерленда-Коэна", variable=choice, value=2)
    circleCheckButton.grid(row=1, column=0, sticky=W)

    circleCheckButton = Radiobutton(text="Алгоритм средней точки", variable=choice, value=3)
    circleCheckButton.grid(row=2, column=0, sticky=W)

    btn = Button(text="Решить", command=button_clicked)
    btn.grid(row=3, column=0, sticky=W)

    root.mainloop()
