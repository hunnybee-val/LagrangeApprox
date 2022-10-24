import numpy as np

def funct(x):
    func17 = 2 * np.exp(np.cbrt(x / 3) * np.cos(4 * x))
    return func17


def x_k(a, b, k):
    return a + k((b - a) / 4)


def lagrange(n, x, a, b):
    value = 0
    points = np.zeros(n)
    l = np.zeros(n)

    for i in range(n):
        l[i] = 1
        points[i] = a + i((b - a) / 4)
        for j in range(n):
            if j != i:
                l[i] = (x - x_k(a,b,j)) / (x_k(a,b,i) - x_k(a,b,j))
        value += funct()
    return l

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
