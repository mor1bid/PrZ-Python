def create():
    import os.path
    if os.path.isfile('clog.txt'):
        with open('clog.txt', 'r', encoding='UTF-8') as count:
            line = count.read()
            numbr = int(line)
    else:
        numbr = 1
    with open('ntbk.txt', 'a', encoding='UTF-8') as ntbk:
        ntbk.writelines(str(numbr))
        ntbk.write('. ')
        text = input('Введите заметку:\n')
        ntbk.write(text)
        ntbk.write('\n')
    numbr += 1
    with open('clog.txt', 'w') as count:
        count.write(str(numbr))
    print("\nВыполнено!\n")
    ntbk.close()
    count.close()
    pass