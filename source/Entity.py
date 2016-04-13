import random
from Vect2 import *
import pyglet
#Constant to tune for ship's acceleration per frame
SHIP_ACC = 1;
SHIP_TURN = 5 * math.pi/180
MAX_VELOCITY = 300


def loop_lines(points):
     #test if points are even
    out = []
    if len(points) % 2 != 0:
        raise ValueError("Uneven list of points")
    i = 0
    while i < len(points) - 3:
        out.extend(points[i:i+4])
        i += 2
    out.extend(points[-2::])
    out.extend(points[0:2])
    return tuple(out)

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
    def __init__(self, position=Vect2(0,0), velocity=Vect2(0,0), acceleration=Vect2(0,0), angle=0, bounds= ( 0, 0, 800, 400 )) :
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.angle = angle
        self.bounds = bounds

    #generate new position and velocity.  Let DT be the time since the last update.
    def update(self, dt):
        self.vel += self.acc
        self.acc *= 0 #Acceleration must be added each time.
        self.pos += (self.vel * dt)
        #Add bounds checking
        if self.pos.x < self.bounds[0]:
            self.pos.x = self.bounds[2]
        elif self.pos.x > self.bounds[2]:
            self.pos.x = self.bounds[0]
        if self.pos.y < self.bounds[1]:
            self.pos.y = self.bounds[3]
        elif self.pos.y > self.bounds[3]:
            self.pos.y = self.bounds[1]

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
    def __init__(self, pos=Vect2(0,0)):
        #I may move these defaults to the constructor later
        super(Player, self).__init__(mass = 1, position=pos)

    #Controller is a dict containing the state of the controls
    def input(self, controller):
        #TODO: Shooting mechanism
        if (controller["fire"]):
            pass
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
        points = loop_lines(points)
        return len(points)//2, pyglet.gl.GL_LINES, None, ( 'v2f', points )

    def update(self, dt):
        super().update(dt)
        if self.vel.mag() > MAX_VELOCITY:
            self.vel = self.vel.normalize() * MAX_VELOCITY

class Asteroid(Inertial):
    def __init__(self, size=3, position=Vect2(0,0)):
        #Asteroids come in 3 sizes: 3 is biggest, one is smallest.
        super(Asteroid, self).__init__(mass=size, position=position)
        self.hit_radius = size*10
        #property to check on deletion loop
        self.alive = True
        self.angleV = random.uniform(-.5, .5)
        #Consider making angular velocity a property of spawning/velocity
        self.shape = []
        for i in range(0, 16):
            radius = self.hit_radius * random.uniform(.75, 1.25)
            self.shape.append(math.cos(2*math.pi*i/15)*radius)
            self.shape.append(math.sin(2*math.pi*i/15)*radius)

    def update(self, dt):
        super().update(dt)
        self.angle += self.angleV

    def draw(self):
        points = []
        radius = self.hit_radius
        for i, e in enumerate(self.shape):
            if i % 2 == 0:
                points.append(e + self.pos.x)
            else:
                points.append(e + self.pos.y)
        points = loop_lines(points)
        return (len(points)//2, pyglet.gl.GL_LINES, None, ('v2f', points ))

#Consider particle class, for effects

class Bullet(Movable):
    def __init__(self, pos, vel, angle, lifespan=10):
        super(Bullet, self).__init__(position=pos, angle=angle, velocity=vel)
        self.life=lifespan

    def update(self, dt):
        super().update(dt)
        self.life -= dt

    def isAlive(self):
        return (self.life > 0)

    def draw(self):
        points = [math.cos(self.angle)*-5 + self.pos.x, math.sin(self.angle)*-5 + self.pos.y, math.cos(self.angle) + self.pos.x, math.sin(self.angle) + self.pos.y]
        return 2, pyglet.gl.GL_LINES, None, ('v2f', tuple(points))
