import view, edit, create, delete
i = 0
print('Здравствуйте!', end=' ')
while True:
    menu = input('Введите желаемый пункт меню:\n(1) Показать заметки\n(2) Редактировать заметки\n(3) Создать заметку\n(4) Удалить заметку')
    if menu == 1:
        view()
    elif menu == 2:
        edit()
    elif menu == 3:
        create()
    elif menu == 4:
        delete()
    else:
        print('Ошибка!')