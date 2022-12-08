listA = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
listB = []
def Reversed(listA, listB):
    for i in range(len(listA)):
        reversed_i = len(listA) -1 - i
        listB.append(listA[reversed_i])

Reversed(listA, listB)
print(f"Hasil sebelum = \n{listA}") 
print(f"Hasil sesudah = \n{listB}")