import numpy as np

arr1 = np.array(input().split(), dtype=int)
arr2 = np.array(input().split(), dtype=int)

common_elements = np.intersect1d(arr1, arr2)
print(common_elements)
