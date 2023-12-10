from scipy.signal import square
import numpy as np
import matplotlib.pyplot as plotlib


frequency = 1.0
duration = 5.0
sampling_rate = 1000

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
rectangle_signal = square(2 * np.pi * frequency * t)

plotlib.plot(t, rectangle_signal, label='Прямоугольный сигнал')
plotlib.title('Прямоугольный сигнал')
plotlib.xlabel('Время')
plotlib.ylabel('Амплитуда')
plotlib.show()