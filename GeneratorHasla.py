#Dodać zapis do csv, automatyczne wyszukiwanie i wykrywanie powtórzeń.

import string
import sys
import secrets
import os
import csv
import pandas as pd

always_true_until_false = True
desktop = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
sciezka_txt = desktop + '\\' + 'Hasła.txt'
sciezka_csv = desktop + '\\' + 'Hasła.csv'
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

def sprawdz_typ(wartosc):
    try:
        val = int(wartosc)
    except ValueError:
        print("Nieprawidłowa wartość.")
        sys.exit(0)

def generowanie_hasla():
    target = str.upper(input ('Do czego potrzebujesz hasła? '))
    size = int(input('Wprowadź długość hasła: '))
    sprawdz_typ(size)
    if size <= 0:
        print('Długość hasła musi być dłuższa od 0.')
        sys.exit(0)
    haslo = ''
    for i in range(size):
        k = secrets.choice(chars)
        haslo += k
    row = [target, haslo]       
    file_csv = open(sciezka_csv, 'a')
    file_csv_write = target + ', ' + haslo + '\n'
    file_csv.write(file_csv_write)

while always_true_until_false:
    opcja = input("Wybierz opcję: Dodanie hasła (1), albo odczytanie hasła (2), albo zakończ działanie programu (3): ")
    opcja_int = int(opcja)
    sprawdz_typ(opcja_int)
    if opcja_int == 1:
        opt1_true = True
        while opt1_true:
            generowanie_hasla()  
            dane = pd.read_csv(sciezka_csv, names=['Domena', 'Hasła '])
            print(dane)
            opt1_val = input("Chcesz wyjść z opcji nr 1? (T/N): ")
            if opt1_val == 'T' or opt1_val == 't':
                opt1_true = False
    elif opcja_int == 2:
        opt2_true = True
        while opt2_true:
            domena = str.upper(input("Do jakiej domeny poszukujesz hasła? "))
            reader = csv.reader(open(sciezka_csv, 'r'))
            slownik = {}
            for row in reader:
                k, v = row
                slownik[k] = v
            if domena in slownik:
                print('Hasło dla: ' + domena + " to: " + slownik[domena])
            else:
                print("Nie ma hasła dla takiej domeny")
            opt2_val = input("Chcesz wyjść z opcji nr 1? (T/N): ")
            if opt2_val == 'T' or opt2_val == 't':
                opt2_true = False
    elif opcja_int == 3:
        print('Wybrano zakończenie programu')
        always_true_until_false = False       
        sys.exit(0)