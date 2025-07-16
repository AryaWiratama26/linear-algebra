import numpy as np
# Metode Sarus

# Matriks 2 x 2
"""
    |a b|
    |c d| = a.d - b.c
"""

# Contoh matriks 2 x 2 dengan metode sarus

a = np.array([
    [3,2],
    [1,1]
])

deteminan_a_2x2 = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
print(deteminan_a_2x2)


print("==============================\n")

""" 

    Matriks 3 x 3
    
    [a b c][a b]
    [d e f][d e]
    [g h i][g h] = (aei + bfg + cdh) - (ceg + afh + bdi)
"""
