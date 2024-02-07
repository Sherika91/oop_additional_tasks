"""
Write a class called User, having the following properties and methods:

init(self, name, password): constructor that accepts the username and password
name: property that returns the username
password: property that allows setting or changing the user's password
is_admin: property that returns whether the user is an administrator or not
_is_admin: helper property that determines whether the user is an administrator or not
login(self, password): method that checks if the entered password matches the user's password
logout(self): method that logs out of the user's account
Use the @property and @password.setter decorators for the name and password properties.
"""


class User:
    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._is_admin = False
        self._is_logged_in = False

    @property
    def name(self):
        """ Returns the username. """
        return self._name

    @property
    def password(self):
        """ Returns the user's password. """
        return self._password

    @password.setter
    def password(self, new_password):
        """ Sets the user's password. """
        self._password = new_password
        return self._password

    @property
    def is_admin(self):
        """ Returns whether the user is an administrator or not. """
        return self._is_admin

    def login(self, password):
        """ Checks if the entered password matches the user's password. """
        if self._password == password:
            self._is_logged_in = True
            return True
        return False

    def logout(self):
        """ Logs out of the user's account. """
        self._is_logged_in = False


user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

print(user1.login("newpassword"))  # True
user1.logout()
