def read_file(file_name, read_type):
    if read_type == 1:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    elif read_type == 2:
        with open(file_name, 'r') as file:
            lines = ''
            for line in file:
                lines += line
            return lines
    else:
        return 'Введен неверный тип чтения'

file_name_input = input('Введите имя файла: ')
read_type_input = int(input('Введите тип чтения(1 - весь файл сразу, 2 - построчно): '))

print(read_file(file_name_input, read_type_input))