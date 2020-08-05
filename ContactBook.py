import sqlite3
from colorama import Fore, Style

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    number BIGGINT
)''')

db.commit()


def del_contact():
    delete_name = input('Какой контакт хотите удалить?:')
    sql.execute(f'SELECT name FROM users WHERE name = "{delete_name}"')
    if sql.fetchone() is None:
        print(Fore.RED + "Такого контакта не существует" + Style.RESET_ALL)
    else:
        sql.execute(f'DELETE FROM users WHERE name = "{delete_name}"')
        db.commit()
        print(Fore.GREEN + "Контакт удален" + Style.RESET_ALL)


def new_contact(user_name=None):
    if user_name is None:
        user_name = input('Name: ')
    else:
        print('Name: ' + user_name)
    user_number = input('Number: ')

    sql.execute(f'SELECT name FROM users WHERE name = "{user_name}"')
    if sql.fetchone() is None:
        sql.execute(f'INSERT INTO users VALUES (?,?)', (user_name, user_number))
        db.commit()
        print(Fore.GREEN + 'Зарегистрировано!' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Контакт с таким именем уже есть!' + Style.RESET_ALL)


def renumber():
    rename = input("Имя контакта для изменения номера:")
    sql.execute(f'SELECT name  FROM users WHERE name = "{rename}"')
    if sql.fetchone() is None:
        print(Fore.RED + "Контакта с таким именем не существует" + Style.RESET_ALL)
        new_contact(rename)
    else:
        new_number = int(input("Введите новый номер:"))
        sql.execute(f"UPDATE users SET number = {new_number} WHERE name = '{rename}'")
        db.commit()
        print(Fore.GREEN + "Номер контакта изменен" + Style.RESET_ALL)


def main():
    print("===========================\n"
          "1 - Cоздать новый контакт\n"
          "2 - Изменить номер контакта\n"
          "3 - Вывести все контакты\n"
          "4 - Удалить контакт\n"
          "===========================")
    i = int(input("Выбирете пункт:"))
    if i == 1:
        new_contact()
    elif i == 2:
        renumber()
    elif i == 3:
        for value in sql.execute('SELECT * FROM users'):
            print(value)
    elif i == 4:
        del_contact()
    else:
        print(Fore.RED + 'Введите корректный номер' + Style.RESET_ALL)


while True:
    main()
