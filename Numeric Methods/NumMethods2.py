import math
import numpy

from tkinter import *
from tkinter import messagebox


# 1-ое уравнение системы
def first(x, y):
    return math.cos(y-1) + x - 0.8


# 2-ое уравнение системы
def second(x, y):
    return y - math.cos(x) - 2


# производная первого по х
def derivative_first_x(x, y):
    return 1


# производная первого по у
def derivative_first_y(x, y):
    return -math.sin(y-1)


# производная второго по х
def derivative_second_x(x, y):
    return math.sin(x)


# производная второго у
def derivative_second_y(x, y):
    return 1


# построение обратной матрицы
def inverse_matrix(a):
    det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    aa = a[0][0]
    a[0][0] = a[1][1] / det
    a[1][1] = aa / det
    aa = a[0][1]
    a[0][1] = -a[1][0] / det
    a[1][0] = -aa / det
    a[1][0], a[0][1] = a[0][1], a[1][0]


def method(x, y):
    eps = 0.001
    count = 0
    a = numpy.zeros((2, 2))
    px, py, dx, dy = 0, 0, 0, 0
    while True:
        count += 1
        px = x
        py = y
        # составляем матрицу Якоби
        a[0][0] = derivative_first_x(x, y)
        a[0][1] = derivative_first_y(x, y)
        a[1][0] = derivative_second_x(x, y)
        a[1][1] = derivative_second_y(x, y)
        # W^-1
        inverse_matrix(a)
        # W^-1(X_k)(F(X_k))
        dx = a[0][0]*first(x, y) + a[0][1]*second(x, y)
        dy = a[1][0]*first(x, y) + a[1][1]*second(x, y)
        # точки пересечния
        x = x - dx
        y = y - dy

        flag = True
        try:
            if (math.fabs(x - px) + math.fabs(y - py)) / (math.fabs(px) + math.fabs(py)) > eps:
                flag = False
        except ZeroDivisionError:
            messagebox.showerror("Ошибка решения", "Деление на ноль")
            return None, None, None

        if flag:
            return x, y, count


# обработчик нажатия кнопки
def button_clicked():
    x = x_input.get()
    y = y_input.get()
    if x == '' and y == '':
        messagebox.showerror("Некорректные данные", "Введите данные еще раз")
        x_input.delete(0, END)
        y_input.delete(0, END)
        return
    x, y, count = method(float(x), float(y))
    if not (x is None and y is None and count is None):
        messagebox.showinfo("Ответ", f'x = {x}\n y = {y}\n steps = {count}')
    x_input.delete(0, END)
    y_input.delete(0, END)


if __name__ == '__main__':

    root = Tk()
    root.title("Решение нелинейных уравнений методом Ньютона")
    root.geometry(f'300x100+{root.winfo_screenwidth()//2-150}+{root.winfo_screenheight()//2-50}')

    f_top = Frame(root)
    f_bottom = Frame(root)
    x_label = Label(f_top, text="x = ")
    x_input = Entry(f_top)
    y_label = Label(f_bottom, text="y = ")
    y_input = Entry(f_bottom)
    btn = Button(text="Решить", command=button_clicked)
    f_top.pack()
    f_bottom.pack()
    x_label.pack(side=LEFT)
    y_label.pack(side=LEFT)
    x_input.pack(side=RIGHT)
    y_input.pack(side=RIGHT)
    btn.pack()

    root.mainloop()
