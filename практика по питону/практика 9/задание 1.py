import numpy as np

with open ('matrix.txt') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]

matrix = np.array(matrix)
print('Матрица:')
print(matrix)
print(f'Минимальный элемент: {matrix.min()}')
print(f'Максимальный элемент: {matrix.max()}')
print(f'Сумма элементов: {matrix.sum()}')

