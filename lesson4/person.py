"""
Write a class called Person, representing a person, with the following methods:
- __init__(self, name, age): constructor that takes the person's name and age;
- get_name(self): method that returns the person's name;
- get_age(self): method that returns the person's age.

Write a class called Student, inheriting from the Person's class, representing a student, with the following methods:
- __init__(self, name, age, major): constructor that takes the student's name, age, and major;
- get_major(self): method that returns the student's major.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def get_major(self):
        return self.major


# код для проверки
person = Person("Ivan", 25)
print(person.get_name())  # Ivan
print(person.get_age())  # 25
print()

student = Student("Maria", 20, "Mathematics")
print(student.get_name())  # Maria
print(student.get_age())  # 20
print(student.get_major())  # Mathematics
