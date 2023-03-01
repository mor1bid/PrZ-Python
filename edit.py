def edit():
    targ = input('Укажите ошибку в вашей заметке: ')
    ntext = input('Введите замену: ')
    with open('ntbk.txt', 'r', encoding='UTF-8') as ntbk:
        note = ntbk.read()
        note = note.replace(targ, ntext, 1)
        with open('ntbk.txt', 'w', encoding='UTF-8') as ntbk:
            ntbk.write(note)
    print('\nВыполнено!\n')
    ntbk.close()
    pass