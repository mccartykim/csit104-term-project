import math
import random

# A fairly simple vector object
# Most functions were defined as I needed them,
# instead of trying to define a robust linear algebra system.
class Vect2(object):
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    #Override addition
    def __add__(self, other):
        return Vect2(self.x + other.x, self.y + other.y)

    #Override subtraction
    def __sub__(self, other):
        return self + (other * -1)

    #Multiply vector by ONLY a scalar
    def __mul__(self, other):
        return Vect2(self.x * other, self.y * other)

    #Magnitude of the vector
    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    #Normalize the vector in place, with the same direction but a magnitude of 1
    def normalize(self):
        self *= (1/self.mag())
        return self

    #Create a normal vector from an angle in radians
    @staticmethod
    def fromAngle(ang):
        return Vect2(math.cos(ang), math.sin(ang))

    #Return an angle in radians from the vector object
    def toAngle(self):
        return math.atan2(self.y, self.x)

    #Avoid issues with pass by reference by returning a new Vect2
    def getCopy(self):
        return Vect2(self.x, self.y)

# Find the distance between two vectors (useful for position vectors)
    def getDistance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y-self.y)**2 )

# Get a random normalized vector
    @staticmethod
    def random():
        return Vect2.fromAngle(random.uniform(0, 2*math.pi))
