
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
