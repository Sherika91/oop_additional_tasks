"""
Create a class called Bottle with the following fields:

Color (color) - string
Volume (volume) - floating-point numbers
Create three instances:

Red 0.7
White 0.3
Black 1.0
"""


class Bottle:

    def __init__(self, color, volume):
        self.color = color
        self.volume = volume


# Create three instances of the Bottle class
bottle_1 = Bottle("Red", 0.7)
bottle_2 = Bottle("White", 0.3)
bottle_3 = Bottle("Black", 1.0)

# Print the color and volume of each bottle
print(bottle_1.color, bottle_1.volume)  # Red 0.7
print(bottle_2.color, bottle_2.volume)  # White 0.3
print(bottle_3.color, bottle_3.volume)  # Black 1.0
