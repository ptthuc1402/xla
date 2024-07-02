import numpy as np
from urllib.request import urlopen

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(urlopen(url), delimiter=',', usecols=(0, 2))

filtered_data = data[(data[:, 0] < 5.0) & (data[:, 1] > 1.5)]

print("Results")
print(filtered_data)
