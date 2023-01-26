def sommalista(numeri):
    totale = 0
    for num in numeri:
        totale += num
    return totale


#provo a chiamare la lista

list1 = [1, 2, 3, 4, 5]


print(sommalista(list1))