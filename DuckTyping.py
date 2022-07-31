# Duck Typing = concept where the class of an object is less important than the methods/attributes that that class might have
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and quacks like a duck, then it must be a duck

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:

    def catch(self, duck): #Since both Chicken and duck walk() and talk() then Python will say: Close enough and use duck.walk and duck.talk as a substitute for using chicken as a parameter
        duck.walk() # Notice these
        duck.talk() # These say duck but we're calling the method below but using the chicken as an argument
        print("You caught it!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken) # Like here