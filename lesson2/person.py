"""
Write a class called Person with the following methods:

init(self, name, age): constructor that takes the person's name and age
display(self): method that displays the person's name and age
from_birth_year(cls, name, birth_year): class method that takes
 the person's name and birth year and returns an object of the Person class
is_adult(cls, age): static method that takes the person's age and returns True,
 if they are older than 18 years old, and False otherwise
"""
from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        """ Returns the person's name and age. """
        return f"{self.name} is {self.age} years old."

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """ Returns an object of the Person class from the person's name and birth year. """
        current_year = datetime.now().year
        return cls(name, current_year - birth_year)

    @staticmethod
    def is_adult(age):
        """ Returns True if the person is older than 18 years old, False otherwise. """
        return age > 18


# код для проверки
person1 = Person("John", 28)
print(person1.display())  # John is 28 years old.

person2 = Person.from_birth_year("Mike", 1995)
print(person2.display())  # Mike is 29 years old)

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False
