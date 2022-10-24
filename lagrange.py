import numpy as np


def funct(x):
    func17 = 2 * np.exp(np.cbrt(x / 3) * np.cos(4 * x))
    return func17


def lagrange(n, point, a, b):
    value = 0
    x = np.zeros(n)
    l = np.zeros(n)

    for i in range(n):
        x[i] = a + i * ((b - a) / 4)
    for i in range(n):
        l[i] = 1
        for j in range(n):
            if j != i:
                l[i] *= (point - x[j]) / (x[i] - x[j])
        value += funct(x[i]) * l[i]
    return value

    # """
    # n = len(x)
    # if y is None:
    #     y = np.zeros(n)
    #     for i in range(n):
    #         y[i] = self.func(x[i])
    # interp = 0
    # l = np.zeros(n)
    # for i in range(n):
    #     l[i] = 1
    #     for k in range(n):
    #         if k != i:
    #             l[i] *= (approx - x[k]) / (x[i] - x[k])
    #     interp += y[i] * l[i]
    # return interp
    # """
