# Daftar buku dan statusnya
buku = ["Python Dasar", "Algoritma dan Logika", "Pemrograman Web"]
status = [True, True, True]  # True berarti tersedia

hari_sekolah = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
batas_pinjam = 3
denda_per_hari = 500

print("=== PEMINJAMAN BUKU ===")
nama = input("Nama peminjam: ")

# Nama Peminjam
print(f"Selamat datang {nama}, di Sistem Perpustakaan Sekolah.")
# Tampilkan buku yang tersedia
print("\nDaftar Buku:")
for i in range(len(buku)):
    if status[i]:
        print(f"{i+1}. {buku[i]}")

# Pilih buku
pilih = int(input("\nPilih nomor buku: ")) - 1

if 0 <= pilih < len(buku) and status[pilih]:
    hari_pinjam = input("Hari pinjam (Senin - Jumat): ").capitalize()
    hari_kembali = input("Hari kembali (Senin - Jumat): ").capitalize()

    if hari_pinjam in hari_sekolah and hari_kembali in hari_sekolah:
        index_pinjam = hari_sekolah.index(hari_pinjam)
        index_kembali = hari_sekolah.index(hari_kembali)

        if index_kembali >= index_pinjam:
            lama = index_kembali - index_pinjam + 1
            print(f"\nLama pinjam: {lama} hari")

            if lama > batas_pinjam:
                telat = lama - batas_pinjam
                denda = telat * denda_per_hari
                print(f"Selamat {nama} pengembalian anda berhasil. Namun, anda terlambat {telat} hari. Denda: Rp{denda}")
            else:
                print("Selamat {nama} pengembalian anda berhasil. Tidak ada denda.")

            status[pilih] = False  # Tandai buku sebagai tidak tersedia
            print("✅ Buku berhasil dipinjam.")
        else:
            print("Hari kembali tidak boleh sebelum hari pinjam.")
    else:
        print("Input hari salah.")
else:
    print("Buku tidak tersedia atau pilihan salah.")