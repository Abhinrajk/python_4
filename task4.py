#4. Shape Drawing Application (Abstraction)

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def draw(self):
        print("Drawing a Circle")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def draw(self):
        print("Drawing a Rectangle")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print("Drawing a Triangle")


# Creating objects
circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(6, 4)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    shape.draw()
    print("Area:", shape.area())
    print()