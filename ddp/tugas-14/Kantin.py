class Kantin:
  def __init__(self):
    self.menu_makanan = {
      'ayam goreng': 10000,
      'nasi goreng': 8000,
      'mie goreng': 7000,
      'bakso': 9000,
      'sate': 11000
    }
    self.menu_minuman = {
      'teh manis': 3000,
      'kopi': 4000,
      'susu': 5000,
      'jus jeruk': 6000,
      'jus mangga': 7000
    }
  
  def cetak_struk(self, nama, uang, pesanan):
    total_harga = 0
    for p in pesanan:
      total_harga += p['harga']
    print(f'Nama: {nama}')
    print('Pesanan:')
    for p in pesanan:
      print(f'{p["nama"]} {p["jumlah"]} x {p["harga"]} = {p["jumlah"] * p["harga"]}')
    print(f'Total harga: {total_harga}')
    print(f'Uang yang dibawa: {uang}')
    print(f'Kembalian: {uang - total_harga}')

class Konsumen:
  def __init__(self, nama, uang):
    self.nama = nama
    self.uang = uang
  
  def pesan(self, kantin, pesanan):
    items = []
    for p in pesanan:
      item = {
        'nama': p,
        'jumlah': pesanan[p],
        'harga': kantin.menu_makanan[p] if p in kantin.menu_makanan else kantin.menu_minuman[p]
      }
      items.append(item)
    
    total_harga = 0
    for item in items:
      total_harga += item['jumlah'] * item['harga']
    
    if total_harga > self.uang:
      print('Maaf, uang Anda tidak cukup.')
    else:
      kantin.cetak_struk(self.nama, self.uang, items)
