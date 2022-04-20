# 2. На плоскости. Даны три точки А, В, С, лежащие на одной прямой.
# Определить расположение точки С относительно
# отрезка АВ (между точками А и В, вне отрезка
# за точкой А, вне отрезка за точкой В).

import math
from .Point import *


a = Point.Point()
b = Point.Point()
c = Point.Point()

if c.distance(a) + c.distance(b) > a.distance(b):
    if c.distance(a) < c.distance(b):
        print('Вне отрезка за точкой А')
    else:
        print('Вне отрезка за точкой B')
else:
    print('На отрезке')














# if a.x == b.x and b.x == c.x and a.y == b.y and b.y == c.y:
#     print('Точки одинаковы')
# elif a.distance(c) + c.distance(b) == a.distance(b):
#     print('Точка С между точками А и В')
#     exit()
# elif a.x == b.x:
#     if c.y < a.x:
#         print('Точка С перед точкой А')
#         exit()
#     else:
#         print('Точка С после точки В')
#         exit()
# elif c.x < a.x:
#     print('Точка С перед точкой А')
#     exit()
# else:
#     print('Точка С после В')
#     exit()
