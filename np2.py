import numpy as np

arr = np.full((4, 5), 1)
arr[:2, :] = np.arange(10).reshape(2, 5)

print(arr)
