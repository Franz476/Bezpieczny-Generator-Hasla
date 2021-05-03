import string
import sys
import secrets
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
sciezka = str(desktop) + '\\' + 'Hasła.txt'

target = input ('Do czego potrzebujesz hasła? ')
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

for i in range(size):
    k = secrets.choice(chars)
    #print(k)
    haslo += k

line = haslo + '                 ' + target + '\n'

#print(desktop)
print(sciezka)
print(line)
file = open(sciezka, 'a+')
file.write(line)
