import math


# Gravitational constant
G = 6.67384 * math.pow(10, -11)


def gravitational_acceleration(mass, radius):
    '''
    Calculate gravity acceleration anywhere in the universe.
    Takes the mass of object pulling on you,
    and the distance from the center (radius) of the object.
    '''
    return G * (mass / math.pow(radius, 2))
