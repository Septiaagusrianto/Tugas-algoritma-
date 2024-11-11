# Program untuk konversi Fahrenheit ke Celsius

# Meminta input suhu dalam Fahrenheit dari pengguna
fahrenheit = float(input("Masukkan suhu dalam (F): "))

# Rumus konversi dari Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Menampilkan hasil konversi
print("Konversi F -> C: {:.2f}°C".format(celsius))

# Masukkan suhu dalam Fahrenheit
fahrenheit = 130

# Konversi Fahrenheit ke Celsius
celsius = (5/9) * (fahrenheit - 32)

# Tampilkan hasil konversi
print("Suhu dalam Fahrenheit:", fahrenheit)
print("Suhu dalam Celsius:", round(celsius,2))