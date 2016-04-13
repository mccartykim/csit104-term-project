import pyglet
from Entity import *
from pyglet.window import key
WIDTH = 800
HEIGHT = 400
window = pyglet.window.Window(WIDTH, HEIGHT)
#Keys holds a handler that keeps track of keyboard state, part of pyglet
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

player = Player(Vect2(x=window.width/2, y=window.height/2))
pyglet.clock.schedule(player.update)

test_asteroid = Asteroid()
test_asteroid.vel = Vect2(1, 1)
pyglet.clock.schedule(test_asteroid.update)

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
    batch.add(*test_asteroid.draw())
    #TODO: Lives
    #TODO: Batch graphics
    batch.add(*player.draw())
    batch.draw()

pyglet.app.run()
