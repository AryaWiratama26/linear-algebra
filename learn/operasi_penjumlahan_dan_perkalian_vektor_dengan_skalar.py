import numpy as np
import math
"""

Secara analitis, operasi penjumlahan dan perkalian vektor dapat ditulis sebagai berikut:
Misal a(bar) = (a1,a2,a3) dan b(bar) = (b1,b2,b3) adalah vektor diruang yang sama, maka

1. a(bar) + b(bar) = (a1+b1,( a2+b2, a3+b3)
2. a(bar) - b(bar) = (a1-b1, a2-b2, a3-b3)
3. k(skalar)a = (ka1, ka2, ka3)

---------------------------------------------

Perkalian antara dua vektor
- Hasil kali titik (dot product)
- Hasil kali silang (cross product)

Hasil kali titik :
-> Hasil kali titik merupakan operasi antara dua buah vektor pada ruang yang sama yang menghasilkan skalar
a(bar)*b(bar) = ||a(bar)|| . ||b(bar)|| . cos 0

dimana 

||a|| -> panjang dari a
||b|| -> panjang dari b
||cos 0|| -> sudut antara keduanya 

Hasil kali silang : 
-> Hasil kali silang merupakan operasi antara dua vektor pada yang |R^3 yang menghasilkan vektor


"""


# Penuumlahan
a = [3,1,2]
b = [2,4,5]

petambahan_a_dan_b = [a[0]+b[0], a[1]+b[1], a[2]+b[2]]
print(petambahan_a_dan_b)

# or
# element_wise = a + b
# print(element_wise)

# Perkurangan 
x = [2,1,2]
y = [2,-1,4]

perkurangan_x_y = [x[0]-y[0], x[1]-y[1], x[2]-y[2]]
print(perkurangan_x_y)

# Perkalian dengan skalar

k = 2
h = [1,2,3]

skalar_perkalian = [k*h[0], k*h[1], k*h[2]]
print(skalar_perkalian)


""" 

Tentukan hasil kali titik dari dua vektor a(bar) = 2i dan b(bar) = 2i + 2j, dengan sudut yang terbentuk antara a dan b adalah 45^o
"""

norm_a = math.sqrt(2**2 + 0**2)
print(f"norm_a : {norm_a}")

norm_b = math.sqrt(2**2 + 2**2) 
print(f"norm_b {norm_b}")

angle_in_radians = math.radians(45)

print(angle_in_radians)

dot_product = norm_a * norm_b * math.cos(angle_in_radians)
print(dot_product)
