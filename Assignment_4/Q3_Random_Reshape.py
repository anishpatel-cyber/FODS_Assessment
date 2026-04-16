'''
Program to create random array using numpy and reshape into matrix 
of valid dimensions.
'''

import numpy as np

# Create random array of 12 numbers
arr = np.random.randint(1, 100, 12)

print("Original Array:", arr)

# Sort
arr.sort()

print("Sorted Array:", arr)

# Reshape
matrix = arr.reshape(3, 4)

print("Reshaped Matrix:\n", matrix)