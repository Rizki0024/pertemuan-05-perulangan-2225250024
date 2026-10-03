# Menampilkan judul program
print("\n=== Deret Aritmetika ===")

# Mengambil input suku pertama dan beda dari pengguna
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

# Mengambil input banyak suku dari pengguna
n = int(input("Banyak suku n: "))

# Mengecek apakah banyak suku merupakan bilangan positif
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

# Menyiapkan variabel untuk menyimpan jumlah seluruh suku
total = 0

# Menghasilkan setiap suku menggunakan perulangan for
for i in range(n):

    # Menghitung nilai suku berdasarkan suku pertama dan beda
    suku = a + i * d

    # Menambahkan suku ke dalam total
    total += suku

    # Menampilkan nomor dan nilai setiap suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

# Menampilkan jumlah seluruh suku
print(f"Jumlah = {total:.2f}")