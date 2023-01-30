def trova_pari(numeri):
    numeripari = []
    for num in numeri:
        if num % 2 == 0:
            numeripari.append(num)
    return numeripari
numeri = []
while True:
    num = input("inserisci i numeri: ")
    if num == 'q':
        break
    numeri.append(int (num))
print(trova_pari(numeri))