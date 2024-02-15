"""
Complete the code within the loop according to the conditions so that the output is correct.
"""


class Animal:
    """
    A class to represent a general animal.

    ...

    Attributes
    ----------
    name : str
        The name of the animal

    Methods
    -------
    walk()
        Placeholder method for walking behavior.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the animal object.

        Parameters
        ----------
            name: str
                The name of the animal
        """
        self.name = name

    def walk(self):
        """
        Placeholder method for walking behavior.
        This method should be overridden by any subclasses.
        """
        pass


class Dog(Animal):
    """
    A class to repesent a dog, inherits from the Animal class.

    ...

    Mehtods
    -------
    bark():
        Prints the sound that the dog makes.
    """

    def bark(self):
        """
        Prints the sound that the dog makes.
        """
        print(f"{self.name} says Woof!")


class Cat(Animal):
    """
    A class to represent a dog, inheritss from the Animal class.

    ...

    Mehtods
    -------
    meow():
        Prints the sound that the cat makes.
    """

    def meow(self):
        """
        Prints the sound that the cat makes
        """
        print(f"{self.name} says Meow!")


# Code for testing
animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    """
    Iterates over a list of animal objects.
    Calls the appropriate method depending on the class of the objct.
    """
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()
