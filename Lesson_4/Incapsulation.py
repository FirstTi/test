class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __inner_method(self): # с помощью двух подчеркиваний перед методом он стал скрытым
                              ## с помощью одного подчерк. можно показать что метод скрыт, но выполнить все равно не получится
        print("Выполнился внутренний метод")

    def get_name(self):
        self.inner_method()
        return self.name

animal = Animal("First", 122)

animal.inner_method() # и попытка вызвать метод вызывает ошибку, если убрать подчеркивания - код отработает

# animal._Animal__inner_method() # так можно увидеть скрытый метод - через явное указывание класса и метода который ты хочешь увидеть
