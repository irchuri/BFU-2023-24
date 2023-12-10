import numpy as np
import matplotlib.pyplot as plotlib


plotlib.hist(172 + 8 * np.random.randn(10000), 100, facecolor="pink")
plotlib.title('Нормальное распределение')
plotlib.xlabel('Величина')
plotlib.ylabel('Плотность вероятности')
plotlib.show()


