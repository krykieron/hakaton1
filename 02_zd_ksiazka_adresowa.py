# Program przechowujący danę kontaktowe znajomych/klientów.
ksiazka_adr = [
    ['Anna','Nowak','666-111-333','anna.nowak@gmail.com'],
    ['Jan','Kaczmarek','665-123-456','jan.kaczmarek@op.pl'],
    ['Frodo','Baggins','234-654-098','shireishere@mordor.com'],
    ['Joanna','Dzwonek','234-567-111','asiamar@op.pl'],
]
# Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie.

#Zadania to:
wybor = input('Napisz to co w nawiasie aby:\n'
              '(ks) wyświetlić książkę adresową\n'
              '(do) dodać wpis do książki\n'
              '(us) usunąć wpis do książki\n'
              '(x) zakończyć pracę programu\n')

# Wyświetlenie wszystkich wpisów
if wybor == 'ks':
    print('Książka adresowa:')
    for kolumna in ksiazka_adr:
        print(kolumna[0],'__',kolumna[1], '__', kolumna[2],'__',kolumna[3])

# Stworzenie nowego wpisu (dane wczytywane z klawiatury)

if wybor == 'do':
        uzupelnienie = input("Wpisz imię, nazwisko, numer telefonu i email który chcesz dodać:").split()
        new_record = [
            uzupelnienie[0],
            uzupelnienie[1],
            uzupelnienie[2],
            uzupelnienie[3],
        ]
ksiazka_adr.append(new_record)
print(ksiazka_adr)

# Usunięcie wpisu
if wybor == 'us':
    usuniecie = []
    usuniete = int(input("Ile pozycji chcesz usunąć?: "))

    for _ in range(usuniete):
        kasowane_cosie = input("Wpisz oddzielając spacjami pozycje, który chcesz dodać:")
        dodane_adresy.append(kasowane_cosie)
    dane_adresowe.remove()

# ksiazka_adr['prowiant'].remove('batonik')
# print(ksiazka_adr)
#
# # # Program ma wypisać ile rzeczy (prowiant + przedmioty) Harcerz ma w plecaku. Komunikat może brzmieć: "Harcerz ma 7 przedmiotów w plecaku.
# ile_rzeczy = len(ksiazka_adr['sprzęt']) + len(ksiazka_adr['prowiant'])
# print('Harcerz ma ', ile_rzeczy, ' przedmiotów w plecaku.')
#
# # # Rozszerzenie:
# # # Napisz funkcję kupno(), która będzie przyjmowała trzy parametry: kwota, przedmiot, ekwipunek. Funkcja nie będzie zwracała żadnej wartości.
#
# def kupno(kwota, przedmiot, ksiazka_adr):
#     print(f'Harcerz kupił {przedmiot} za {kwota} zł')
# # # Funkcja ta ma wyświetlić na ekranie komunikat "Harcerz kupił (przedmiot) za kwotę (kwota) zł".
# # # Funkcja ma odjąć z ekwipunku odpowiednią kwotę i dodać przedmiot.
# # # Dodaj w programie jeszcze jedną rzecz, którą harcerz kupi.
# # # Rozszerzenie 2:
# # # Dodaj do napisanej powyżej funkcji sprawdzanie, czy Harcerz ma Imię na zakup. Jeśli nie, wyświetl na ekranie stosowny komunikat i nie wprowadzaj żadnych zmian w ekwipunku. Aby zakończyć wykonywanie funkcji użyj wyrażenia return bez żadnej wartości do zwrócenia.
# #
# #
# #
# #
# #
# # # for k, v in dict_from_list.items():
# #     print(k, '->', v)