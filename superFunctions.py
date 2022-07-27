# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used.

class Rectangle: # "Super class"

    def __init__(self, length, width):
        self.length = length
        self.width = width



class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width) # Instead of writing the comments below we can use this to spare lines of code

    def area(self):
        return self.length*self.width

        #self.length = length
        #self.width = width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height # Height must still be made here as the super class only has length and width

    def volume(self):
        return self.length*self.width*self.height

        #self.length = length
        #self.width = width



square = Square(3, 3) # Length, Width
cube = Cube(3, 3, 3) # Length, Width, Height

print(square.area())
print(cube.volume())
