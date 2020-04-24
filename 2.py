#Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на екран значення коріння і квадратів кожного з елементів масиву.
#Вишневський А.В 122Д
import numpy as np
import math
n = 5
x = np.zeros((n), dtype=int)
k = 0
for i in range(n):
    x[i] = int(input(f'Вв {i+1} елементи масиву: '))
    print(f'Ваш sqrt: {math.sqrt(x[i])}')
    print(f'Your square: {x[i]**2}')
print(x)
