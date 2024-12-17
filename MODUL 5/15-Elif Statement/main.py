# membuat kalkulator sederhana

print(20*"=")
print("kalkulator sederhana")
print(20*"=" + "\n")

angka_1 = float (input("bilangan 1 = "))
operator = input("pilih operator (+,-,x,/,**,%,//)")
angka_2 = float(input("Bilangan 2 = "))
# percabagan banyak kondisi

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "x" :
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "/" :
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "**" :
    hasil = angka_1 ** angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "%" :
    hasil = angka_1 % angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "//" :
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah = {hasil}")    
else:
    print("masukan dengan benar")

print("program berakhir")