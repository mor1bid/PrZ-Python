def view():
    print('Ваши заметки:\n')
    with open('ntbk.txt', 'r', encoding='UTF-8') as ntbk:
        text = ntbk.readlines()
        for ln in text:
            print(ln)
        print('\n')
    pass