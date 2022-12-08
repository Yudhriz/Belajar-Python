#Buat Program mnggunakan logika if utk praktikum
#Input
nama = input("Masukkan nama Anda? ")
kelas = input("Masukkan kelas Anda? ")
lab = input("Gimana kondisi lab skrg? ")

#Proses
if lab == "tersedia":
    ket = "praktikum"
elif lab == "penuh":
    ket = "pindah jadwal"
else :
    ket = "tidak jadi praktikum"

#Output
print("Nama saya",nama)
print("Kelas saya",kelas)
print("Kondisi lab hari ini adalah",lab)
print("Maka kamu harus",ket)