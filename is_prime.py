def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("inserisci il numero che ritireni primo"))
if is_prime(num):
    print("questo è un numero primo: ")
else:
    print("NON è UN NUMERO PRIMO")