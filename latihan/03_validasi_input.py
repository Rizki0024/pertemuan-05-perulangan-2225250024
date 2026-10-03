# Menampilkan judul program
print("\n=== Validasi Nilai ===")

# Mengambil input nilai dari pengguna
nilai = float(input("Nilai 0-100: "))

# Mengecek apakah nilai berada di luar rentang yang diperbolehkan
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")

    # Meminta pengguna memasukkan nilai kembali
    nilai = float(input("Nilai 0-100: "))

# Menampilkan nilai yang sudah valid
print(f"Nilai diterima: {nilai}")