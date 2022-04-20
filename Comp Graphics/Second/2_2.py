import math
import time

from tkinter import *  # подключаем графическую библиотеку tkinter

root = Tk()
canvas = Canvas(root, width=500, height=550)  # инициализация холста 500х500
canvas.pack()  # размещаем холст в нашем окне
canvas.create_oval(10, 10, 490, 490, fill="white")  # циферблат  просто круг

i = 0  # счетчик цикла
while i < 60:  # цикл вывода секундных рисочек
    i = i + 1
    canvas.create_line(250 + 210 * math.cos(-i * 6 * math.pi / 180 + math.pi / 2),
                       250 - 210 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                       250 + 190 * math.cos(-6 * i * math.pi / 180 + math.pi / 2),
                       250 - 190 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                       width=2)
    if i % 5 == 0:  # когда i кратно 5 выводим более жирную рисочку для обозначения часов
        canvas.create_line(250 + 215 * math.cos(-i * 6 * math.pi / 180 + math.pi / 2),
                           250 - 215 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                           250 + 190 * math.cos(-6 * i * math.pi / 180 + math.pi / 2),
                           250 - 190 * math.sin(-6 * i * math.pi / 180 + math.pi / 2),
                           width=4)
        continue
i = 0
while i < 12:  # цикл вывода цифр часов
    i += 1
    canvas.create_text(250 + 225 * math.cos(-i * 30 * math.pi / 180 + math.pi / 2),
                       250 - 225 * math.sin(-30 * i * math.pi / 180 + math.pi / 2),
                       text=i, font=('Arial', 16))

i = 950  # счетчик цикла  и координата х для вывода текста бегущей строки
while 1:  # основной бесконечный цикл
    time_now = time.localtime()  # получаем текущее время в виде
    # time.struct_time(tm_year=2016, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=23, tm_sec=35, tm_wday=6, tm_yday=87, tm_isdst=0)
    time_sec = int(time.strftime("%S", time_now))  # получаем секунды из переменной time_now
    time_hour = int(time.strftime("%I", time_now))  # получаем часы из переменной time_now
    time_min = int(time.strftime("%M", time_now))  # получаем минуты из переменной time_now
    sec_angle = 6 * time_sec  # угол отклонения секундной стрелки за 1 секунду
    min_angle = time_min * 6 + time_sec * 0.1  # угол отклонения минутной стрелки за 1 секунду
    hour_angle = time_hour * 30 + time_min * 60 * (30 / 3600)  # угол отклонения часовой стрелки за 1 секунду

    # рисуем минутную стрелку
    line_min = canvas.create_line(250,
                                  250,
                                  250 - 180 * math.cos(min_angle * math.pi / 180 + math.pi / 2),
                                  250 - 180 * math.sin(min_angle * math.pi / 180 + math.pi / 2),
                                  width=3, fill='darkblue')
    # рисуем часовую стрелку
    line_hour = canvas.create_line(250,
                                   250,
                                   250 - 150 * math.cos(hour_angle * math.pi / 180 + math.pi / 2),
                                   250 - 150 * math.sin(hour_angle * math.pi / 180 + math.pi / 2),
                                   width=5, fill='darkblue')
    # рисуем секундную стрелку
    line_sec = canvas.create_line(250,
                                  250,
                                  250 - 180 * math.cos(sec_angle * math.pi / 180 + math.pi / 2),
                                  250 - 180 * math.sin(sec_angle * math.pi / 180 + math.pi / 2),
                                  width=2, fill='red')
    i = i - 0.5
    if i == -600:
        i = 950
    root.update()  # обновляем экран/холст
    canvas.delete(line_sec)  # удаляем секундную стрелку
    canvas.delete(line_min)  # удаляем минутную стрелку
    canvas.delete(line_hour)  # удаляем часовую стрелку

root.mainloop  # создаем постоянный цикл
