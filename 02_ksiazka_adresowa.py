dane_adr = {}
dane_adr["Nowak Anna"] = ("Poznań", "anna.nowak@gmail.com", "666-111-333")
dane_adr["Kaczmarek Jan"] = ("Wrocław", "jan.kaczmarek@op.pl", "665-123-456")
dane_adr["Dzwonek Joanna"] = ("Poznań", "askadzwo@op.pl", "222-343-545")
dane_adr["Baggins Frodo"] = ("Shire", "shireishere@mordor.com", "234-654-098")


wybor = input('Wpisz liczbę aby:\n'
		'(1) - wyświetlić książkę adresową\n'
		'(2) - dodać wpis do książki\n'
		'(3) - usunąć wpis z książki\n'
		'(4) - zakończyć pracę programu\n')

if wybor == '1':
    for nazwisko in dane_adr.items():
        print(nazwisko)

if wybor == '2':
    for nazwisko in dane_adr.items():
        print(nazwisko)

if wybor == '3':
    for nazwisko in dane_adr.items():
        usuniete = input("Podaj Nazwisko i imię osoby do wykreślenia z książki:")
        print(dane_adr.pop(usuniete))

if wybor == '4':
    print(" ")



