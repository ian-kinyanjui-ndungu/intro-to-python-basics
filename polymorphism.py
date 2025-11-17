#polymorphism explained
from abc import ABC, abstractmethod

#polymorphism through inheritance
class Shape:
    @abstractmethod
    def area(self):

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2

class Square(Shape):
    def __init__(self,side):
        self.side = side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

circle = Circle()

shapes =[Circle(), Square(), Rectangle(), Triangle()]
