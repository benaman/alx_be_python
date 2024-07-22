import math

# Define the base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Define the derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Define the derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

