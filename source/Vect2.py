import math
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
