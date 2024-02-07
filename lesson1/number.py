"""
Create a class called Number with a field value (specified during initialization).

Create an instance, for example, x = Number(7).

Add methods:

.get() returns the current value.

.add(<value>) adds the specified number to the value.

.subtract(<value>) subtracts the specified number from the value.
"""


class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        """ Returns the current value. """
        return self.value

    def add(self, number):
        """ Adds the specified number to the value."""
        self.value += number

    def subtract(self, number):
        """ Subtracts the specified number from the value. """
        self.value -= number


n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.subtract(5)
print(n.get())  # 5
