user_text = input('Введите текст для записи в файл: ')

with open('user_input.txt', 'w', encoding='utf-8') as file:
    file.write(user_text + '\n')

print('Текст записан')

while True:
    more_text = input('Введите текст для добавления в файл(или нажмите Enter чтобы выйти): ')
    if more_text == '':
        break
    with open('user_input.txt', 'a', encoding='utf-8') as file:
        file.write(more_text + '\n')

    print('Текст добавлен')