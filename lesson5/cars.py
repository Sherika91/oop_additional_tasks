"""
Write a class called Car, representing a car, with the following properties:
- Brand
- Model
- Year of manufacture
Since this class is used in a large catalog, it needs to be optimized by creating a class that uses slots collections.

Compare the speed of operation of two classes: with slots collections and without them.
For this, write a method called get_set_del for each class,
which involves getting, assigning, and deleting a value.
"""

import timeit


class Car:
    def __init__(self, brand, model, year_manufactured):
        self.brand = brand
        self.model = model
        self.year_manufactured = year_manufactured

    def get_set_del(self):
        getattr(self, 'brand')
        setattr(self, 'brand', 'New Brand')
        delattr(self, 'brand')
        # we set the brand back to the original value, so we don't get an error when we try to use it
        self.brand = 'brand'


class CarSlots:
    __slots__ = ['brand', 'model', 'year_manufactured']

    def __init__(self, brand, model, year_manufactured):
        self.brand = brand
        self.model = model
        self.year_manufactured = year_manufactured

    def get_set_del(self):
        getattr(self, 'brand')
        setattr(self, 'brand', 'New Brand')
        delattr(self, 'brand')
        # we set the brand back to the original value, so we don't get an error when we try to use it
        self.brand = 'brand'


car = Car('Toyota', 'Corolla', 2022)
car_slots = CarSlots('Toyota', 'Crown', 1990)

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)
print((t1 - t2) / t1 * 100)
