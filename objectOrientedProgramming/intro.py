# class - defines the structure for creating objects
# objects - a specific instance of a class
# Atrributes - properties of an object 
# methods - actions that the object can perform

# example 
class car:
    color = 'red' # attribute
    # method
    def drive(self):
        print('the car is driving')

# creating an object 
my_car = car()
print(my_car.color)
my_car.drive()


# constructors the __init__ method and instance variables 
# example constructor 
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
# creating objects with unique attributes
car1 = Car('blue', 'sedan')
car2 = Car('silver', 'subaru')

print(car1.model)
print(car2.color)
    