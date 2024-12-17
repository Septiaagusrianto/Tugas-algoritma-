def konversi_nilai(nilai):
    if nilai > 90:
        return "A"
    elif 81 <= nilai <= 90:
        return "A-"
    elif 75 <= nilai <= 80:
        return "B+"
    elif 70 <= nilai <= 74:
        return "B"
    elif 65 <= nilai <= 69:
        return "C+"
    elif 60 <= nilai <= 64:
        return "C"
    elif 55 <= nilai <= 59:
        return "D"
    else:
        return "E"

# Contoh input nilai
nilai = float(input("Masukkan nilai (dapat berupa desimal, misal 82.5): "))
hasil = konversi_nilai(nilai)
print(f"Nilai: {nilai}, Grade: {hasil}")
