import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, 4]
unique_species = np.unique(species)
count_species = len(unique_species)

print(f"Уникальные: ", unique_species)
print(f"Количество: ", count_species)