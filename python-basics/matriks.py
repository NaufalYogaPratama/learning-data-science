import numpy as np #-> using numpy to save memory
import sys
var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

# Declare and access matrix
var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1])

# Matrix Operations in Python
# Membuat matriks 2x2
var_mat_sys = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]
for i in range(len(var_mat_sys)):
  for j in range(len(var_mat_sys[0])):
    def_mat[i][j] = var_mat_sys[i][j]*2
print(def_mat)
#using numpy
var_mat_numpy = np.array([[5, 0],
                    [1, -2]])
result = var_mat_numpy * 2
print(result)