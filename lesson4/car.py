"""
Write a class called Car, representing a car, which has the following methods:
- __init__(self, brand, model, year): constructor that takes the car's make, model, and year of manufacture;
- get_brand(self): method that returns the car's make;
- get_model(self): method that returns the car's model;
- get_year(self): method that returns the car's year of manufacture.

Write a class called ElectricCar, inheriting from the Car class, representing an electric car, which has the following methods:
- __init__(self, brand, model, year, battery_size):
constructor that takes the electric car's make, model, year of manufacture, and battery size;
- get_battery_size(self): method that returns the electric car's battery size.
"""


class Car:
    """
    A class to represent a general car.

    ...

    Attributes
    ----------
    brand : str
        The brand of the car.
    model : str
        The mode of the car.
    year : str
       the year a car was manufactured.

    Methods
    -------
    get_brand():
        Returns the brand of the car.
    get_model():
        Returns the model of the car.
    get_year():
        Returns the year a car was manufactured.
    """

    def __init__(self, brand, model, year):
        """
        Contstructs all the necessary attributes for the car object.

        Parameters
        ----------
            brand : str
                The brand of the car.
            model : str
                The model of the car.
            year : int
                The year a car was manufactured.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def get_brand(self):
        """
        Returns the brand of the car.
        """
        return self.brand

    def get_model(self):
        """
        Returns the model of the car.
        """
        return self.model

    def get_year(self):
        """
        Returns the year of the car.
        """
        return self.year


class ElectricCar(Car):
    """
    A class to represent an electric car, inherits from the Car class.

    ...

    Attributes
    ----------
    battery_size : int
        The battery size of the electric car.

    Methods
    -------
    get_battery_size():
        Returns the battery size of the electric car
    """

    def __init__(self, brand, model, year, battery_size):
        """
        Constructs all the necessary attributes for the electric car object.

        Parameters
        ----------
            brand : str
                The brand of the electric car
            model : str
                The model of the electric car
            year : int
                The year a car was manufactured.
            battery_size : int
                The battery size of the electric car
        """

        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def get_battery_size(self):
        """
        Returns the battery size of the elctric car.
        """
        return self.battery_size


# Code for testing
car = Car("Tesla", "Model S", 2022)
print(car.get_brand())  # Tesla
print(car.get_model())  # Model S
print(car.get_year())  # 2022
print()

electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
print(electric_car.get_brand())  # Tesla
print(electric_car.get_model())  # Model S
print(electric_car.get_year())  # 2022
print(electric_car.get_battery_size())  # 100
