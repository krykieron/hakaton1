# Program przechowujący danę kontaktowe znajomych/klientów.

dane_adresowe = [['Imię', 'Anna'], ['Nazwisko', 'Nowak'], ['Telefon', '000 111 222'], ['e-mail', 'anna.nowak@gmail.com']]
# Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie.

#Zadania to:
wybor = input('Napisz to co w nawiasie aby:\n'
              '(ks) wyświetlić książkę adresową\n'
              '(do) dodać wpis do książki\n'
              '(us) usunąć wpis do książki\n'
              '(x) zakończyć pracę programu\n')

# Wyświetlenie wszystkich wpisów
if wybor == 'ks':
    adresy_format = dict(dane_adresowe)
    print('Książka adresowa:\n')

    for kolumna1, kolumna2 in adresy_format.items():
        print(kolumna1, ':::', kolumna2)

# Stworzenie nowego wpisu (dane wczytywane z klawiatury)
if wybor == 'do':
    dodane_adresy = []
    dodane = int(input("Ile pozycji chcesz dodać?: "))

    for _ in range(dodane):
        costam = input("Wpisz oddzielając spacjami pozycje, który chcesz dodać:")
        dodane_adresy.append(costam)

# Usunięcie wpisu
    if wybor == 'us':
        usuniete_adresy = []
    usuniete = int(input("Ile pozycji chcesz usunąć?: "))

    for _ in range(usuniete):
        kasowane_cosie = input("Wpisz oddzielając spacjami pozycje, który chcesz dodać:")
        dodane_adresy.append(kasowane_cosie)
    dane_adresowe.remove()
    # Zakończenie pracy programu
else:
    print('Dziękuję')

