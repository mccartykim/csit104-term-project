import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label('Hello world', font_name="Times New Roman", font_size=36, x = window.width//2, y = window.height//2, anchor_x='center', anchor_y='center')

#TODO: Vector class:
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


#TODO: Model basic entity for game.
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


#TODO: Update function with delta-t

#TODO: Draw function
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
