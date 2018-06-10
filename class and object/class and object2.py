class Animal:
    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound
    def compareWeight(self, anotherAnimal):
        if self.weight > anotherAnimal.weight:
            print(self.name, 'weight is greater than', anotherAnimal.name, 'weight')
        elif self.weight < anotherAnimal.weight:
            print(self.name, 'weight is less than', anotherAnimal.name, 'weight')

animal1 = Animal('cat',10, 'meow')
animal2 = Animal('dog', 20, 'woof')
animal3= Animal('horse',100, 'neigh')
animal4 = Animal('bird',5, 'chirp')
animal5 = Animal('lion',100, 'roar')

animal1.compareWeight(animal5)

