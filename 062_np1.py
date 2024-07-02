import numpy as np
from urllib.request import urlopen

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

sepallength_data = np.genfromtxt(urlopen(url), delimiter=',', usecols=0)

print("Sepallength_data:")
print(sepallength_data[:5])

def min_max_normalize(data):
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

sepallength_normalized = min_max_normalize(sepallength_data)

print("Sepallength_normalized:")
print(sepallength_normalized[:5])

# Min-Max Normalization: Là phương pháp đơn giản nhất để chuẩn hóa phạm vi của các đặc trưng dữ liệu.
# Công thức tổng quát cho phạm vi [0, 1] là:
# Xnormalied = (X - Xmin) / (Xmax - Xmin)
# X: giá trị ban đầu của dữ liệu
# Xmax: giá trị lớn nhất trong cột
# Xmin: giá trị bé nhất trong cột