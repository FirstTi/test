import json


class Pizzeria:
    @staticmethod
    def load_menu():
        f = open("menu.json", "r")
        menu = json.load(f)
        f.close()
        return menu

    @staticmethod
    def __save_menu(menu):
        f = open("menu.json", "w")
        json.dump(menu, f)
        f.close()

    def add_pizza(self, name, price):
        menu = self.load_menu()
        if name in menu.keys():
            print("Такая пицца есть в меню")
        else:
            menu[name] = price
        self.__save_menu(menu)

    def remove_pizza(self, name):
        menu = self.load_menu()
        if name in menu.keys():
            print("Удаляем")
            del menu[name]
        else:
            print('Нет такой пиццы. Удалять нечего')
        self.__save_menu(menu)

    def order_pizza_api(self, order):
        menu = self.load_menu()
        cost = 0
        for pizza_name in order:
            if pizza_name in menu.keys():
                cost += menu[pizza_name]
            else:
                return None
        return cost

    def order_pizza(self):
        order = []
        cost = 0
        menu = self.load_menu()
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

pizzeria = Pizzeria()


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
                    pizzeria.add_pizza(name_pizza, price)  # сейчас используем позиционные аргументы
                    # или именованые аргументы т.е. можно в любом порядке вводить аргументы он сам найдет add_pizza(price=price, name=name)
                elif q2 == "remove":
                    name_pizza = input("Введите имя для удаляемой пиццы: ")
                    pizzeria.remove_pizza(name_pizza)
                f = open("menu.json", "r")
                menu = json.load(f)
                print(menu)
                f.close()

            elif role == "User":
                print(pizzeria.order_pizza())
            else:
                print("Данные введены неверно")
