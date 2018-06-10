class Animal:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.weight = kwargs['weight']
        self.sound = kwargs['sound']

    def __str__(self):
        return f'{self.name} is an animal'

cat = Animal(name='cat', weight=10, sound='meow')
dog = Animal(name='dog', weight=20, sound='bark')

class Cat(Animal):

    def __init__(self, **kwargs):
        self.breed = kwargs['breed']
        super().__init__(**kwargs)

    def __str__(self):
        return f'{self.name} is a {self.breed} cat'

cat1 = Cat(name='tom', weight=7, sound='meow', breed='Persian')
cat2 = Cat(name='dan', weight=3, sound='meow', breed='Russian Blue')
cat3 = Animal(name='dan', weight=3, sound='meow', breed='Russian Blue')
print(cat2)
print(cat3)

class Dog(Animal):

    def __init__(self, **kwargs):
        self.tricks = kwargs['tricks']
        super().__init__(**kwargs)

    def __str__(self):
        return f'{self.name} can {self.tricks}'

dog1 = Dog(name='bella', weight=20, sound='bark', tricks='roll over')
dog2 = Dog(name='loki', weight=24, sound='bark', tricks='sit down')
print(dog1)
print(dog2)
