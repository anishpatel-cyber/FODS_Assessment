'''
Program to take two matrices as input from the user and perform matrix operations
such as addition, subtraction and multiplication using numpy with validation.
'''

import numpy as np

try:
    # Input matrices
    rows = int(input("Enter rows: "))
    cols = int(input("Enter cols: "))

    print("Enter first matrix:")
    A = np.array([list(map(int, input().split())) for _ in range(rows)])

    print("Enter second matrix:")
    B = np.array([list(map(int, input().split())) for _ in range(rows)])

    # Addition & Subtraction
    print("Addition:\n", A + B)
    print("Subtraction:\n", A - B)

    # Multiplication check
    if A.shape[1] == B.shape[0]:
        print("Multiplication:\n", np.dot(A, B))
    else:
        raise ValueError("Matrix dimensions not compatible for multiplication")

except Exception as e:
    print("Error:", e)