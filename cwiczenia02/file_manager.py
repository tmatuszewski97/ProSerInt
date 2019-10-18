# Zadanie 8


class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as file_reader:
            for line in file_reader:
                print(line, end='')

    def update_file(self, text_data):
        with open(self.file_name, 'a') as my_file:
            my_file.write(text_data)
