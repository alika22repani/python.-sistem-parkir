matriks = [
    [4, 7, 9],
    [8, 13, 10],
    [3, 22, 15],
]
maks = matriks[0] [0]

for baris in matriks:
    for elemen in baris:
        if elemen > maks:
            maks = elemen 
print("Angka terbesar dalam matriks adalah:", maks)