from random import randint
from math import sqrt
 
slownikPolskaAscii = {
  'ą': 'a',
  'ć': 'c',
  'ę': 'e',
  'ł': 'l',
  'ń': 'n',
  'ó': 'o',
  'ś': 's',
  'ź': 'z',
  'ż': 'z'
}
 
 
def kalkulator(wybor):
  czynnosc = ["dodać", "odjąć", "pomnożyć", "podzielić"]
  print(f"Podaj liczby które chcesz {czynnosc[wybor-1]}")
  wejscie = input()
  try:
    liczby = [int(i) for i in wejscie.strip().split(',')]
  except:
    liczby = [int(i) for i in wejscie.split()]
 
  if wybor == 1:
    wynik = liczby[0]+liczby[1]
  elif wybor == 2:
    wynik = liczby[0]-liczby[1]
  elif wybor == 3:
    wynik = liczby[0]*liczby[1]
  elif wybor == 4:
    wynik = liczby[0]/liczby[1]
  print(f"Wynik działania to {wynik}, wpisz 'd' aby wrócić do wyboru działania, lub 'n' aby obliczyć kolejne działanie.")
 
  operacja = input().strip()
  if operacja == 'd':
    return 404
  elif operacja == 'n':
    return 200
 
def menu():
  wynik = 404
  while wynik==404:
    print("""
     1. Dodawanie
     2. Odejmowanie
     3. Mnożenie
     4. Dzielenie
     =====================================
   """)
    wybor = int(input())
   
    wynik = 200
    while wynik == 200:
      wynik = kalkulator(wybor)
 
 
dane = input("Podaj swoje dane: ")
dane = dane.strip()
for litera in slownikPolskaAscii:
  dane = dane.replace(litera, slownikPolskaAscii[litera])
 
try:
  nick = dane[0]+dane[dane.index(' ')+1:]
except:
  nick = dane[0]
losowa = randint(1,10)
 
print(f"Witaj {nick}, aby przejść dalej powiedz jaki jest pierwiastek z {losowa}.")
 
odpowiedz = 0
 
while(round(sqrt(losowa), 2) != odpowiedz):
  odpowiedz = round(float(input()),2)
  if round(sqrt(losowa), 2) != odpowiedz:
    print("Spróbuj ponownie")
 
print("Poprawnie")
 
menu()