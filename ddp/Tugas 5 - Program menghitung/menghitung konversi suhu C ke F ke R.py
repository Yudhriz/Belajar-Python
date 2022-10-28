#program menghitung konversi suhu dari celcius ke fahrenheit ke reamur
#input
celcius = input ('Masukkan nilai celcius = ')
#rumus
fahrenheit = (9/5) * int(celcius) + 32
reamur = (4/5) * int(celcius)
kelvin = int(celcius) + 273

#output
print("Nilai celcius \t\t= ",celcius,"C")
print("Nilai fahrenheit \t= ",fahrenheit,"F")
print("Nilai reamur \t\t= ",reamur,"R")
print("Nilai kelvin \t\t= ",kelvin,"K")