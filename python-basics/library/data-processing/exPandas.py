import pandas as pd

# Membuat DataFrame
print("\nContoh implementasi Pandas:")
data = {
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Usia': [24, 27, 22],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Menambah kolom baru
print("\nMenambah kolom baru:")
df['Pekerjaan'] = ['Engineer', 'Doctor', 'Artist']
print(df)

# Menghitung statistik dasar
print("\nStatistik dasar:")
print(df.describe())

# Menyaring data berdasarkan kondisi
print("\nMenyaring data dengan usia > 23:")
filtered_df = df[df['Usia'] > 23]
print(filtered_df)

# Membaca dan menulis ke file CSV
print("\nMenyimpan DataFrame ke file CSV:")
df.to_csv('data_output.csv', index=False)
print("DataFrame telah disimpan ke 'data_output.csv'")
