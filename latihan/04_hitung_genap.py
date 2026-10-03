# Menampilkan judul program
print("\n=== Menghitung Bilangan Genap ===")

# Mengambil input batas bilangan dari pengguna
n = int(input("Banyak bilangan: "))

# Menyiapkan variabel untuk menghitung banyak bilangan genap
jumlah_genap = 0

# Mengecek setiap bilangan dari 1 sampai n
for i in range(1, n + 1):

    # Mengecek apakah bilangan habis dibagi 2
    if i % 2 == 0:
        jumlah_genap += 1

# Menampilkan jumlah bilangan genap
print(f"Banyak bilangan genap = {jumlah_genap}")