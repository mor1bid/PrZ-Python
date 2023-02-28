def edit():
    targ = input('Введите номер желаемой заметки: ')
    targ = targ + '.'
    with open('ntbk.txt', 'w', encoding='UTF-8') as ntbk:
        for ln in ntbk:
            if targ in ln:
                ntext = input('Введите заметку:\n')
                nln = targ + ntext
                res = ln.replace(ln, nln)
                ntbk.write(res)
            elif ln == '':
                print('Запрошенного номера не найдено.')
    ntbk.close()
    pass