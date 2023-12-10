import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def MSE_Calculation(x, y):
    return np.square(x - y).mean()

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(2 * np.pi * X) * np.cos(2 * np.pi * Y) 

MSEvalues = np.zeros_like(Z)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        MSEvalues[i, j] = MSE_Calculation(Z[i, j], np.zeros_like(Z[i, j]))


fig = plt.figure(figsize=(10, 5))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, MSEvalues)
ax1.set_title('Среднеквадратичное отклонение')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, MSEvalues)
ax2.set_title('Среднеквадратичное отклонение \n(с логарифмическим масштабом)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('MSE')
ax2.set_zscale('log')   

plt.tight_layout()
plt.show()