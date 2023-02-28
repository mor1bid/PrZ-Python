def edit():
    targ = input('Введите номер желаемой заметки: ')
    targ = targ + '.'
    with open('ntbk.txt', 'w', encoding='UTF-8') as ntbk:
        for ln in ntbk:
            if targ in ln:
                ntext = input('Введите заметку:\n')
    ntbk.close()
    pass