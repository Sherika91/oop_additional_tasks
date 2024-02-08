"""
Write a class called Logger, which has the following methods:

- __init__(self, filename): a constructor that accepts the name of the file where logs will be written;
- __call__(self, message): a magic method that allows using an object of the Logger class as a function,
taking a message and writing it to the file.
"""


class Logger:
    def __init__(self, filename):
        """ Constructor that accepts the name of the file where logs will be written. """
        self.filename = filename

    def __call__(self, messsage):
        try:
            with open(self.filename, "a") as file:
                file.write(f"{messsage}\n")
                print("Text written to file successfully!")
        except IOError as e:
            print("Error writing to file:", e)


# Code for testing the class
logger = Logger("log.txt")
logger("This is a test message.")
