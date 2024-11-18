# operasi kompirasi / pembandingan 

# hasil operasi selalu bertipe boolean (TRUE/FLASE)

# >,<,==,!=,>=,<=,is, dan is not

a = 4
b = 2

# lebih besar dari sama dengan
print("===Lebih besar dari (>)===")
hasil = a > b # TRUE
print(a, ">", 3, "=", hasil)
hasil = b > a # FLASE
print(b, ">" , 3, "=", hasil)
hasil = b > 2 # TERU
print(b, ">", 2, "=", hasil)

# lebih besar dari >
print("===Lebih besar dari (<)===")
hasil = a < b # FLASE
print(a, "<", 3, "=", hasil)
hasil = b < a # TERU
print(b, "<" , 3, "=", hasil)
hasil = b < 2 # FLASE
print(b, "<", 2, "=", hasil)