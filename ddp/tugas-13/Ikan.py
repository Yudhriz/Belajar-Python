from Animal import *
class Ikan(Animal):
    def __init__(self,name,makanan,hidup,berkembang_biak,habitat,panjang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.panjang = panjang
    def cetak(self):
        super().cetak()
        print(f"Habitatnya di {self.habitat}")
        print(f"panjang {self.panjang}")
    def bernapas(self):
        print(f"{self.name} bernapas dengan insang.")
    def berenang(self):
        print(f"{self.name} berenang dengan sirip.")