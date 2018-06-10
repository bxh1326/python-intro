class Robot:

    count = 0

    def __init__(self, name):
        self.name = name
        Robot.count += 1
        print(f'Created robot {name}')

    def sayHi(self):
        print(f'Hi my name is a {self.name}')

    def die(self):
        Robot.count -= 1
        print(f'Destroying {self.name}')

    @classmethod
    def howMany(cls):
        print(f'There are {cls.count} robots in my universe')

robot1 = Robot('R2D2')
robot2 = Robot('Moonwalker')
robot3 = Robot('C3PO')
Robot.howMany()
robot1.die()
robot1.howMany()
robot3.die()
robot2.howMany()

