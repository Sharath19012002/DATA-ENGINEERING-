# Abstract class representing a Shape
class Shape:
    def area(self):
        pass
# Concrete class Circle implementing Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
# Concrete class Rectangle implementing Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
# Using the abstract class without importing any modules
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area of the shape: {shape.area()}")
