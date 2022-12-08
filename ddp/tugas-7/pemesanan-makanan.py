#Buat Program utk pemesanan restoran
#Input
nPembeli = input("Masukkan Nama Pembeli? ")
noHp = input("Masukkan No.Hp Pembeli? ")
psnMenu = input("Pesan Menu Apa? ")
#Proses Pesan Menu Apa
if psnMenu == 'makanan':
    print("Nasi Goreng = Rp 15.000")
    print("Mie Goreng = Rp 12.000")
    print("Ayam Gebrek = Rp 18.000")
elif psnMenu == 'minuman':
    print("Aneka Jus = Rp 15.000")
    print("Soft Drink = Rp 10.000")
    print("Sweet Ice Tea = Rp 5.000")
mskkanPsn = input('Masukkan Pesanan? ')
mskkanJmlhPsn = int(input("Masukkan Jumlah Pesanan? "))

#Proses
#----------Makanan------------
if mskkanPsn == 'nasi goreng':
    harga = 15000 * mskkanJmlhPsn
elif mskkanPsn == 'mie goreng':
    harga = 12000 * mskkanJmlhPsn
elif mskkanPsn == 'ayam geprek':
    harga = 18000 * mskkanJmlhPsn
#----------Minuman------------
if mskkanPsn == 'aneka jus':
    harga = 15000 * mskkanJmlhPsn
elif mskkanPsn == 'soft drink':
    harga = 10000 * mskkanJmlhPsn
elif mskkanPsn == 'sweet ice tea':
    harga = 5000 * mskkanJmlhPsn

#Output
print("Nama Pembeli = ",nPembeli)
print("No Hp Pembeli = ",noHp)
print("Menu yang di Pesan = ",mskkanPsn)
print("Jumlah pesanan = ",mskkanJmlhPsn)
print("Harga yang harus di bayarkan = ",harga)