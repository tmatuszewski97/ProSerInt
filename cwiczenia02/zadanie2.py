# Zadanie 2


def show_info(data_text):
    letters = []
    data_text = str(data_text)
    length = len(data_text)
    for i in data_text:
        letters.append(i)
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    result = {'length:': length, 'letters:': letters, 'big_letters:': big_letters, 'small_letters:': small_letters}
    return result


string = input("Wprowadź dowolny ciąg znaków: ")
info = show_info(string)
print('Wynik:', info)
