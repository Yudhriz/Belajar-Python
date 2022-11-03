#Buat Program mnggunakan logika if utk menghitung nilai
#Input
nama = input("Masukkan nama Anda? ")
kelas = input("Masukkan kelas Anda? ")
nilai = int(input("Masukkan nilai Anda? "))

#Proses
if nilai < 101 and nilai > 89:
    ket = "istimewa"
elif nilai < 90 and nilai > 69:
    ket = "sangat bagus"
elif nilai < 70 and nilai > 59:
    ket = "cukup"
else :
    ket = "gagal"

#Output
print("Nama saya ",nama)
print("Kelas saya ",kelas)
print("Nilai saya ",nilai)
print("Kamu dinyatakan",ket)