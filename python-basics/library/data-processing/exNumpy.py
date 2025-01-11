import numpy

# Membuat matriks 3x3
matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriks awal:")
print(matriks)

# Operasi dasar pada matriks
print("\nTranspos matriks:")
print(matriks.T)

print("\nDeterminant matriks:")
print(numpy.linalg.det(matriks))

print("\nInvers matriks:")
try:
    invers = numpy.linalg.inv(matriks)
    print(invers)
except numpy.linalg.LinAlgError:
    print("Matriks tidak memiliki invers.")

# Penjumlahan dan perkalian dengan skalar
skalar = 2
print("\nPenjumlahan dengan skalar 2:")
print(matriks + skalar)

print("\nPerkalian dengan skalar 2:")
print(matriks * skalar)

# Penjumlahan dan perkalian antar matriks
matriks_b = numpy.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("\nMatriks B:")
print(matriks_b)

print("\nPenjumlahan Matriks A dan B:")
print(matriks + matriks_b)

print("\nPerkalian elemen-wise Matriks A dan B:")
print(matriks * matriks_b)

print("\nPerkalian matriks A dan B (dot product):")
print(numpy.dot(matriks, matriks_b))

# Menghitung eigenvalue dan eigenvector
print("\nEigenvalues dan Eigenvectors Matriks A:")
eigenvalues, eigenvectors = numpy.linalg.eig(matriks)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# Membuat matriks identity dan diagonal
identity_matrix = numpy.eye(3)
diagonal_matrix = numpy.diag([10, 20, 30])
print("\nMatriks Identitas:")
print(identity_matrix)

print("\nMatriks Diagonal:")
print(diagonal_matrix)

# Reshape matriks
reshape_matriks = numpy.arange(1, 17).reshape(4, 4)
print("\nMatriks diubah menjadi 4x4:")
print(reshape_matriks)

# Menghitung norm matriks
print("\nNorma Matriks A:")
print(numpy.linalg.norm(matriks))