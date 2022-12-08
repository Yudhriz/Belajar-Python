#program menghitung berat badan ideal (BMI)
#input
berat =  int(input('Masukkan berat kamu (kg) \t= '))
tinggi = int(input('Masukkan tinggi kamu (cm) \t= '))
tinggi = tinggi/100 #konversi ke meter

#rumus
BMI = berat/(tinggi**2)

#output
print("Nilai BMI kamu = ",BMI)

#Logika if else
if BMI < 18.5:
    print('Berat badan kamu masih kurang')
elif BMI > 18.5 and BMI < 24.9:
    print('Berat kamu sudah normal',)
elif BMI > 25 and BMI < 29.9:
    print('Berat kamu sudah meiebihi')
elif BMI > 30:
    print('Berat kamu sudah obesitas')