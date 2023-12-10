import numpy as np
import matplotlib.pyplot as plt

def LisaguCurve(t, A, B, a, b, delta):
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)
    return x, y


A = 1
B = 1
delta = np.pi / 2


frequencies = [(3, 2), (3, 4), (5, 4), (5, 6)]


fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Фигуры Лисажу')

for i, (a, b) in enumerate(frequencies):
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = LisaguCurve(t, A, B, a, b, delta)

    row = i // 2
    col = i % 2
    axs[row, col].plot(x, y, label=f'{a}:{b}')
    axs[row, col].set_title(f'Соотношение частот: = {a}:{b}')
    axs[row, col].axis('equal')
    axs[row, col].grid(True)
    axs[row, col].legend()

plt.show()