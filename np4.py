import numpy as np

arr = np.array(input().split(), dtype=int)

filtered_arr = arr[(arr >= 5) & (arr <= 10)]

print(filtered_arr)