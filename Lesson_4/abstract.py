from abc import abstractmethod


class MilkAnimal:
    @abstractmethod
    def make_noise(self):
        pass

    def make_many_noise(self):
        for i in range(5):
            self.make_noise()


class Horse(MilkAnimal):
    pass
    def make_noise(self):
        print("igogo")


class Bird(MilkAnimal):
    def make_noise(self):
        print("chirik")

horse = Horse()
#print(horse.make_many_noise())
horse.make_many_noise()
