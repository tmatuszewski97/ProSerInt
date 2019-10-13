imie = "Tomasz"
nazwisko = "Matuszewski"

# Zadanie 4

print(dir(imie))
help(imie.replace("masz", "biasz"))

# Zadanie 5

print("Imie i nazwisko odwrotnie, zaczynające się z wielkiej litery:",
      imie.lower()[::-1].capitalize(), nazwisko.lower()[::-1].capitalize())

# Zadanie 6

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista1[5:]
lista1 = lista1[:5]
print("lista pierwsza:", lista1, ", lista druga: ", lista2)

# Zadanie 7

lista3 = lista1 + lista2
lista3.insert(0, 0)
lista3_kopia = lista3
lista3_kopia.sort(reverse=True)
print("lista połączona, poprzedzona 0 i posortowana malejąco:", lista3_kopia)

# Zadanie 8

studenci = ((145584, "Jan Nowak"), (145769, "Dariusz Kowalski"), (137432, "Karol Szpakowski"),
            (143523, "Aleksandra Nowicka"), (136734, "Marta Janosz"))

# Zadanie 9

slownik = dict(studenci)
slownik[145584] = {"Jan Nowak", "19 lat", "nowak123@gmail.com", 2000, "Olsztyn"}
slownik[145769] = {"Dariusz Kowalski", "25 lat", "dkowalski@gmail.com", 1994, "Siedlce"}
slownik[137432] = {"Karol Szpakowski", "26 lat", "szpaku1993@o2.pl", 1993, "Warszawa"}
slownik[143523] = {"Aleksandra Nowicka", "22 lat", "nowicka_a@wp.pl", 1997, "Olsztyn"}
slownik[136734] = {"Marta Janosz", "20 lat", "nowicka_a@wp.pl", 1999, "Radom"}

# Zadanie 10
lista = [583024382, 573921423, 426342165, 583024382, 123456789, 426342165]
print("Lista numerów przed wykluczeniem powtórzeń:", lista)
lista = set(lista)
print("Lista numerów po wykluczeniu powtórzeń:", lista)

# Zadanie 11

print("Wypisanie liczb od 1 do 10: ")
for i in range(1, 11):
    print(i, end=' ')

# Zadanie 12

print("\nWypisanie liczb od 100 do 20, co 5 wartości: ")
for i in range(100, 19, -5):
    print(i, end=' ')

# Zadanie 13

print("")
zdanie = ''
lista_slownikow = [{1: "Dariusz Kowalski", 2: "Jan Nowak", 3: "Kamil Janowicz"}, {1: "Audi A6", 2: "BMW E36",
                                                                                  3: "Aston Martin DB9"}]
for slownik in lista_slownikow:
    for wartosc in slownik.values():
        zdanie += wartosc + " "
print(zdanie)
