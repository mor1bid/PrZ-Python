def edit():
    targ = input('Введите номер желаемой заметки: ')
    targ = targ + '.'
    with open('ntbk.txt', 'r', encoding='UTF-8') as ntbk:
        note = ntbk.readlines()
        for line in ntbk:
            if targ in line:
                ntext = input('Введите заметку:\n')
                nln = targ + ntext
                # res = note.replace(line, nln)
                with open('ntbk.txt', 'w', encoding='UTF-8') as ntbk:
                    ntbk.seek(0)
                    for ln in note:
                        if targ not in ln:
                            ntbk.write(ln)
                        else:
                            ntbk.write(nln)
                print('\nВыполнено!\n')
            elif line == '':
                print('Запрошенного номера не найдено.')
    ntbk.close()
    pass