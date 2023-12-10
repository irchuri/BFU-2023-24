import numpy as np

a = np.arange(16).reshape(4, 4)
print(f"Old: \n{a}")

a[[0, 2]] = a[[2, 0]]

print(f"New: \n{a}")