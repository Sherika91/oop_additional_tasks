"""
Write a class called Employee, representing an employee, with the following methods:
- __init__(self, name, salary): constructor that accepts the employee's name and their salary;
- get_salary(self): method that returns the employee's salary.

Write a class called Manager, inheriting from the Employee class, representing a manager, with the following methods:
- __init__(self, name, salary, bonus): constructor that accepts the manager's name, their salary, and bonus;
- get_salary(self): method that returns the manager's salary plus their bonus.
"""


class Employee:
    """
    A class to represent a general employee.

    ...

    Attributes
    ----------
    name : str
        the name of the employee
    salary : int
        the salary of the employee

    Methods
    -------
    get_salary():
        Returns the salary of the employee.
    """

    def __init__(self, name, salary):
        """
        Constructs all the necessary attributes for the employee object.

        Parameters
        ----------
            name : str
                the name of the employee
            salary : int
                the salary of the employee
        """
        self.name = name
        self.salary = salary

    def get_salary(self):
        """
        Returns the salary of the employee.
        """
        return f"Salary of {self.name} is equal to {self.salary}."


class Manager(Employee):
    """
    A class to represent a manager. Inherits from the Employee class.

    ...

    Attributes
    ----------
    bonus : int
        the bonus of the manager

    Methods
    -------
    get_salary():
        Returns the salary of the manager plus their bonus.
    """

    def __init__(self, name, salary, bonus):
        """
        Constructs all the necessary attributes for the manager object.

        Parameters
        ----------
            name : str
                the name of the manager
            salary : int
                the salary of the manager
            bonus : int
                the bonus of the manager
        """
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        """
        Returns the salary of the manager plus their bonus.
        """
        return f"Salary of Manager is equal to {self.salary + self.bonus}."


# Code for testing
employee = Employee("John", 5000)
print(employee.get_salary())  # 5000

manager = Manager("Jane", 10000, 5000)
print(manager.get_salary())  # 15000
