# program menghitung luas dan keliling trapesium
#Input
a = int(input("Masukkan sisi A? "))
b = int(input("Masukkan sisi B? "))
c = int(input("Masukkan sisi C? "))
d = int(input("Masukkan sisi D? "))
t = int(input("Masukkan tinggi? "))

#Proses
luas = 1/2 * (a+b) * t
keliling = a+b+c+d

#Output
print("Hasil luas trapesium adalah = ",luas)
print("Hasil keliling trapesium adalah = ",keliling)