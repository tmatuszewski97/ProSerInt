# Zadanie 1

napis = """Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. 
Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. 
Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. 
Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum,
a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach
 osobistych, jak Aldus PageMaker"""

# Zadanie 2

imie = "Tomasz"
nazwisko = "Matuszewski"
litera_1 = imie[2]
litera_2 = nazwisko[3]
print("W tekście jest", napis.count(litera_1), "liter", litera_1, "oraz", napis.count(litera_2), "liter", litera_2)