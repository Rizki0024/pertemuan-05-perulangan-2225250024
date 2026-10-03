# Pertemuan 05 Perulangan Python

## Identitas
* **Nama:** Rizki Ramadan
* **NIM:** 2225250024
* **Kelas:** 3F

## Tujuan
Pada pertemuan ini saya mempelajari penggunaan perulangan `for` dan `while` dalam Python. Perulangan digunakan untuk menjalankan suatu proses secara berulang sesuai kondisi atau jumlah pengulangan yang ditentukan. Selain itu, saya juga belajar melakukan tracing perubahan variabel, menggunakan kondisi `if` di dalam perulangan, melakukan validasi input, serta mengelola dan mengunggah program melalui GitHub.

## Struktur Folder
pertemuan-05-perulangan-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
│── praktik/
│   └── kuis2_deret_aritmetika.py
└── kuis_formatif_pertemuan_5

## Cara Menjalankan Program
Pastikan Python sudah terpasang dan terminal berada pada folder utama project.

Latihan 1
python latihan/01_tabel_perkalian.py

Latihan 2
python latihan/02_jumlah_bilangan.py

Latihan 3
python latihan/03_validasi_input.py

Latihan 4
python latihan/04_hitung_genap.py

Kuis 2
python praktik/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Memasukkan nilai suku pertama a.
2. Memasukkan nilai beda d.
3. Memasukkan banyak suku n.
4. Memeriksa nilai n menggunakan while.
5. Jika n kurang dari atau sama dengan 0, program meminta input kembali.
6. Mengatur nilai awal total = 0.
7. Menggunakan for untuk melakukan perulangan sebanyak n kali.
8. Menghitung setiap suku berdasarkan suku pertama, beda, dan nomor suku.
9. Menambahkan setiap suku ke dalam total.
10. Menampilkan setiap suku dan jumlah akhirnya.

## Hasil Pengujian

Latihan 1 - Tabel Perkalian
Input: 4 -> Hasil: Tabel perkalian 4 dari 1 sampai 10 -> Status: Berhasil
Input: -3 -> Hasil: Tabel perkalian -3 dari 1 sampai 10 -> Status: Berhasil
(Kedua pengujian menghasilkan 10 baris sesuai dengan jumlah perulangan yang ditentukan.)

Latihan 2 - Jumlah Bilangan
Input: 1 -> Hasil yang Diharapkan: 1 -> Status: Berhasil
Input: 5 -> Hasil yang Diharapkan: 15 -> Status: Berhasil
Input: 10 -> Hasil yang Diharapkan: 55 -> Status: Berhasil

Latihan 3 - Validasi Input
Input: 120 -> Hasil: Ditolak karena lebih dari 100 -> Status: Berhasil
Input: -5 -> Hasil: Ditolak karena kurang dari 0 -> Status: Berhasil
Input: 75 -> Hasil: Diterima -> Status: Berhasil
(Program berhasil meminta input kembali sampai nilai yang dimasukkan berada pada rentang 0 sampai 100.)

Latihan 4 - Menghitung Bilangan Genap
Input: 1 -> Hasil yang Diharapkan: 0 -> Status: Berhasil
Input: 2 -> Hasil yang Diharapkan: 1 -> Status: Berhasil
Input: 5 -> Hasil yang Diharapkan: 2 -> Status: Berhasil
Input: 10 -> Hasil yang Diharapkan: 5 -> Status: Berhasil

Kuis 2 - Deret Aritmetika
Input a=2, d=3, n=5 -> Suku yang Dihasilkan: 2, 5, 8, 11, 14 -> Jumlah: 40.00 -> Status: Berhasil
Input a=10, d=-2, n=4 -> Suku yang Dihasilkan: 10, 8, 6, 4 -> Jumlah: 28.00 -> Status: Berhasil
Input a=1.5, d=0.5, n=3 -> Suku yang Dihasilkan: 1.5, 2.0, 2.5 -> Jumlah: 6.00 -> Status: Berhasil

## Refleksi

1. Bagian mana yang menentukan jumlah perulangan?
Pada for, jumlah perulangan ditentukan oleh nilai atau urutan yang diberikan pada range(). Sedangkan pada while, jumlah perulangan bergantung pada kondisi yang diberikan.

2. Mengapa total = 0 harus diinisialisasi sebelum perulangan?
Karena total digunakan untuk menyimpan hasil penjumlahan setiap iterasi. Dengan memberikan nilai awal 0 sebelum perulangan, setiap hasil dapat ditambahkan ke nilai sebelumnya.

3. Apa yang terjadi jika total = 0 diletakkan di dalam perulangan?
Nilai total akan kembali menjadi 0 setiap kali perulangan dimulai, sehingga hasil penjumlahan sebelumnya akan hilang dan hasil akhirnya tidak sesuai.

4. Mengapa validasi n lebih sesuai menggunakan while?
Karena kita tidak mengetahui berapa kali pengguna akan memasukkan nilai yang salah. Perulangan dapat terus dilakukan selama nilai n belum memenuhi kondisi yang ditentukan.

5. Bagaimana cara memastikan perulangan berhenti?
Perulangan harus memiliki kondisi berhenti yang dapat tercapai. Pada while, nilai yang digunakan dalam kondisi harus diperbarui sehingga pada akhirnya kondisi menjadi salah.

## Kesimpulan
Pada pertemuan ini saya dapat menggunakan perulangan for dan while dalam Python untuk menyelesaikan beberapa permasalahan. Saya juga memahami penggunaan if di dalam perulangan, proses akumulasi, validasi input, serta cara melakukan pengujian program menggunakan beberapa test case.

Selain membuat program, saya juga mempelajari cara menyimpan perubahan program menggunakan Git dan mengunggahnya ke GitHub.

## Sumber dan Bantuan
- Bahan Ajar Pertemuan 05 Perulangan for dan while dalam Python di VS Code dan Pengumpulan melalui GitHub.
- Python Documentation.
- Visual Studio Code Documentation.
- GitHub Documentation.
- Bantuan AI digunakan sebagai pendamping dalam memahami materi dan menyusun solusi, kemudian program diuji kembali secara mandiri.
