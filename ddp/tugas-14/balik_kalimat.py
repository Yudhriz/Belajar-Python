# Buatlah program dengan menampilkan kalimat yang dibalik
def balik_kalimat(kata):
    kata = kata.split()
    backward = ""
    for x in range(len(kata)):
        x += 1
        backward = backward + kata[-x] + " "
    return backward

print(balik_kalimat("saya mahasiswa Nurul Fikri"))
print(balik_kalimat("saya prodi Teknik Informatika"))
print(balik_kalimat("Pemrograman Dasar Menyenangkan"))