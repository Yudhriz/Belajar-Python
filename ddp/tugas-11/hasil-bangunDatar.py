# 1) Buatlah modul bangun datae utk menghitung luas (min 5)

import bangun_datar

# Menghitung luas persegi dengan sisi 4
luas_persegi = bangun_datar.luas_persegi(4)
print(f"Luas persegi\t\t: {luas_persegi}")

# Menghitung luas persegi panjang dengan panjang 5 dan lebar 7
luas_persegi_panjang = bangun_datar.luas_persegi_panjang(5, 7)
print(f"Luas persegi panjang\t: {luas_persegi_panjang}")

# Menghitung luas lingkaran dengan jari-jari 8
luas_lingkaran = bangun_datar.luas_lingkaran(8)
print(f"Luas lingkaran\t\t: {luas_lingkaran}")

# Menghitung luas segitiga dengan alas 10 dan tinggi 6
luas_segitiga = bangun_datar.luas_segitiga(10, 6)
print(f"Luas segitiga\t\t: {luas_segitiga}")

# Menghitung luas trapesium dengan alas atas 10, alas bawah 12, dan tinggi 8
luas_tranpesium = bangun_datar.luas_trapesium(10, 12, 8)
print(f"Luas tranpesium\t\t: {luas_tranpesium}")