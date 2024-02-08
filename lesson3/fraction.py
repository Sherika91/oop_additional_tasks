"""
Write a class called Fraction, representing a fraction, which has the following methods:

- __init__(self, numerator, denominator): constructor that takes the numerator and denominator of the fraction;
- __repr__(self): magic method that returns a string representation of the fraction,
 which can be used to create a new Fraction object;
- __str__(self): magic method that returns a string representation of the fraction;
- __add__(self,  other): magic method that allows adding fractions and returns a new fraction.
"""


class Fraction:
    def __init__(self, numerator, denominator):
        """ Constructor that takes the numerator and denominator of the fraction. """
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        """ magic method that returns a string representation of the fraction. """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        """ magic method that returns a string representation of the fraction. """
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """ magic method that allows adding fractions and returns a new fraction. """
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(new_numerator, common_denominator)


# Code for testing the class
fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
