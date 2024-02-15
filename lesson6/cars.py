"""
Write a class called Car, representing a car, with the following properties:

- brand
- model
- year of manufacture

It is important to handle exceptions in the constructor if the year is greater than the current year.
"""
from datetime import datetime


class Car:
    def __init__(self, brand, model, year_manufactured):
        self.brand = brand
        self.model = model
        self.year_manufactured = year_manufactured
        if year_manufactured > datetime.now().year:
            raise Exception('This car has not been released yet')


# Code for testing
car = Car('Toyota', 'Corolla', 2022)

car = Car('Toyota', 'Corolla', 3000)
# raises Exception ('This car has not been released yet')
