# Zadanie 7


def read_from_back(text):
    for i in range(len(text)-1, -1 , -1):
        print(text[i], end='')


string = input("Wprowadź dowolny ciąg znaków: ")
print("Wynik: ", end='')
read_from_back(string)


