import numpy as np

# функция в 17 варианте
def funct(x):
    func17 = 2 * np.exp(np.cbrt(x / 3) * np.cos(4 * x))
    return func17

#первый способ задания точек

def x_data1(a, b, n):
    x = np.zeros(n)
    for i in range(n):
        x[i] = a + i * ((b - a) / 4)
    return x

#второй способ задания точек

def x_data2(a, b, n):
    x = np.zeros(n+1)
    for i in range(1,n+1):
        x[i] = ((b - a) / 2)*np.cos((2*i-1)*np.pi/10)+(b+a)/2
    return x

# интерполяционный полином Лагранжа

def lagrange(n, point, a, b, oneortwo):
    value = 0
    if oneortwo == 1:
        x = x_data1(a, b, n)
    else:
        x = x_data2(a, b, n)
    l = np.zeros(n)

    for i in range(n):
        l[i] = 1
        for j in range(n):
            if j != i:
                l[i] *= (point - x[j]) / (x[i] - x[j])
        value += funct(x[i]) * l[i]
    return value


# Интерполяционный полином в форме Ньютона
# Разностные отношения

def div_diff(a, b, n):
    x = x_data1(a, b, n)
    y = np.zeros(n)
    for i in range(n):
        y[i] = funct(x[i])
    coef = np.zeros([n,n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = \
                (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef

def newton_poly(x, n, a, b):
    x_points = x_data1(a, b, n)
    coef = div_diff(a,b,n)[0, :]
    p = coef[n-1]
    for k in range(1,n+1):
        p = coef[n - k] + (x - x_points[n - k]) * p
    return p

#Интерполяционный полином в форме Эрмита-Фейера

def hermite(x,n):
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*hermite(x,n-1)-2*(n-1)*hermite(x,n-2)

# n=5
# for i in range (n):
#     print("переменная: ", x_data1(0,2 * np.pi / 3,5)[i])
#     print("значение: ", funct(x_data1(0, 2 * np.pi / 3, 5)[i]))