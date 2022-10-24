import numpy as np

# функция в 17 варианте
def funct(x):
    func17 = 2 * np.exp(np.cbrt(x / 3) * np.cos(4 * x))
    return func17

def x_data(a,b,n):
    x = np.zeros(n)
    for i in range(n):
        x[i] = a + i * ((b - a) / 4)
    return x

# интерполяционный полином Лагранжа

def lagrange(n, point, a, b):
    value = 0
    x = x_data(a,b,n)
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
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = a + i * ((b - a) / 4)
        y[i] = funct(x[i])
    coef = np.zeros([n,n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = \
                (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef

def newton_poly(x, n, a, b):
    x_points = x_data(a,b,n)
    n = len(x_points) - 1
    coef = div_diff(a,b,n)[0, :]
    p = coef[n-1]
    for k in range(n):
        p = coef[n-k-1] + (x -x_points[n-k])*p
    return p


def mape(actual, pred):
    actual, pred = np.array(actual), np.array(pred)
    return np.mean(np.abs((actual - pred) / actual)) * 100
