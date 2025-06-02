angka_list = [3, 4, 7, 10, 12, 23, 28, 30, 34, 43, 50]
jumlah_genap = 0
for angka in angka_list:
    if angka % 2 == 0:
        jumlah_genap += 1
print("jumlah angka genap dalam list adalah:", jumlah_genap)