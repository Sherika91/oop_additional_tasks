"""
Write a class called Rectangle with the following methods:

init(self, width, height): constructor that takes the width and height of the rectangle
area(self): method that returns the area of the rectangle
perimeter(self): method that returns the perimeter of the rectangle
from_diagonal(cls, diagonal, aspect_ratio): class method that takes the diagonal of the rectangle
 and the aspect ratio and returns an object of the Rectangle class
is_square(width, height): static method that takes the width and height of the rectangle
 and returns True if it's a square, and False otherwise
"""
from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")
        self.width = width
        self.height = height

    def area(self):
        """ Returns the area of the rectangle. """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of the rectangle. """
        return 2 * (self.width + self.height)

    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        """ Returns width and height of rectangle from a diagonal and aspect ratio."""
        if diagonal <= 0 or aspect_ratio <= 0:
            raise ValueError("Diagonal and aspect ratio must be positive values.")
        width = diagonal / sqrt(aspect_ratio ** 2 + 1)
        height = width * aspect_ratio
        return cls(width, height)

    @classmethod
    def is_square(cls, width, height):
        """ Return True if rectangle is a square, False otherwise."""
        return width == height


rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 1)
print(round(rectangle2.area(), 2))  # 12.5
print(round(rectangle2.perimeter(), 2))  # 14.14

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
