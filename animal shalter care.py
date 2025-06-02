# Animal Shelter Care
# Aplikasi sederhana untuk mencatat hewan di shelter

animals = []  # List untuk menyimpan data hewan

# Fungsi untuk menambahkan hewan
def tambah_hewan():
    nama = input("Masukan nama hewan: ")
    jenis = input("Masukan jenis hewan: ")
    umur = input("Masukan umur hewan: ")
    animals.append([nama, jenis, umur])
    print("Hewan berhasil ditambahkan!\n")
    print("Isi data sekarang:",animals)

# Fungsi untuk menampilkan semua hewan
def tampilkan_hewan():
    if not animals:
        print("Belum ada hewan di shelter.\n")
    else:
        print("\nDaftar Hewan di Shelter:")
        for i, hewan in enumerate(animals):
            print(f"{i+1}. Nama: {hewan[0]}, Jenis: {hewan[1]}, Umur: {hewan[2]}")
        print()

# Fungsi untuk mencari hewan
def cari_hewan():
    keyword = input("Cari berdasarkan nama atau jenis: ").lower()
    hasil = [h for h in animals if keyword in h[0].lower() or keyword in h[1].lower()]
    
    if hasil:
        print("\nHasil pencarian:")
        for hewan in hasil:
            print(f"Nama: {hewan[0]}, Jenis: {hewan[1]}, Umur: {hewan[2]}")
        print()
    else:
        print("Hewan tidak ditemukan.\n")

# Fungsi untuk menghapus hewan
def hapus_hewan():
    tampilkan_hewan()
    try:
        index = int(input("Masukkan nomor hewan yang ingin dihapus: ")) - 1
        if 0 <= index < len(animals):
            del animals[index]
            print("Hewan berhasil dihapus.\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka!\n")

# Fungsi untuk memperbarui data hewan
def update_hewan():
    tampilkan_hewan()
    try:
        index = int(input("Masukkan nomor hewan yang ingin diperbarui: ")) - 1
        if 0 <= index < len(animals):
            nama = input("Nama baru: ")
            jenis = input("Jenis baru: ")
            umur = input("Umur baru: ")
            animals[index] = [nama, jenis, umur]
            print("Data hewan berhasil diperbarui.\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka!\n")

# Menu utama
while True:
    print("=== Animal Shelter Care ===")
    print("1. Tambah Hewan")
    print("2. Tampilkan Daftar Hewan")
    print("3. Cari Hewan")
    print("4. Update Data Hewan")
    print("5. Hapus Hewan")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_hewan()
    elif pilihan == "2":
        tampilkan_hewan()
    elif pilihan == "3":
        cari_hewan()
    elif pilihan == "4":
        update_hewan()
    elif pilihan == "5":
        hapus_hewan()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan Animal Shelter Care!")
        break
    else:
        print("Pilihan tidak valid.\n")