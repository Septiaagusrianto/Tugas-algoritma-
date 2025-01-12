# Program menghitung total belanja dengan diskon berdasarkan kepemilikan kartu member

# Input dari pengguna
nama = input("Masukkan nama pelanggan: ")
kartu_member = input("Apakah pelanggan memiliki kartu member? (ya/tidak): ").strip().lower() == "ya"
total_belanja = float(input("Masukkan total belanja: "))

# Inisialisasi variabel diskon
diskon_persen = 0

if kartu_member:
    if total_belanja > 500_000:
        diskon_persen = 10
    elif total_belanja >= 100_000:
        diskon_persen = 5
    elif total_belanja < 100_000:
        diskon_persen = 3
else:
    if total_belanja > 100_000:
        diskon_persen = 3

# Hitung diskon dalam rupiah dan total setelah potongan
diskon_rupiah = total_belanja * (diskon_persen / 100)
total_setelah_potongan = total_belanja - diskon_rupiah

# Tampilkan hasil
print("Nama Pelanggan          :", nama)
print("Status Kartu Member     :", "Memiliki" if kartu_member else "Tidak Memiliki")
print("Total Belanja Sebelum   : Rp", format(total_belanja, ","))
print("Diskon (dalam Persen)   :", diskon_persen, "%")
print("Diskon (dalam Rupiah)   : Rp", format(diskon_rupiah, ","))
print("Total Setelah Potongan  : Rp", format(total_setelah_potongan, ","))
