from Vect2 import *
#Constant to tune for ship's acceleration per frame
SHIP_ACC = 1;
SHIP_TURN = 1
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
    def __init__(self, position=Vect2(0,0), velocity=Vect2(0,0), acceleration=Vect2(0,0), angle=0):
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

class Inertial(Movable):
    def __init__(self, mass=1, **kwargs):
        super(Inertial, self).__init__(**kwargs)
        self.mass=mass

    def addForce(self, fVect):
        self.acc += (fVect * 1/self.mass)

#Player is an object with movement, controlled by user input
class Player(Inertial):
    def __init__(self):
        #I may move these defaults to the constructor later
        super(Player, self).__init__(mass = 1)

    #Controller is a dict containing the state of the controls
    def input(self, controller):
        #TODO: Shooting mechanism
        if (controller["acc"]):
            #There's a bit going on here.  We create a normal vector pointing at the ship's heading
            #And then we scale it to the acceleration per frame constant.
            self.acc += Vect2.fromAngle(self.angle) * SHIP_ACC
        if (controller["left"]):
            self.angle += SHIP_TURN
        if (controller["right"]):
            self.angle -= SHIP_TURN

    def draw(self):
        #Return a "data object" for pyglet's graphics.draw command.
        #front of the ship
        bow = ( Vect2.fromAngle(self.angle) * 10 ) + self.pos
        port = (Vect2.fromAngle(self.angle + (120 * math.pi/180)) * 5) + self.pos
        starboard = (Vect2.fromAngle(self.angle - (120 * math.pi/180)) *5) + self.pos
        points = (bow.x, bow.y, port.x, port.y, starboard.x, starboard.y)
        return ('v2f', points)
