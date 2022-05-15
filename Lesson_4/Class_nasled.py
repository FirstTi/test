class Animal:
    def __init__(self, name, health, speed):
        self.speed = speed
        self.name = name
        self.health = health


    def make_noise(self):
        print("Grrrr")


class Cat(Animal):
    def make_noise(self):
        print("Mya")

class Dog(Animal):
    def make_noise(self):
        print("Gav")



cat1 = Cat( name="Barsik", speed=20, health=100)
dog = Dog(name="Sharik", health=200, speed=25)
print(cat1.name)
print(cat1.health)
print(cat1.make_noise())
print(cat1.speed)

cat1.make_noise()
dog.make_noise()


