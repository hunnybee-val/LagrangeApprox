# Контрольная по численным методам
# Стрыгина Валерия Михайловна, группа 05-005
# 17 вариант

import numpy as np
import numpy.polynomial.polynomial as poly
def Func(x):
    func17 = 2 * np.exp(np.cbrt(x/3) * np.cos(4 * x))
    return func17
def Polynome(a, b):



    """
    n = len(x)
    if y is None:
        y = np.zeros(n)
        for i in range(n):
            y[i] = self.func(x[i])
    interp = 0
    l = np.zeros(n)
    for i in range(n):
        l[i] = 1
        for k in range(n):
            if k != i:
                l[i] *= (approx - x[k]) / (x[i] - x[k])
        interp += y[i] * l[i]
    return interp
    """

#основная часть программы

print("Полином Лагранжа вычисляется по следующей формуле: ")
print("sum[n,k=1]( f(x_k) * l_k(x)), где l_x(x) = mult[n,j=1]( (x-x_j) / (x_k-x_j) )")