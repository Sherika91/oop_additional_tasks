"""
Write a class called Shape, representing a geometric shape, with the following methods:
- __init__(self, name): constructor that accepts the name of the geometric shape;
- area(self): method that computes the area of the geometric shape.

Write a class called Rectangle, inheriting from the Shape class, representing a rectangle, with the following methods:
- __init__(self, name, width, height): constructor that accepts the name of the rectangle, its width, and height;
- area(self): method that computes the area of the rectangle.

Write a class called Triangle, inheriting from the Shape class, representing a triangle, with the following methods:
- __init__(self, name, base, height): constructor that accepts the name of the triangle, its base, and height;
- area(self): method that computes the area of the triangle.
"""


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return int(1 / 2 * (self.base * self.height))


shape = Shape("Shape")
print(shape.area())  # 0

rect = Rectangle("Rectangle", 5, 10)
print(rect.area())  # 50

tri = Triangle("Triangle", 6, 4)
print(tri.area())  # 12
