import numpy as np
import urllib.request

# URL của file dữ liệu
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

response = urllib.request.urlopen(url)
data = np.genfromtxt(response, delimiter=',', dtype='str')

data[data == ''] = '0' 
numeric_data = np.array(data[:, :-1], dtype=float)  

num_nan = 10
rows, cols = numeric_data.shape
for _ in range(num_nan):
    i = np.random.randint(0, rows)
    j = np.random.randint(0, cols)
    numeric_data[i, j] = np.nan

numeric_data = np.nan_to_num(numeric_data)

print(numeric_data)
