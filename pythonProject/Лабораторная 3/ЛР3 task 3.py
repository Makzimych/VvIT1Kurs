def read_file(name,type='r'):
    try:
        with open(name,'r') as file:
                if type=='all':
                    content=file.read()
                    print(content)
                elif type=='lines':
                    for line in file:
                        print(line)
                else:
                    print('Неправильный выбор чтения,выберите "all" или "lines".')
    except FileNotFoundError:
        print(f'Файл "{name}" не существует,пожалуйста,проверьте наличие файла ')
read_file('1.txt','all')