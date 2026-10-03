# Menampilkan judul program
print("\n=== Jumlah Bilangan ===")

# Mengambil input bilangan dari pengguna
n = int(input("Banyak bilangan: "))

# Menyiapkan variabel untuk menyimpan jumlah
total = 0

# Menjumlahkan bilangan dari 1 sampai n
for i in range(1, n + 1):
    total += i

# Menampilkan hasil penjumlahan
print(f"Jumlah = {total}")