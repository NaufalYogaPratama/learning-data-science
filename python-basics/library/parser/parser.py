import argparse #-> Argument parser bermanfaat jika kita ingin membuat program atau skrip kecil yang langsung menerima parameter pada saat pemanggilan program
import sys
from datetime import datetime

# Membuat parser
parser = argparse.ArgumentParser(description="Script panggildicoding.py")

# Menambahkan argumen
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal Lahir Anda (format: dd-mm-yyyy)")

# Parsing argumen
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Validasi format tanggal lahir
try:
    tanggal_lahir = datetime.strptime(args.tanggallahir, '%d-%m-%Y')
except ValueError:
    print("Error: Format tanggal lahir harus dd-mm-yyyy.")
    sys.exit(1)

# Output hasil
print(f"Terima kasih telah menggunakan panggildicoding.py, {args.nama}.")
print(f"Tanggal lahir Anda adalah {tanggal_lahir.strftime('%d %B %Y')}.")
