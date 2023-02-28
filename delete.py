def delete():
    import os, os.path
    move = input('Очистить заметки полностью? (y)es/(n)o/(c)ancel: ')
    if move == 'y':
        with open('ntbk.txt', 'w') as ntbk:
            ntbk.seek(0)
            ntbk.truncate
            if os.path.isfile('clog.txt'):
                os.remove('clog.txt')
        print('\nВыполнено!\n')
    elif move == 'n':
        targ = input('Введите номер желаемой заметки: ')
        with open('ntbk.txt', 'r', encoding='UTF-8') as ntbk:
            text = ntbk.readlines()
            with open('ntbk.txt', 'w', encoding='UTF-8') as ntbk:
                ntbk.seek(0)
                for ln in text:
                    if targ not in ln:
                        ntbk.write(ln)
        print('\nВыполнено!\n')
    elif move == 'c':
        print('\nВыполнено!\n')
    else:
        print('\nОшибка!\n')
    pass