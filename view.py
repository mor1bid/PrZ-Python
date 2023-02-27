with open('ntbk.txt', 'r', encoding='UTF-8') as ntbk:
    text = ntbk.readlines()
    print('\n')
    for ln in text:
        print(ln)