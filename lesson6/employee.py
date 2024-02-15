"""
Write a class called Person, representing a person, with the following attributes:

- name
- age
- salary

Write a class called Employee,
 in which the constructor checks that the age is not less than 18 and not greater than 127 years old.

If the age does not fit within the specified limits, raise a ValueError exception and terminate the program.
Also, in the constructor, it is necessary to check the salary level,
 which should not be less than 16242. Raise a ValueError
exception if this condition is violated.

The raised exceptions should explain specifically what error occurred.
"""


class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        if salary < 16242:
            raise ValueError("Salary cannot be less than 16242")
        if not 18 <= age <= 127:
            raise Exception("Age must be between 18 and 127")


# код для проверки
# employee = Employee('John', 30, 5000)
# raises ValueError('Salary cannot be less than 16242')

employee = Employee("Jane", 17, 50000)
# raises ValueError('Age must be between 18 and 127')

employee = Employee("Kate", 175, 50000)
# raises ValueError('Age must be between 18 and 127')
