import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def moveX(a, n):
    return [a[0] + n, a[1]]


def moveY(a, n):
    return [a[0], a[1] + n]


def reflection(a):
    a.reverse()


def reflectionOX(a):
    a[1] = -a[1]


def reflectionOY(a):
    a[0] = -a[0]


def correct_angle(a, b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    if -x + y <= 0:
        return True
    else:
        return False


def line(a, b):
    A = [a[0], b[0]]
    B = [a[1], b[1]]
    oper = []

    ###############################Геом преобразования###############################
    if a[0] != 0 or a[1] != 0:
        dx = -a[0]
        dy = -a[1]
        a = moveX(a, dx)
        b = moveX(b, dx)
        a = moveY(a, dy)
        b = moveY(b, dy)
        oper.append({'move': (dx, dy)})

    # Если точка находится в 3/4
    if a[1] < 0 or b[1] < 0:
        reflectionOX(a)
        reflectionOX(b)
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
        oper.append({'yx': 0})

    ###############################Алгоритм###############################
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

    return xEnd, yEnd


def count_to_dict(lst):
    return {k: lst.count(k) for k in lst}


def button_clicked():
    n = n_entry.get()
    if n == '':
        messagebox.showerror("Некорректные данные", "Введите данные еще раз")
        n_entry.delete(0, END)
        return
    n = int(n)
    X = []
    N = 100
    for i in range(N):
        X.extend([i] * N)
    Y = [int(i) for i in range(N)] * N
    C = ['g' for i in range(N)] * N
    x = []
    y = []
    for i in range(int(n)):
        point = simpledialog.askstring(title="Введите данные", prompt=f'Вершина {i + 1}: ')
        if point is None:
            root.destroy()
            return
        point = point.split()
        x.append(int(point[0]))
        y.append(int(point[1]))
    centreX = min(x) + ((max(x) - min(x)) // 2)
    print(centreX)
    x.append(x[0])
    y.append(y[0])
    xA = []
    yA = []
    t = []
    for i in range(n):
        a = [x[i], y[i]]
        b = [x[i + 1], y[i + 1]]
        xEnd, yEnd = line(a, b)
        xA.extend(xEnd)
        yA.extend(yEnd)
        k = 0
        while k < (len(yEnd) - 1):
            if yEnd[k] == yEnd[k + 1]:
                if abs(xEnd[k] - centreX) < abs(xEnd[k + 1] - centreX):
                    xEnd.remove(xEnd[k])
                    yEnd.remove(yEnd[k])
                    k -= 1
                else:
                    xEnd.remove(xEnd[k + 1])
                    yEnd.remove(yEnd[k + 1])
                    k -= 1
            k += 1
        for j in range(len(yEnd)):
            startX = min(xEnd[j], centreX)
            endX = max(xEnd[j], centreX)
            for currentX in range(startX, endX):
                try:
                    ind = t.index((currentX, yEnd[j]))
                    t.remove(t[ind])
                except ValueError:
                    t.append((currentX, yEnd[j]))
    for point in t:
        xA.append(point[0])
        yA.append(point[1])
    plt.scatter(X, Y, c='g')
    plt.scatter(xA, yA, c='r')
    plt.show()
    messagebox.showinfo("Решение построено", "Готово!")
    n_entry.delete(0, END)


def button_clicked1(event):
    button_clicked()


if __name__ == '__main__':
    root = Tk()
    root.title("XOr-2 с перегородкой")
    root.geometry(f'250x120+{root.winfo_screenwidth() // 2 - 125}+{root.winfo_screenheight() // 2 - 60}')
    root.bind("<Return>", button_clicked1)

    n_label = Label(text='Количество вершин: ')
    n_entry = Entry()

    btn = Button(text="Решить", command=button_clicked)

    n_label.pack()
    n_entry.pack()
    btn.pack()

    root.mainloop()
    # n = int(input('Количество вершин: '))
