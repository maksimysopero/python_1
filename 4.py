#Построение диаграммы для категориальных данных

import matplotlib.pyplot as plt
import numpy as np

fruits = ["apple", "peach", "orange", "bannana", "melon"] # Список № 1
counts = [34, 25, 43, 31, 17] # Список № 2

plt.bar(fruits, counts)  
plt.title("Fruits!") 
plt.xlabel("Fruit")  # Ось Y
plt.ylabel("Count" ) # Ось X

plt.show()