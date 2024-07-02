import numpy as np
from urllib.request import urlopen

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(urlopen(url), delimiter=',', usecols=(0, 1, 2, 3))

print(data[:4, :])
