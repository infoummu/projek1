 # Contoh fungsi 1: 
 # Isi/copy-paste code contoh 1 dibawah:
def sapa_nama(nama):
    print(f"Nama anda : {nama}! Selamat datang.")

sapa_nama("Ami")
sapa_nama("Qusay")
# fungsi pertama saya berhasil OK.

# Batas, berikutnya Contoh fungsi 2:
print("-" * 25)
print("FUNGSI KE-2, Berikut: ")
print("-" * 25)
#----------------------------

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

angka_pertama = 5
angka_kedua = 3
jumlah = tambah(angka_pertama, angka_kedua)
print(f"Hasil penjumlahan: {jumlah}")

print(f"Hasil 10 + 7 adalah: {tambah(10, 7)}") # Bisa langsung digunakan

# Batas, berikutnya Contoh fungsi 3:
#print("-" * 25)

# ini baris tambahan untuk test git 