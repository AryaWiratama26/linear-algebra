import numpy as np


""" 

    Untuk 2 x 2
    A^-1 = 1 / det(a) . adjoin(A)
    
    adjoin = [d -b]
             [-c a]
             
    untul 3 x 3 adjoinnya menggunakan Transpose Cofaktor
"""


a = np.array([
    [1,0,1],
    [1,-1,0],
    [0,2,1],
])

invers_a = np.linalg.inv(a)
print(invers_a)