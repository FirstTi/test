# 1) Админ. управляет меню(добавляет, удаляет пиццу в меню)
# 2) Пользователь делает заказ(Выбирает из меню, автоматически рассчитывается стоимость)

menu = {
    'margarita': 400,
    'peperoni': 600,
}

def add_pizza(name, price):
    if name in menu.keys():
        print("Такая пицца есть в меню")
    else:
        menu[name] = price

def remuve_pizza(name):
    if name in menu.keys():
        print("Удаляем")
        del menu[name]
    else :
        print('Нет такой пиццы')



print(menu)
add_pizza("carbonara", 600)
print(menu)

