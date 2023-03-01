def edit():
    numbr = input('Введите номер заметки: ')
    numbr = numbr + '.'
    targ = input('Укажите ошибку в вашей заметке: ')
    ntext = input('Введите замену: ')
    with open('ntbk.txt', 'r', encoding='UTF-8') as ntbk:
        note = ntbk.read()
        for ln in ntbk:
            if numbr in ln:
                note = note.replace(targ, ntext, 1)
        # note = note.replace(targ, ntext, 1)
    with open('ntbk.txt', 'w', encoding='UTF-8') as ntbk:
        ntbk.write(note)
    print('\nВыполнено!\n')
            # elif line == '':
            #     print('Запрошенного номера не найдено.')
    ntbk.close()
    pass