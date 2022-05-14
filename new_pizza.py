# 1) Админ. управляет меню(добавляет, удаляет пиццу в меню)
# 2) Пользователь делает заказ(Выбирает из меню, автоматически рассчитывается стоимость)

# menu = {
#     'margarita': 400,
#     'peperoni': 600,
# }
import json


# f = open("test.json", "r")
# menu = json.load(f)
# f.close()

with open("test.json", "r") as f:
    menu = json.load(f)


def load_menu():
    f = open("test.json", "r")
    menu = json.load(f)
    f.close()
    return menu

def save_menu(menu):
    f = open("test.json", "w")
    json.dump(menu, f)
    f.close()





def add_pizza(name, price):
    menu = load_menu()
    if name in menu.keys():
        print("Такая пицца есть в меню")
    else:
        menu[name] = price
    save_menu(menu)


def remove_pizza(name):
    menu = load_menu()
    if name in menu.keys():
        print("Удаляем")
        del menu[name]
    else :
        print('Нет такой пиццы. Удалять нечего')
    save_menu(menu)

# list_keys = list(menu.keys())
# list_keys_str = ", ".join(list_keys)


def order_pizza():
    order = []
    cost = 0
    menu = load_menu()
    while True:
        q1 = input("Continue? ")
        if q1 == "No":
            break
        else:
            print("Наше меню: ")
            print(menu)
            pizza_name = input("Какую пиццу заказываем?: ")
            if pizza_name in menu.keys():

                order.append(pizza_name)
                cost += menu[pizza_name]
                print(f"Пицца добавлена в заказ. Ваш заказ на сумму {cost}")

    return {"order": order, "cost": cost}
    # или print({"order": order, "cost": cost})

if __name__ == "__main__":
    while True:
        q3 = input("Продолжаем?: ")
        if q3 == "yes":
            role = input("Ваша роль?: ")
            if role == "Admin":
                q2 = input("Добавить или удалить?: ")
                if q2 == "add":
                    name_pizza = input("Введите имя новой пиццы: ")
                    name_pizza = name_pizza.strip()
                    price = input("Введите стоимость: ")
                    #price_pizza = int(input("Введите стоимость: "))
                    add_pizza(name_pizza, price)  # сейчас используем позиционные аргументы
                    # или именованые аргументы т.е. можно в любом порядке вводить аргументы он сам найдет add_pizza(price=price, name=name)
                elif q2 == "remove":
                    name_pizza = input("Введите имя для удаляемой пиццы: ")
                    remove_pizza(name_pizza)
                f = open("test.json", "r")
                menu = json.load(f)
                print(menu)
                f.close()

            elif role == "User":
                print(order_pizza())
                # или order_pizza()
            else:
                print("Данные введены неверно")




add_pizza("carbonara", 600)
#print(menu)

