"""
Write a class called BankAccount, which has the following properties and methods:

init(self, balance): constructor that takes the initial account balance
balance: property that returns the current account balance
deposit(self, amount): method that allows depositing money into the account
withdraw(self, amount): method that allows withdrawing money from the account
close(self): method that closes the account and returns the remaining money in it
Use the @property decorator for the balance property.
"""


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        """ Returns the current account balance. """
        return self._balance

    def deposit(self, amount):
        """ Allows depositing money into the account. """
        self._balance += amount

    def withdraw(self, amount):
        """ Allows withdrawing money from the account. """
        if 0 < amount <= self._balance:
            self._balance -= amount
            return amount
        else:
            print("Insufficient funds")

    def close(self):
        """ Closes the account and returns the remaining money in it. """
        closed_account = self._balance
        self._balance = 0
        return closed_account


# код для проверки 
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
