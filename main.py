# Контрольная по численным методам
# Стрыгина Валерия Михайловна, группа 05-005
# 17 вариант

import numpy as np
import lagrange as p


# основная часть программы

a = 0
b = 2 * np.pi / 3
x = 1

print("Полином Лагранжа вычисляется по следующей формуле: ")
print("sum[n,k=1]( f(x_k) * l_k(x)), где l_x(x) = mult[n,j=1]( (x-x_j) / (x_k-x_j) )")

select = int(input("Выберите точку для аппроксимации: 1 - 0.095п, 2 - 0.18п , 3 - 0.42п\n"))
if select == 1:
    x = 0.095*np.pi
elif select == 2:
    x = 0.18*np.pi
elif select == 3:
    x = 0.42*np.pi
lagrangeres = p.lagrange(5, x, a, b, 1)
calculated = 2 * np.exp(np.cbrt(x / 3) * np.cos(4 * x))
newton_form = p.newton_poly(x, 5, a, b)
print("Результат интерполирования: ", lagrangeres)
print("В форме Ньютона: ", newton_form)
print("Результат вычисления: ", calculated)
print("Погрешность: ", p.mape(calculated, lagrangeres))