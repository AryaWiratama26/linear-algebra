import math
import numpy as np

"""

Definisi dari vektor : Besaran yang memiliki nilai dan arah

1. Vektor di Bidang (|R^2)
bisa dinotasikan dengan a bar, a topi, dan a tebal

a(bar) = (a1, a2) = (a1)  
                    (a2)


2. Vektor di Ruang (|R^3)

a(bar) = (a1,a2,a3) = (a1)
                      (a2)
                      (a3)


-------------------------------------------------------

Norm Vektor (Panjang Vektor)

Misalkan U(bar)  = (u1, u2), maka ||u(bar)|| = akar u1^2 + u2^2. 


-------------------------------------------------------

Jarak antara dua buah titik

Misal a(bar) = (a1, a2) dan b(bar) = (b1,b2), Maka jarak antara titik A dan B adalah

d(A,B) = ||AB(bar)|| = akar (b1-a1)^2 + (b2-a2)^2


"""

u = [3,-2]

norm_vektor_u = math.sqrt(u[0]**2 + u[1]**2)
print(norm_vektor_u)


# Contoh lain

b = [1,2,2]

norm_vektor_b = math.sqrt(b[0]**2 + b[1]**2 + b[2])
print(np.ceil(norm_vektor_b))

# Atau bisa menggunakan method norm pada numpy
print(np.linalg.norm(b))


x = [1,1,1] 
y = [2,3,4]

jarak_x_dan_y = math.sqrt(
    (y[0] - x[0])**2 +
    (y[1] - x[1])**2 +
    (y[2] - x[2])**2
)
print(jarak_x_dan_y)