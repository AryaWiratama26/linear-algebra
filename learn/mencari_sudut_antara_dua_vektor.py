import numpy as np
import math

""" 

Mencari sudut diantara dua vektor

COS 0 = u(bar) . v(bar) / norm(u). nor(v)

Persamaan hasil kali titik (dot product) dapat digunakan untuk menghitung sudut teta diantar dua buah vektor

0 sudut lancip jika dan hanya jika u.v > 0
0 sudut tumpul jika dan hanya jika u.v < 0
0 phi/2 jika dan hanya jika u.v = 0

Teuntukan sudut yang dibentuk oleh vektor a = 2i, b = 2i + 2j


"""

a = [2,0]
b = [2,2]

norm_a = np.linalg.norm(a)
print(f"norm a : {norm_a}")

norm_b = np.linalg.norm(b)
print(f"norm b : {norm_b}")


cos_teta = np.dot(a, b) / (norm_a * norm_b)
print(f"cos θ: {cos_teta}")

theta_rad = math.acos(cos_teta)
print(f"θ (radian): {theta_rad}")

theta_deg = math.degrees(theta_rad)
print(f"θ (derajat): {theta_deg}")


""" 

Diberikan u = [1,-2,3], v = [-3,4,2], w = [3,6,3]
Tentukan jenis sudut yang dibentuk oleh 

a . u dan v
b. v dan w
c. u dan w
"""

u = [1,-2,3]
v = [-3,4,2]
w = [3,6,3]

# u dan v

u_dan_v = np.dot(u,v)
print(f"u dan v : {u_dan_v} = Sudut Tumpul")

# v dan w

v_dan_w = np.dot(v,w)
print(f"v dan w : {v_dan_w} = Sudut lancip")

# u dan w

u_dan_w = np.dot(u,w)
print(f"u dan w : {u_dan_w} = Sudut {math.pi/2}")





