# 4. В пространстве. Даны три точки А, В, С, D своими координатами, найти
# уравнение плоскости проходящей через точку D и параллельную плоскости АВС.

def OnOneLine():
    a = (cx - ax) * (by - ay) * (bz - az)
    b = (cy - ay) * (bx - ax) * (bx - az)
    c = (cz - az) * (bx - ax) * (by - ay)
    return a == b and a == c and b == c

def EquationP():
    equation = []
    a = ay * (bz - cz) + by * (cz - az) + cy * (az - bz)
    b = az * (bx - cx) + bz * (cx - ax) + cz * (ax - bx)
    c = ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)
    d = -(ax * (by * cz - cy * bz) + bx * (cy * az - ay * cz) + cx * (ay * bx - by * az))
    equation.append(a)
    equation.append(b)
    equation.append(c)
    equation.append(d)
    return equation


ax = float(input('Ax = '))
ay = float(input('Ay = '))
az = float(input('Az = '))

bx = float(input('Bx = '))
by = float(input('By = '))
bz = float(input('Bz = '))

cx = float(input('Cx = '))
cy = float(input('Cy = '))
cz = float(input('Cz = '))

dx = float(input('Dx = '))
dy = float(input('Dy = '))
dz = float(input('Dz = '))

if not OnOneLine():
    equation = EquationP()
    print(f'Плоскость АВС = {equation[0]}x + {equation[1]}y + {equation[2]}z + {equation[3]} = 0')
    equation[3] = equation[0] * dx + equation[1] * dy + equation[2] * dz
    print(f'Плоскость проведена через точку D({dx};{dy};{dz})'
          f'и параллельную плоскости ABC {equation[0]}x + {equation[1]}y + {equation[2]}z + {equation[3]} = 0')
else:
    print('Точки лежат на одной прямой')