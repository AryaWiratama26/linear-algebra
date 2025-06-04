import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from learn import *


"""DAY 1"""
print(f"{'-----DAY 1-----':^20}"+ "\n")

# Basic Matrix Operation
A = np.array([
    [2, 3],
    [2, -1]
])

B = np.array([
    [3, 2],
    [4, 1]
])

scalar = 5

C = np.array([
    [3,2],
    [1,-1]
])

D = np.array([
    [3,1,0],
    [1,-2,3]
])

print(f"Summation Matrix AB =\n{summation_matrix(A, B)}")
print(f"Scalar Multiplication Matrix =\n{scalar_multiplication_matrix(scalar, B)}")
print(f"Matrix Multiplication =\n{matrix_multiplication(C,D)}")

# Trace and Transpose

A1 = np.array([
    [1,3,2],
    [2,1,3],
    [2,4,-5]
])

print(f"Trace Matrix =\n{trc(A1)}")
print(f"Transpose Matrix =\n{transp(A1)}")

print("\n"+f"{'-----DAY 1-----':^20}")
