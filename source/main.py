import pyglet
from Entity import *
from pyglet.window import key
WIDTH = 800
HEIGHT = 400
window = pyglet.window.Window(WIDTH, HEIGHT)
#Keys holds a handler that keeps track of keyboard state, part of pyglet
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

entities = []

player = Player(Vect2(x=window.width/2, y=window.height/2))
entities.append(player)

test_asteroid = Asteroid()
test_asteroid.vel = Vect2(5,5)
entities.append(test_asteroid)

test_bullet = Bullet(Vect2(0,0), Vect2(50,50), (math.pi/4))
entities.append(test_bullet)

for e in entities:
    pyglet.clock.schedule(e.update)

@window.event
def on_draw():
    window.clear()
    #map keys to input object
    #On a proper engine the controller would probably be its own class.
    controller = {'acc': keys[key.W], 'left': keys[key.A], 'right':keys[key.D], 'fire':key.SPACE}
    player.input(controller)
    batch = pyglet.graphics.Batch()
    #TODO: Score
    #TODO: Asteroids
    for e in entities:
        batch.add(*e.draw())
    #TODO: Lives
    #TODO: Batch graphics
    for e in entities:
        if not e.isAlive():
            entities.remove(e)
    batch.draw()

pyglet.app.run()
