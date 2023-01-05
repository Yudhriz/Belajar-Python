from Kantin import *

kantin = Kantin()

print(f'='*40)
konsumen1 = Konsumen('Yudha', 500000)
konsumen1.pesan(kantin, {'ayam goreng': 2, 'kopi': 1})

print(f'='*40)
konsumen2 = Konsumen('Alvingky', 30000)
konsumen2.pesan(kantin, {'nasi goreng': 1, 'teh manis': 2, 'sate': 1})

print(f'='*40)
konsumen3 = Konsumen('Joko', 1000)
konsumen3.pesan(kantin, {'nasi goreng': 1, 'teh manis': 2, 'sate': 1})