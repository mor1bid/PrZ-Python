def create():
    with open('ntbk.txt', 'a', encoding='UTF-8') as ntbk:
        text = input('Введите заметку:\n')
        ntbk.writelines(text)
    pass