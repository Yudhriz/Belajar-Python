from Animal import *
class Badak(Animal):
    def __init__(self,name,makanan,hidup,berkembang_biak,habitat,berat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.berat = berat
    def cetak(self):
        super().cetak()
        print(f"Habitatnya di {self.habitat}")
        print(f"berat {self.berat}")
    def bernapas(self):
        print(f"{self.name} bernapas dengan paru - paru")
    def karakteristik(self):
        print(f"{self.name} termasuk hewan herbivora")