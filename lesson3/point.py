"""
Write a class called Point, representing a point on the plane, which has the following methods:

- __init__(self, x, y): constructor that accepts the coordinates of the point;
- __repr__(self): magic method that returns a string representation of the point,
which can be used to create a new object of the Point class;
-__str__(self): magic method that returns a string representation of the point;
-__add__(self, other): magic method that allows adding points and returns a new point.
"""


class Point:
    def __init__(self, x, y):
        """ Constructor that accepts the coordinates of the point. """
        self.x = x
        self.y = y

    def __repr__(self):
        """ magic method that returns a string representation of the point. """
        return f"Point({self.x, self.y})"

    def __str__(self):
        """ magic method that returns a string representation of the point. """
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """ magic method that allows adding points and returns a new point. """
        new_point_x = self.x + other.x
        new_point_y = self.y + other.y
        return Point(new_point_x, new_point_y)


# Code for testing the class
point1 = Point(1, 2)
print(repr(point1))  # Point(1, 2)
print(str(point1))  # (1, 2)

point2 = Point(3, 4)
point3 = point1 + point2
print(point3)  # (4, 6)
