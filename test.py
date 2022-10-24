import numpy as np

n = 5
a = 2
b = 32
points = np.zeros(n)
l = np.zeros(n)

for i in range(n):
    l[i] = 1
    points[i] = a + i * ((b - a) / 4)
    print(points[i])

