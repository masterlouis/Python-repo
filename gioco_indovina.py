import random

numero_casuale = random.randint(0, 100)
tentativi = 0
n_tentativo = 0
while True:
    tentativo = int(input("indoviana il numero: "))
    tentativo += 1
    n_tentativo += 1
    if tentativo == numero_casuale:
        print("Hai vinto al", n_tentativo, "tentativo!!!")
    elif tentativo<numero_casuale:
        print("il numero è troppo piccolo")
    else:
        print("il numero è troppo grande")