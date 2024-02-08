"""
Write a class called MyList, representing a list, which has the following methods:

- __init__(self, data): constructor that accepts a list of elements;
- __repr__(self): magic method that returns a string representation of the list,
which can be used to create a new object of the MyList class;
- __str__(self): magic method that returns a string representation of the list;
- __len__(self): magic method that returns the length of the list;
- __add__(self, other): magic method that allows adding lists and returns a new list.
"""


class MyList:
    def __init__(self, data):
        """ Constructor that accepts a list of elements. """
        self.data = data

    def __repr__(self):
        """ magic method, which returns a string representation of the list,"""
        return f"MyList({self.data})"

    def __str__(self):
        """ magic method, which returns a string representation of the list. """
        return f"{self.data}"

    def __len__(self):
        """ magic method, which returns the length of the list. """
        return len(self.data)

    def __add__(self, other):
        """ magic method, which allows adding lists and returns a new list. """
        new_data = self.data + other.data
        return MyList(new_data)


# Code for testing the class
my_list1 = MyList([1, 2, 3])
print(repr(my_list1))  # MyList([1, 2, 3])
print(str(my_list1))  # [1, 2, 3]
print(len(my_list1))  # 3

my_list2 = MyList([4, 5, 6])
my_list3 = my_list1 + my_list2
print(my_list3)  # [1, 2, 3, 4, 5, 6]
