"""
Create a class Student with the following fields:

- Name (name) - string
- Course (course) - integer
- Grades - a list of integers, which may be empty

Describe the Student class and the avg_rate method so that the average grade is calculated,
 and 0 is returned for an empty list of grades.
"""


class Student:

    def __init__(self, name: str, course: int, grades: list):
        self.name = name
        self.course = course
        self.grades = grades

    def avg_rate(self):
        if len(self.grades) == 0:
            return 0
        else:
            sum(self.grades) / len(self.grades)


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate()  # 4.75

student = Student('Ivan', 'Python', [])
student.avg_rate()  # 0.0
