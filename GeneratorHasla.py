import string
import random
import math
import sys
import secrets

size = int(input('Wprowadź długość hasła: '))
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
print(chars)

def sprawdz_typ(wartosc):
    try:
        val = int(wartosc)
        print("Prawidłowo wprowadzona wartość. Wynosi ona: ", val)

    except ValueError:
        print("Wprowadzono nieprawidłowy typ zmiennej.")
        sys.exit(0)

sprawdz_typ(size)

if size <= 0:
    print('Długość hasła musi być dłuższa od 0.')
    sys.exit(0)

haslo = ''
5
for i in range(size):
    k = secrets.choice(chars)
    print(k)
    haslo += k


print(haslo)
    
