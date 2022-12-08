listA = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def duplicate(listA):
    listB = listA.copy()

    listA[1] = "pepaya"
    listA[2] = "mangga"
    listA[3] = "mangga"
    listA[4] = "pisang"

    listB[0] = "pisang"
    listB[1] = "durian"
    listB[2] = "durian"
    listB[3] = "jambu"

    listNew = listA+listB
    listA.extend(listNew)
    return listNew

listNew = duplicate(listA)
print(f"Hasilnya = \n{listNew}")
