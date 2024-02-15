"""
Write a class called Person, representing a person, with the following methods:
- __init__(self, name, age): constructor, taking the person's name and age;
- get_name(self): method that returns the person's name;
- get_age(self): method that returns the person's age.

Write a class called Employee2, inheriting from the Person class, representing an employee, with the following methods:
- __init__(self, name, age, salary): constructor, taking the employee's name, age, and salary;
- get_salary(self): method that returns the employee's salary.

Write a class called Manager2, inheriting from the Employee2 class, representing a manager, with the following methods:
- __init__(self, name, age, salary, bonus): constructor, taking the manager's name, age, salary, and bonus;
- get_bonus(self): method that returns the manager's bonus.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Employee2(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager2(Employee2):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus


# код для проверки
person = Person("John", 30)
print(person.get_name())  # John
print(person.get_age())  # 30
print()

employee = Employee2("Jane", 25, 5000)
print(employee.get_name())  # Jane
print(employee.get_age())  # 25
print(employee.get_salary())  # 5000
print()

manager = Manager2("Bob", 40, 10000, 5000)
print(manager.get_name())  # Bob
print(manager.get_age())  # 40
print(manager.get_salary())  # 10000
print(manager.get_bonus())  # 5000
