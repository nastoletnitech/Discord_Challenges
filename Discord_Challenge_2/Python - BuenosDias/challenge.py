from random import randint
from math import sqrt
from functools import reduce

POLSKIE_ZNAKI = {
    'ą': 'a',
    'ę': 'e',
    'ć ': 'c',
    'ł': 'l',
    'ń': 'ń',
    'ó': 'o',
    'ś': 's',
    'ó': 'o',
    'ź': 'z',
    'ż': 'z'
}

def wyklucz_pol_znaki(string):
    for key, value in POLSKIE_ZNAKI.items():
        string = string.replace(key, value)
    return string

imie, nazwisko = map(wyklucz_pol_znaki, input('Podaj swoje dane > ').title().split(maxsplit=1))
print(imie, nazwisko)

while True:
    pierwiastek = randint(1, 10)
    try:
        if float(input(f'Witaj {imie[0] + nazwisko}, aby przejść dalej powiedz jaki jest pierwiastek z {pierwiastek} ')) == round(sqrt(pierwiastek), 2):
            break
    except ValueError:
        pass
    print('Nieudalo sie :( Sproboj ponownie')

CHOICES = {
    'Dodawanie': [lambda x, y: x + y, 'dodac'],
    'Odejmowanie':[lambda x, y: x - y, 'odjac'],
    'Mnożenie': [lambda x, y: x * y, 'pomnozyc'],
    'Dzielenie': [lambda x, y: x / y, 'podzielic']
}

def menu():
    print('Co chcesz zrobić? Wpisz cyfrę opcji, aby wykonać działanie.')
    
    for i, choice in enumerate(CHOICES.keys()):
        print(f'{i + 1}. {choice}')

    choice = list(CHOICES.items())[int(input()) - 1]
    return choice

zn = 'z'
while True:
    if zn == 'z':
        choice = menu()
    elif zn != 'n':
        print('Zly wybor')
        break
    liczby = list(map(int, input(f'Podaj liczby ktore chcesz {choice[1][1]} ').replace(',', '').split()))
    zn = input(f"Wynik dzialania to {reduce(choice[1][0], liczby)}, wpisz ( na przykład ) 'z' aby wrócić do wyboru działania, lub 'n' aby obliczyć kolejne działanie. ")