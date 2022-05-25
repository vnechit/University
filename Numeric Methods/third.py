import math


a = 0
b = 1
c = 2
d = 3
m = 15
eps = 0.001


def function(t, x) -> float:
    return math.pow(math.e, (math.sqrt(t)/(1+x*x)))


def doubling(t) -> str:
    n = 3
    previous_value = -1
    current_value = 0
    while math.fabs(current_value - previous_value) >= eps:
        x = a
        n *= 2
        h = (b - a) / n
        previous_value = current_value
        current_value = 0
        current_value += (function(t, a) + function(t, b)) / 2
        x += h
        for i in range(1, n):
            current_value += function(t, x)
            x += h
        current_value *= h
    return f'Удвоение числа шагов N={n}, значение - {current_value}'


def gauss(t) -> str:
    nodes3answer = 0
    nodes4answer = 0
    nodes3 = [
        [
            -0.774596669,   # Xi
            0,
            0.774596669,
        ],
        [
            0.5555555555556,    # Ci
            0.8888888888889,
            0.555555556,
        ],
    ]
    nodes4 = [
        [
            -0.861136312,  # Xi
            - 0.339981044,
            0.339981044,
            0.861136312
        ],
        [
            0.347854845,   # Ci
            0.652145155,
            0.652145155,
            0.347854845
        ],
    ]
    # Гаусс при 3-ех узлах
    for i in range(3):
        # второй аргумент в функции это ui=(b-a)/2*xi + (b+a)/2
        nodes3answer += nodes3[1][i] * function(t, ((b-a) / 2 * nodes3[0][i] + (b + a) / 2))
    # домножаем на константу (b - a) / 2 , вынесенную за знак суммы
    nodes3answer *= (b - a) / 2
    # Гаусс при 4-ех узлах
    for i in range(4):
        nodes4answer += nodes4[1][i] * function(t, ((b - a) / 2 * nodes4[0][i] + (b + a) / 2))
    nodes4answer *= (b - a) / 2
    return f'Гаусс при 3-ех узлах, значение - {nodes3answer}\nГаусс при 4-ех узлах, значение - {nodes4answer}\n'


if __name__ == '__main__':
    tau = (d - c) / m
    t_j = c
    while t_j <= d + 0.01:
        print(f'При t = {t_j}\n{doubling(t_j)}\n{gauss(t_j)}')
        t_j += tau
