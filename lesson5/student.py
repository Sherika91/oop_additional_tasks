"""

Write a class called Student, representing a student, with the following attributes:
slots = ('name', 'age', 'grades'): list of attributes available to the object.

Write a class called Course, representing a course, with the following attributes:
slots = ('name', 'students'): list of attributes available to the object.
"""


class Student:
    __slots__ = ('name', 'age', 'grades')

    def __init__(self):
        pass


class Course:
    __slots__ = ('name', 'students')

    def __init__(self):
        pass


# код для проверки
student1 = Student()
student1.name = "John"
student1.age = 20
student1.grades = [90, 80, 85]

student2 = Student()
student2.name = "Jane"
student2.age = 21
student2.grades = [95, 85, 90]

course = Course()
course.name = "Math"
course.students = [student1, student2]
