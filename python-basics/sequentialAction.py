# Sequential Actions -> sederetan instruksi yang akan dijalankan oleh komputer berdasarkan urutan penulisannya
print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2023 - int(tahun_lahir)
print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")

# Case-sensitive
teks = "Naufal"
Teks = "Yoga"
print(teks)
print(Teks)
#print(TEks) -> akan error

# One-liner
x = 1
y = 2
x, y = y, x    # One-liner
print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)