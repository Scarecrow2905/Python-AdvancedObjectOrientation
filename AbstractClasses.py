# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# Abstract class = A class which contains one or more abstract methods.
# Abstract method = A method that has a declaration but does not have an implementation.

# abc = acronym for Abstract Base Class
from abc import ABC, abstractmethod

class Vehicle(ABC):

# All the classes who inherit Vehicle need to have these two methods for the program to work
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


#vehicle = Vehicle() This can't be used as Vehicle()  is an abstract class, it can't become a "physical" form. It acts only as a blueprint
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()