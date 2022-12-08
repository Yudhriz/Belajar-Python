#Buat Program mnggunakan logika if utk roler coster dg tinngi min 90 cm blh main dan dibawah 90 tdk blh main
#Input
nama = input("Masukkan nama Anda? ")
umur = input("Masukkan umur Anda? ")
tinggi = int(input("Masukkan tinggi Anda? "))

#Proses
if tinggi > 89:
    ket = "Boleh bermain Roler Coster"
else :
    ket = "Tidak boleh bermain Roler Coster"

#Output
print("Nama saya ",nama)
print("Umur saya ",umur,"Thn")
print("Tinggi saya ",tinggi,"cm")
print("Kamu ",ket)