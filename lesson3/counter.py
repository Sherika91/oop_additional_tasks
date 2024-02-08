"""
Write a class called Counter, which has the following methods:

- __init__(self): constructor that creates a counter and sets its value to 0;
- __call__(self): magic method that allows using an object of the Counter class as a function, returning the current value of the counter;
- increment(self): method that increases the value of the counter by 1.
"""


class Counter:
    def __init__(self):
        """ Create a counter and set its value to 0. """
        self.value = 0

    def __call__(self):
        """ Return the current value of the counter. """
        return self.value

    def increment(self):
        """ Increase the value of the counter by 1. """
        self.value += 1


# Code for testing the class
counter = Counter()
print(counter())  # 0

counter.increment()
print(counter())  # 1

counter.increment()
print(counter())  # 2
