users = {"admin": "1234"}
secret_info = "42"

def loggest():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password

def login():
    login, password = loggest()

    if login in users.keys():
        if users[login] == password:
            print("Welcome")
            print(secret_info)
    else:
        print("Неверный пароль")

def registred():
    login, password = loggest()
    if login in users.keys():
        print("Логин занят")
    else:
        users[login] = password
        print("Успешная регистрация")

def delete():
    login, password = loggest()
    if login in users.keys():
        if password == users[login]:
            del users[login]
            print("Получилось")
        else:
            print("Нет такой учетки")


while True:
    q1 = input("Вход или регистрация, а может удалить учетку? : ").lower()
    if q1 == "вход":
        login()
    elif q1 == "регистрация":
        registred()
    elif q1 == "удалить":
        delete()
    break

