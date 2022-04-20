from .line import *
from .circle import *

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def button_clicked():
    if choice.get() == 1:
        pointA = simpledialog.askstring(title="Введите данные", prompt="Введите точку А:")
        if pointA is None:
            root.destroy()
            return
        pointB = simpledialog.askstring(title="Введите данные", prompt="Введите точку B:")
        if pointB is None:
            root.destroy()
            return
        line(pointA, pointB)
    elif choice.get() == 2:
        center = simpledialog.askstring(title="Введите данные", prompt="Введите центр окружности:")
        if center is None:
            root.destroy()
            return
        r = simpledialog.askstring(title="Введите данные", prompt="Введите радиус:")
        if r is None:
            root.destroy()
            return
        circle(center, r)
    else:
        messagebox.showinfo("Неправильный выбор", "Выберите задачу")


if __name__ == '__main__':

    root = Tk()
    root.title("Алгоритмы Брезенхема растеризации отрезка и окружности")
    root.geometry("300x100+1000+500")

    choice = IntVar()
    choice.set(0)
    lineCheckButton = Radiobutton(text="Линия/отрезок", variable=choice, value=1)
    lineCheckButton.grid(row=0, column=0, sticky=W)

    circleCheckButton = Radiobutton(text="Окружность", variable=choice, value=2)
    circleCheckButton.grid(row=1, column=0, sticky=W)

    btn = Button(text="Решить", command=button_clicked)
    btn.grid(row=2, column=0, sticky=W)

    root.mainloop()
