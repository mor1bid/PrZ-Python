def delete():
    move = input('Очистить заметки полностью? (y/n/c)')
    if move == 'y':
        with open('ntbk.txt', 'w') as ntbk:
            ntbk.seek(0)
            ntbk.truncate
    elif move == 'n':
        targ = input('Введите номер желаемой заметки: ')
    print('Выполнено.')
    pass