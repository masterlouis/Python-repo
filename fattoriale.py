def calcola_fattoriale(numero):
    fattoriale = 1
    for i in range(1, numero + 1):
        fattoriale = fattoriale * i    
    return fattoriale

numero = int(input("inserisci il numero:"))
risultato = calcola_fattoriale(numero)
print("il fattoriale di", numero, "è", risultato)