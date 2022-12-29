from Animal import *
from Badak import *
from Ikan import *
from Ular import *

# Objek
b1 = Badak('Badak bercula satu','tunas','darat','beranak','dataran rendah','> 1 ton')
b1.cetak()
b1.bernapas()
b1.karakteristik()

print(f"="*50)

i1 = Ikan('Cupang','jentik nyamuk','air','bertelur','perairan dangkal','6-8 cm')
i1.cetak()
i1.bernapas()
i1.berenang()

print(f"="*50)

u1 = Ular('Ular Sawah','tikur','amphibi','bertelur','sawah','1-75 kg')
u1.cetak()
u1.bernapas()
u1.merayap()