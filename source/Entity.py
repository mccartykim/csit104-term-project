class Entity(object):

    #Process user input, if relevant.
    def input(self, controller):
        pass

    #Update whatever changes in this object over time
    def update(self, dt):
        pass

    #Render the object, if applicable.
    def draw(self):
        pass

#An entity that can move with basic physics
class Movable(Entity):
    def __init__(self, position=None, velocity=None, acceleration=None, angle=0):
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.angle = angle

    #generate new position and velocity.  Let DT be the time since the last update.
    def update(self, dt):
        self.vel += self.acc
        self.acc *= 0 #Acceleration must be added each time.
        self.pos += (self.vel * dt)

    def addAcc(self, acc):
        self.acc += acc

def Inertial(Movable):
    def __init__(self, **kwargs, mass=1):
        super(Inertial, self).__init__(**kwargs)
        self.mass=mass

    def addForce(self, fVect):
        self.acc += (fVect * 1/self.mass)
