import numpy as np

""" 

Cross Product merupakan hasil kali antara dua vektor di ruang (|R^3) yang menghasilkan vektor yang tegak lurus terhadap kedua vektor yang dikalikan tersebut.
Misalkan a = (a1,a2,a3) dan b = (b1,b2,b3) adalah vektor di |R^3, maka cross product a x b yang di definisikan


a x b = [i j k]
        [a1 a2 a3]
        [b1 b2 b3]
        
Disarankan gunakan metode ekspansi kofaktor

======

[a2 a3] i - [a1 a3] j + [a1 a2] k
[b2 b3]     [b1 b3]     [b1, b2]

Carilah w = u x v dimana u = (1,2,-2) dan v = (3,0,1)

"""

u = np.array([1,2,-2])
v = np.array([3,0,1])

w = np.cross(u,v)
print(w)