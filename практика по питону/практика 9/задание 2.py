import numpy as np

massiv = np.array([1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 6])
print(np.unique(massiv, return_counts=True))