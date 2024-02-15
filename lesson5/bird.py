"""
Write a class called Bird, representing a bird, with the following methods:
fly(self): method that prints the message "Flying".

Write a class called Penguin, inheriting from the Bird class, representing a penguin, with the following methods:
fly(self): method that prints the message "I am a penguin and cannot fly".

Write a class called Eagle, inheriting from the Bird class, representing an eagle, with the following methods:
hunt(self): method that prints the message "Hunting".
"""


class Bird:
    def __init__(self):
        pass

    def fly(self):
        print("Flying")


class Penguin(Bird):
    def fly(self):
        print("I am a penguin and cannot fly")


class Eagle(Bird):
    def hunt(self):
        print("Hunting")


# код для проверки
bird = Bird()
bird.fly()  # Flying
print()

penguin = Penguin()
penguin.fly()  # I am a penguin and cannot fly
print()

eagle = Eagle()
eagle.fly()  # Flying
eagle.hunt()  # Hunting
