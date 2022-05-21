users = {"admin": "1234"}
secret_info = "42"

while True:
    q1 = input("Вход или регистрация, а может удалить учетку? : ").lower()
    if q1 == "вход":
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login in users.keys():
            if users[login] == password:
                print("Welcome")
                print(secret_info)
                break
            else:
                print("Неверный пароль")
    elif q1 == "регистрация":
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if login in users.keys():
            print("Логин занят")
        else:
            users[login] = password
            print("Успешная регистрация")
    elif q1 == "удалить":
        login = input("Введите имя учетки которую хотите удалить: ")
        if login in users.keys():
            password = input("Введите пароль: ")
            if password == users[login]:
                del users[login]
                print("Получилось")
                break
        else:
            print("Нет такой учетки")

    else:
        print('Неверные данные (Введите Вход или регистрация)')
