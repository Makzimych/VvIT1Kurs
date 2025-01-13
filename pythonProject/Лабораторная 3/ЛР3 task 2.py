def read_file():
    task=input('Введите "1" для записи или "2" для добавления текста: ')
    if task=='1':
        user_input=input('Введите текст для записи в файл: ')
        with open('2.txt', 'a+', encoding='utf-8') as file:
            file.write(user_input)
        print('Текст записан в текстовый документ')
    elif task=='2':
        user_input=input('Введите текст для добавления: ')
        with open('2.txt', 'a+', encoding='utf-8') as file:
            file.write('\n' + user_input)
            print('Текст добавлен в текстовый документ')
    else:
        print('Некорректный ввод.')
read_file()