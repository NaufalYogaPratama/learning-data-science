import matplotlib.pyplot as plt
import seaborn as sns

# Data untuk visualisasi
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Membuat plot garis sederhana menggunakan Matplotlib
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Data Sample', color='blue', marker='o')

# Menambahkan judul dan label
plt.title('Contoh Plot Menggunakan Matplotlib', fontsize=14)
plt.xlabel('Sumbu X', fontsize=12)
plt.ylabel('Sumbu Y', fontsize=12)

# Menambahkan grid dan legenda
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Menampilkan plot
plt.show()

# Membuat visualisasi tambahan: Histogram menggunakan Matplotlib
data = [22, 24, 22, 25, 30, 27, 28, 29, 22, 24, 30]
plt.figure(figsize=(8, 5))
plt.hist(data, bins=5, color='green', edgecolor='black', alpha=0.7)
plt.title('Histogram Data', fontsize=14)
plt.xlabel('Kelompok Data', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Menampilkan histogram
plt.show()

# Membuat visualisasi tambahan: Scatter Plot menggunakan Matplotlib
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [5, 10, 15, 20, 25]
plt.figure(figsize=(8, 5))
plt.scatter(x_scatter, y_scatter, color='red', label='Points', s=100, alpha=0.8)
plt.title('Scatter Plot Example', fontsize=14)
plt.xlabel('Sumbu X', fontsize=12)
plt.ylabel('Sumbu Y', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Menampilkan scatter plot
plt.show()

# Membuat visualisasi tambahan menggunakan Seaborn
# Data untuk seaborn
import pandas as pd

data_seaborn = pd.DataFrame({
    'Kategori': ['A', 'B', 'C', 'D', 'E'],
    'Nilai': [15, 25, 35, 45, 20]
})

# Bar Plot menggunakan Seaborn
plt.figure(figsize=(8, 5))
sns.barplot(data=data_seaborn, x='Kategori', y='Nilai', palette='muted')
plt.title('Bar Plot Menggunakan Seaborn', fontsize=14)
plt.xlabel('Kategori', fontsize=12)
plt.ylabel('Nilai', fontsize=12)

# Menampilkan Bar Plot
plt.show()

# Heatmap menggunakan Seaborn
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plt.figure(figsize=(6, 5))
sns.heatmap(matrix, annot=True, fmt="d", cmap="coolwarm", cbar=True)
plt.title('Heatmap Menggunakan Seaborn', fontsize=14)

# Menampilkan Heatmap
plt.show()