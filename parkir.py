# Inisialisasi tempat parkir
parkiran = {}

# Fungsi untuk menambah kendaraan
def tambah_kendaraan(nomor, jenis, waktu_masuk):
    parkiran[nomor] = {
        "jenis": jenis,
        "waktu_masuk": waktu_masuk
    }
    print(f"Kendaraan {nomor} berhasil ditambahkan.")

# Fungsi untuk menghapus kendaraan dan menghitung biaya parkir
def hapus_kendaraan(nomor, waktu_keluar, tarif_per_jam):
    if nomor in parkiran:
        data = parkiran.pop(nomor)
        waktu_masuk = data["waktu_masuk"]
        
        if waktu_keluar < waktu_masuk:
            print("Error: Waktu keluar tidak boleh lebih kecil dari waktu masuk.")
            return
        
        durasi = waktu_keluar - waktu_masuk
        biaya = durasi * tarif_per_jam
        print(f"Kendaraan {nomor} keluar. Biaya parkir: RP{biaya:,}")  
    else:
        print("Kendaraan tidak ditemukan.")
if __name__ == "__main__":
    tambah_kendaraan("B1234DCD", "mobil", 10)
    hapus_kendaraan("B1234DCD", 12, 5000)
        

 