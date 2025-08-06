class Car:
    def move(self):
        print('am driving')

class Plane:
    def move(self):
        print('Am flying')

class Ship:
    def move(self):
        print('Am floating')

class Train:
    def move(self):
        print('am in a train')

car = Car()
car.move()
plane = Plane()
plane.move()
ship = Ship()
ship.move()
train = Train()
train.move()

# for x in [Car(), Plane(), Ship(), Train()]:
#     print(x.move())