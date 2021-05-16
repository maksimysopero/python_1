# Построение графика 

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = x

plt.title("Линейная зависимость y = x")   
plt.xlabel("x")                           # Ось x
plt.ylabel("y")                           # Ось y
plt.grid()                                # Визуал сетки
plt.plot(x, y, "r--")                     # Настройка графика,  (r - красный цвет, "-" это пунктирная линия.)
plt.show()