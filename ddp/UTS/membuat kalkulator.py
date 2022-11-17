# program membuat kalkulator
#Input
print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Bagi \t [/]')
print('  4. Kali \t [*}')
print('  5. Pangkat \t [**]')
print('  *Noted : JIka Pangkat angka kedua nya dikasih angka 0')

print('=' * 25)
a = int(input("Masukkan angka pertama? "))
b = int(input("Masukkan angka kedua? "))
po = input("Masukkan pilihan operator? ")

#Proses
if po == '1':
    hasil = a + b
elif po == '2':
    hasil = a - b
elif po == '3':
    hasil = a / b
elif po == '4':
    hasil = a * b
elif po == '5':
    hasil = a **2
else:
  print('Tidak valid')

#Output
print("Angka pertama = ",a)
print("Angka kedua = ",b)
print("Pilihan Operator = ",po)
print("Hasil Operator = ",hasil)