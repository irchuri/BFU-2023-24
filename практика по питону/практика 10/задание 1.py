import numpy as np
from scipy import special
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 1000)

for n in range(1, 8):
    y = special.legendre(n)(x)
    plt.plot(x, y, label=f'P_{n}(x)')

plt.title('Полиномы Лежандра')
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.legend()
plt.grid(True)
plt.show()