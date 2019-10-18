#  Zadanie 9

from cwiczenia02 import file_manager

file_name = input("Na jakim pliku chcesz operować? Wprowadź nazwę wraz z rozszerzeniem: ")
file = file_manager.FileManager(file_name)
text = input("Jaki ciąg znaków dopisać do pliku? Wprowadź: ")
file.update_file(text)
print("Teraz odczytamy dane z pliku: ")
file.read_file()
