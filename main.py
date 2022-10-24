# Контрольная по численным методам
# Стрыгина Валерия Михайловна, группа 05-005
# 17 вариант

import numpy as np
import lagrange as l


# основная часть программы

print("Полином Лагранжа вычисляется по следующей формуле: ")
print("sum[n,k=1]( f(x_k) * l_k(x)), где l_x(x) = mult[n,j=1]( (x-x_j) / (x_k-x_j) )")

select = int(input("Выберите точку для аппроксимации: 1 - 0.095п, 2 - 0.18п , 3 - 0.42п\n"))
if select == 1:
    x = 0.095*np.pi
elif select == 2:
    x = 0.18*np.pi
elif select == 3:
    x = 0.42*np.pi
lagrangeres = l.lagrange(5, x, 0, (2*np.pi)/3)
calculated = 2 * np.exp(np.cbrt(x / 3) * np.cos(4 * x))
print("Результат интерполирования: ", lagrangeres)
print("Результат вычисления: ", calculated)
print("Погрешность: ", l.mape(calculated,lagrangeres))