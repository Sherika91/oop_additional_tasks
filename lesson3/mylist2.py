"""
Write a class called MyList2, which will work similarly to the built-in list() class. The class should have the following methods:

- __init__(self, data): constructor that accepts a list of elements;
- __iter__(self): magic method that returns an iterator;
- __next__(self): magic method that returns the next element of the sequence;
- __getitem__(self, index): magic method that allows accessing the element of the list by index.
"""


class MyList2:
    def __init__(self, data):
        """ Constructor that accepts a list of elements and sets the index to 0. """
        self.data = data
        self.index = 0

    def __iter__(self):
        """ magic method that returns an iterator. """
        return self

    def __next__(self):
        """ magic method that returns the next element of the sequence. """
        if self.index >= len(self.data):
            raise StopIteration

        item = self.data[self.index]
        self.index += 1
        return item

    def __getitem__(self, item):
        """ magic method that allows accessing the element of the list by index. """
        return self.data[item]


# Code for testing the class
my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i, end=" ")  # 1 2 3
print()

print(my_list[1])  # 2
