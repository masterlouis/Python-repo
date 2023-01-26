def trova_pari(numeri):
    numeripari = []
    for num in numeri:
        if num % 2 == 0:
            numeripari.append(num)
    return numeripari
numeri = []
num = input("inserisci i numeri: ")
numeri.append(num)
print(trova_pari(numeri))