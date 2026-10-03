# Menampilkan judul program
print("\n=== Tabel Perkalian ===")

# Mengambil input bilangan dari pengguna
n = int(input("Bilangan: "))

# Menampilkan hasil perkalian dari 1 sampai 10
for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")