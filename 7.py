import numpy as np
import matplotlib.pyplot as plt

# Исходник

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]

# Регулирования размера

plt.figure(figsize=(12, 7))

# Вывод графика

plt.subplot(2, 2, 1)
plt.plot(x, y1, '-')

plt.subplot(2, 2, 2)
plt.plot(x, y2, '--')

plt.subplot(2, 2, 3)
plt.plot(x, y3, '-.')

plt.subplot(2, 2, 4)
plt.plot(x, y4, ':')
plt.show()

# . Функция subplots() возвращает
#два объекта, первый – это Figure, подложка, на которой будут размещены поля с
#графиками, второй – объект или массив объектов Axes, через которые можно получить
#полных доступ к настройке внешнего вида отображаемых элементов

fig, axs = plt.subplots(2, 2, figsize=(12, 7))
axs[0, 0].plot(x, y1, '-')
axs[0, 1].plot(x, y2, '--')
axs[1, 0].plot(x, y3, '-.')
axs[1, 1].plot(x, y4, ':')
plt.show()
