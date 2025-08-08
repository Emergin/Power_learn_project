# inheritance example 

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
class Car(Vehicle):
    pass
car = Car(4)
print(car.wheels)


# polymophism with polymophism a method name can mean different things across multiple classes
# example 
class Dog:
    def speak(self):
        return 'woof'

class Cat:
    def speak(self):
        return 'meow'
#polymophism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())

# encapsulation this is the practice of keeping methods and attributes private to 
# prevent unwanted interferencefrom the outside class
# example 

class SecretStash:
    def __init__(self):
        self.__chocolates = 1    # private attribute

    def take_chocolates(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print('one chocolate taken')
        else:
            print('no chololates left ')
stash  = SecretStash()
stash.take_chocolates()
