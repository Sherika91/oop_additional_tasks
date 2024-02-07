"""
Create a class called Student with the following fields:

Name (name) - string
Course (course) - integers
Create two instances:

Alice, 3 [course]
Margarita, 2 [course]
"""


class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course


# Create two instances of the Student class
student_1 = Student("Alice", 3)
student_2 = Student("Margarita", 2)

# Print the name and course for each student
print(student_1.name, student_1.course)  # Alice 3
print(student_2.name, student_2.course)  # Margarita 2
