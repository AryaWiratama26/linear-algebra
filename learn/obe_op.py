import numpy as np

"""
Studi kasus soal

Tentukan matriks eleson baris tereduksi dari matriks berikut :

A = ([
    [-3,-2,-1],
    [1,2,3],
    [0,2,4]
])

"""

# 1. Definisika matriks

print("1. Definisikan Matriks")

A = np.array([
    [-3,-2,-1],
    [1,2,3],
    [0,2,4]
])

print(A)

print("============================\n")


# 2. Tukar baris 1 dan 2

print("Tukar baris 1 dan 2")

A[[0,1]] = A[[1,0]]

print(A)

print("============================\n")


# 3. Membuat 0 nilai di bawah 1 utama baris utama

print("Membuat 0 nilai di bawah 1 utama baris utama")

temp = (3*A[0]) + A[1]

A[[1]] = temp

print(A)

print("============================\n")

# 4. Kembuat 1 pada angka 4 pada baris ke-2 kolom ke -2

print("Kembuat 1 pada angka 4 pada baris ke-2 kolom ke -2")

temp = A[1] * 1/4

A[[1]] = temp

print(A)

print("============================\n")


# 5. Membuat nilai 0 di bawah 1 utama baris ke-2 dan kolom ke-2

print("Membuat nilai 0 di bawah 1 utama baris ke-2 dan kolom ke-2")

temp = (-2 * A[1] + A[2])

A[2] = temp

print('Ini sudah termasuk kedalam MEB')
print(A)

print("============================\n")

# 6. Membuat nilai 2 pada baris ke-1 kolom ke-2 menjadi 0

print("Membuat nilai 2 pada baris ke-1 kolom ke-2 menjadi 0")

temp = (-2 * A[1]) + A[0]

A[0] = temp

print("Ini adalah Matrik Eselon Baris Tereduksi (MEBT) atau Gauss-Jordan : \n")
print(A)

print("============================\n")