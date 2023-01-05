# program dengan menampilkan bintang bintang segitiga

def segitiga_bintang(tinggi):
    for x in range(tinggi):
        for b in range(x + 1):
            print("*", end="")
        print()

def segitiga_terbalik(tinggi):
    for x in range(tinggi):
        for b in range(tinggi - x - 1):
            print("*", end="")
        print()

tinggi = 6

segitiga_bintang(tinggi)
segitiga_terbalik(tinggi)