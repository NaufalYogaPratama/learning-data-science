# Control Flow -> sebuah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan dan di mana harus memulai dan berakhir

# 1 if-else statement
# ex 1
nilai = 65
if nilai>=80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai>=70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai>=60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")
# ex 2
nilai = 81
perilaku = 'tidak baik'
if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")
   
# Ternary Operators
lulus = True
print("selamat") if lulus else print("perbaiki")


# 2 loop (for and while)
# for -> Definite iteration -> sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.
for i in range(1,10,2): #-> range(start,stop,step)
    print(i)
# while -> Indefinite iteration -> sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment
# nested loop
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)
        
# Loop Control
# break -> untuk menghentikan loop
# ex 1
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1
# ex 2
for huruf in 'Nau fal':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))
    
# continue -> untuk melanjutkan ke iterasi berikutnya
for huruf in 'Nau fal':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
    
# Else after For
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")
    
# Else after While
count = 0
while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")
    
#Pass
Pass = 10
if Pass > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")
    
# List Comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka] #-> new_list=[expression for_loop_one_or_more_conditions] 
print(pangkat)
