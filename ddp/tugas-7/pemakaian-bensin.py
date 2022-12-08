#Buat Program harga bensin ke kota tujuan
#Declare
pLite = 10000
pMax = 14000
pTurbo = 17000

jTempuhPLite = 12
jTempuhPMax = 13
jTempuhPTurbo = 13.5

jakarta = 20
bekasi = 35.7
depok = 5
tangerang = 99
bogor = 120.6

#Input
nKen = input("Nama Kendaraan? ")
jBen = input("Jenis Bensin? ")
KotaT = input("Kota yang dituju? ")

#Proses
if (jBen == 'pertalite'):
    hasilPakai = eval(KotaT) / jTempuhPLite
    totalHarga = hasilPakai * pLite
elif (jBen == 'pertamax'):
    hasilPakai = eval(KotaT) / jTempuhPMax
    totalHarga = hasilPakai * pMax
elif (jBen == 'pertamax turbo'):
    hasilPakai = eval(KotaT) / jTempuhPTurbo
    totalHarga = hasilPakai * pTurbo
else :
    print('ERROR')

#Rounding
hasilPakai = round(hasilPakai, 2)
totalHarga = round(totalHarga)

#Output
print("==========================================")
print("Nama Kendaraan = ",nKen)
print("Jenis Bensin = ",jBen)
print("Kota yang dituju = ",KotaT)
print("Pemakaian Bensin =",hasilPakai,"L")
print("Total Harga dari Bensin = ","Rp",totalHarga)