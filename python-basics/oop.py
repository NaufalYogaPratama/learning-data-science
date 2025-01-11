class Mobil: # Deklarasi kelas 
    def __init__(self, warna, merek, kecepatan): #-. attributes with constructor class
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self): #-> object method
        self.kecepatan += 10


class MobilSport(Mobil): #-> Pewarisan kelas dari parent class (Mobil)
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self): #-> override method
        super().tambah_kecepatan() #-> super konsep
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160) #-> deklarasi objek
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)