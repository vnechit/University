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


def method(x, y, eps):
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
            nevyazka = [math.cos(y-1)+x-0.8, y-math.cos(x)-2]
            return x, y, count, nevyazka


# обработчик нажатия кнопки
def button_clicked():
    x = x_input.get()
    y = y_input.get()
    eps = eps_input.get()
    if x == '' or y == '':
        messagebox.showerror("Некорректные данные", "Введите данные еще раз")
        x_input.delete(0, END)
        y_input.delete(0, END)
        eps_input.delete(0, END)
        return
    x, y, count, nevyazka = method(float(x), float(y), float(eps))
    if not (x is None and y is None and count is None):
        messagebox.showinfo("Ответ", f'x = {x}\n y = {y}\n steps = {count}\nМатрица невязки:\n{nevyazka[0]}\n{nevyazka[1]}')
    x_input.delete(0, END)
    y_input.delete(0, END)
    eps_input.delete(0, END)


if __name__ == '__main__':

    root = Tk()
    root.title("Решение нелинейных уравнений методом Ньютона")
    root.geometry(f'250x130+{root.winfo_screenwidth()//2-125}+{root.winfo_screenheight()//2-65}')

    x_label = Label(text="x = ")
    x_input = Entry()

    y_label = Label(text="y = ")
    y_input = Entry()

    eps_label = Label(text="eps = ")
    eps_input = Entry()

    btn = Button(text="Решить", command=button_clicked)

    x_label.grid(column=0, row=0)
    y_label.grid(column=0, row=1)
    eps_label.grid(column=0, row=2)

    x_input.grid(column=1, row=0)
    y_input.grid(column=1, row=1)
    eps_input.grid(column=1, row=2)

    btn.grid(column=1, row=3)

    root.mainloop()
