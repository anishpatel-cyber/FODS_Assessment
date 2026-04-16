'''
Program to perform basic operations like sum, mean value, largest and
smallest value on a NumPy array.
'''

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

# Sum
print("Total Sum:", np.sum(arr))

# Mean
print("Mean:", np.mean(arr))

# Max & Min
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))