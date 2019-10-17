# Zadanie 3


def delete_letters(text, letter):
    text = str(text)
    for i in text:
        if i == letter:
            text = text.replace(i, '')
    return text


string = input("Wprowadź dowolny ciąg znaków: ")
char = input("Której litery chciałbyś się pozbyć? ")
new_string = delete_letters(string, char)
print('Wynik:', new_string)
