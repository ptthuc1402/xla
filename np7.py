import numpy as np
from urllib.request import urlopen

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

data = np.genfromtxt(urlopen(url), delimiter=',', usecols=0)

mean_sepal_length = np.mean(data)
median_sepal_length = np.median(data)
std_sepal_length = np.std(data)

print(f"Mean:, {mean_sepal_length: .2f}")
print(f"Median, {median_sepal_length: .2f}")
print(f"Standard deviation, {std_sepal_length: .2f}")
