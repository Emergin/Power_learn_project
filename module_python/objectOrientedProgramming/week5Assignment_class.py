class Laptop:
    color = 'silver'
    name = 'HP'
    ram = '8gb'
    rom = '500gb'
    keyboard = 'black'
    camera = 'no'
    battery = 'dead'
    price = 33000

    def description(self, color, name, price):
        self.color = color
        self.name = name
        self.price = price
        print(f'this is my laptop which is {Laptop.color} in color, name {Laptop.name} and it cost me {Laptop.price} ksh')


class LaptopBag(Laptop):
    size = 'large'
    pockets = 12
    pass


class WaterBottle(Laptop):
    def __init__(self):
        self.__number = 1
        pass
    def describe(self):
        if self.__number < 1:
            self.__number -= 1
            print('water bottle has been stolen')
        else:
            print('water bottle present')

query = WaterBottle()
query.describe()

bag  = LaptopBag()
print(LaptopBag.color)

desc1 = Laptop()
print(Laptop.name)
desc1.description('color', 'name', 'price')
