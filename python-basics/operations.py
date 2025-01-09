# Operasi pada List, Set, dan String

# 1 len()
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
print(len(contoh_list))

contoh_set = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(contoh_set)
print(len(contoh_set))

contoh_str = "Belajar Python"
print(contoh_str)
print(len(contoh_str))

# 2 max() dan min()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# 3 Count
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10] #-> list
print(genap.count(6))

string = "Belajar Python di Dicoding sangat menyenangkan" #-> string
substring = "a"
print(string.count(substring))

# 4 in dan not in
kalimat = "Belajar Python bersama Naufal sangat menyenangkan"
print('Naufal' in kalimat)
print('tidak' in kalimat)
print('Naufal' not in kalimat)
print('tidak' not in kalimat)

# 5 Sort -> tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)


# Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]