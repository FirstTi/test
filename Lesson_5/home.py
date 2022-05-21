class Country:
    def __init__(self, population, name):
        self.population = population
        self.name = name

    def setPopulation(self, population, name):
        self.population = population
        self.name = self.__main__
        return self.population, self.name

    def getPopulation(self):
        print(f"Население {self.name} составляет {self.population} миллионов")
        return self.population, self.name

class Bulgaria(Country):
    population = 75
    name = "Bulgaria"
    pass


class Canada(Country):
    population = 100
    name = "Canada"



class Germany(Country):
    population = 120
    pass


canada_country = Canada(population=100, name=Canada)

# print(canada_country.setPopulation)
print(canada_country.getPopulation())
# print(Germany.getPopulation)
#print(Bulgaria.getPopulation)