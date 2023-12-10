import numpy as np
import numpy.random

massiv = numpy.random.normal(1, 5, size=(10,4))
new_var = massiv[:4]
print('Матрица:')
print(massiv)
print(f'Минимальное значение: {massiv.min()}')
print(f'Максимальное значение: {massiv.max()}')
print(f'Среднее значение: {massiv.mean()}')
print(f'Стандартное отклонение: {massiv.std()}')
print('Первые пять строк:')
print(new_var) 