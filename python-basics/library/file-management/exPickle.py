import pickle

# Data yang akan disimpan
my_data = {
    'name': 'Naufal',
    'age': 19,
    'hobbies': ['coding', 'reading', 'gaming']
}

# Menyimpan data ke file menggunakan pickle
with open('my_data.pkl', 'wb') as file:
    pickle.dump(my_data, file)
print("Data berhasil disimpan ke my_data.pkl")

# Membaca data dari file menggunakan pickle
with open('my_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print("Data yang di-load dari file:")
print(loaded_data)

# Contoh implementasi untuk menyimpan dan memuat daftar angka
numbers = [1, 2, 3, 4, 5]

# Menyimpan daftar angka
with open('numbers.pkl', 'wb') as file:
    pickle.dump(numbers, file)
print("Daftar angka berhasil disimpan ke numbers.pkl")

# Memuat daftar angka
with open('numbers.pkl', 'rb') as file:
    loaded_numbers = pickle.load(file)
print("Daftar angka yang di-load dari file:")
print(loaded_numbers)