def tambah(*args):
  hasil = 0
  for arg in args:
    hasil += arg
  print("Hasil dari penjumlahan adalah", hasil)
def kurang(*args):
  hasil = args[0]
  for arg in args[1:]:
    hasil -= arg
  print("Hasil akhir dari pengurangan adalah", hasil)
def kali(*args):
  hasil = 1
  for arg in args:
    hasil *= arg
  print("Hasil akhir dari perkalian adalah", hasil)
def bagi(*args):
  hasil = args[0]
  for arg in args[1:]:
    hasil /= arg
  print("Hasil akhir dari pembagian adalah", hasil)