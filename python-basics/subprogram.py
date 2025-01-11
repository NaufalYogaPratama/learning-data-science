# Subprogram -> serangkaian instruksi dirancang untuk melakukan operasi yang sering digunakan dalam suatu program

# tanpa subprogramn
# Luas pertama
panjang = 5
lebar = 10
luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)
# Luas kedua
panjang = 4
lebar = 15
luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# dengan subprogram
def mencari_luas_persegi_panjang(panjang,lebar): #-> user-defined functions
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang
persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

# Docstring
def mencari_luas_persegi_panjang_docstring(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.
    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.
    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang
persegi_panjang_pertama = mencari_luas_persegi_panjang_docstring(5,10)
print(persegi_panjang_pertama)

# Parameter
# Positional-or-Keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan
print(greeting("Naufal", "Selamat pagi!")) #-> postional
print(greeting(pesan="Selamat sore!", nama="Naufal")) #-> keyword
# Var-positional (Variadic Positional Parameter)
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total
print(hitung_total(1, 2, 3))
# Var-Keyword (Variadic Keyword Parameter)
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info
print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

# Lambda Expression
mencari_luas_persegi_panjang_lambda = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang_lambda(5,10))

# Prosedur -> tidak mengharuskan adanya parameter input atau output dan dapat dipandang sebagai fungsi yang tidak menghasilkan nilai
def greeting_pros(name):
    print("Halo " + name + ", Selamat Datang!")
greeting_pros("Naufal Yoga")