"""
Write a class called Animal, representing an animal, which has the following methods:
- __init__(self, name): constructor that takes the name of the animal;
- speak(self): method that outputs the sound made by the animal.

Write a class called Dog, inheriting from the Animal class, representing a dog, which has the following methods:
- speak(self): method that outputs the sound made by the dog.

Write a class called Cat, inheriting from the Animal class, representing a cat, which has the following methods:
- speak(self): method that outputs the sound made by the cat.
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
        speak():
            Prints the sound that the animal makes.
        """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the animal object.

        Parameters
        ----------
            name : str
                the name of the animal
        """
        self.name = name

    def speak(self):
        """
        Prints the sound that the animal makes.
        This method should be overridden by any subclasses.
        """
        pass


class Dog(Animal):
    """
    A class to represent a dog, inherits from the Animal class.
    ...

    Methods
    -------
    speak():
        Prints the sound that the dog makes.
    """

    def speak(self):
        """
        Prints the sound that the dog makes.
        Overrides the speak() method in the Animal class.
        """
        print(f"{self.name} says Woof!")


class Cat(Animal):
    """
    A class to represent a cat, inherits from the Animal class.

    ...

    Methods
    -------
    speak()
        Prints the sound that the cat makes.
    """

    def speak(self):
        """
        Prints the sound that the cat makes.
        Overrides the speak() method in the Animal class.
        """
        print(f"{self.name} says Meow!")


# Code for testing the classes
animal = Animal("Animal")
animal.speak()  # ?

dog = Dog("Dog")
dog.speak()  # Woof!

cat = Cat("Cat")
cat.speak()  # Meow!
