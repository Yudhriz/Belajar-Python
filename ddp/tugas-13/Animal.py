class Animal:
    name = ""
    makanan = ""
    hidup = ""
    berkembang_biak = ""
    
    def __init__(self,name,makanan,hidup,berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print(f"Nama : {self.name}")
        print(f"makanan : {self.makanan}")
        print(f"Hidup di : {self.hidup}")
        print(f"Berkembang biak : {self.berkembang_biak}\n")