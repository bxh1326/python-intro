#1. A class is a set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.
# An object is an instance of a class. An instance is a method.
#2. A class variable is a variable defined in a class and an instance variable is a variable is a special type of class attribute.
#3. Inheritance is when a super class is inherited by a subclass
#4. A parent class is a class from which the child class inherits information.
class shoes:
    def __init__(self, type, color, size):
        self.type = type
        self.color = color
        self.size = size
flat = shoes(type = 'flat', color = 'black', size = 8.5)
sneaker = shoes(type = 'sneaker', color = 'grey', size = 7)
heel = shoes(type = 'heel', color = 'red', size = 9)

class flat(shoes):
    def __init__(self, loworHighTop, brand):
        self.loworHighTop = loworHighTop
        self.brand = brand
    def __str__(self):
        return f'{self.type} is a {self.loworHighTop}'


# noinspection PyArgumentList
flat1 = flat(loworHighTop ='low top')
# noinspection PyArgumentList
flat2 = flat(loworHighTop ='high top')
print(flat1)
print(flat2)
