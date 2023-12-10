import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

def LisaguCurve(t, A, B, a, b, delta):
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)
    return x, y

def update(frame):
    plt.clf()
    ax = plt.gca()

    ratio = frame / frames
    a = 1
    b = ratio

    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = LisaguCurve(t, A, B, a, b, delta)

    ax.plot(x, y, label=f'a/b = {a}/{b}')
    ax.set_title(f'a/b = {a}/{b}')
    ax.axis('equal')
    ax.grid(True)
    ax.legend()

frames = 100
A = 1
B = 1
delta = 0  


ani = matplotlib.animation.FuncAnimation(plt.gcf(), update, frames=frames, interval=100, repeat=True)

plt.show()