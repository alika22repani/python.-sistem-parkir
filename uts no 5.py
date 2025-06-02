# Program Mesin ATM Sederhana 
saldo = 10000000
pin_terdaftar = "4321"
pin = "4321"  # PIN yang dimasukkan secara langsung

if pin == pin_terdaftar:
    pilihan = "2"  # "1" = cek saldo, "2" = tarik tunai, "3" = tabung, "4" = keluar
    print(f"Pilihan yang dimasukkan: {pilihan}")

    if pilihan == "1":
        print(f"Saldo Anda: {saldo}")
    elif pilihan == "2":
        jumlah = 500000  # jumlah penarikan
        if jumlah <= saldo:
            saldo -= jumlah
            print(f"Penarikan berhasil. Saldo sekarang: {saldo}")
        else:
            print("Saldo tidak mencukupi.")
    elif pilihan == "3":
        simpan = 200000  # jumlah yang ingin ditabung
        saldo += simpan
        print(f"Tabungan berhasil. Saldo sekarang: {saldo}")
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan Bank ABCXYZ.")
    else:
        print("Pilihan tidak valid.")
else:
    print("PIN salah!")