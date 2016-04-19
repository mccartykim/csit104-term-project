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

for e in entities:
    pyglet.clock.schedule(e.update)

@window.event
def on_draw():
    window.clear()
    #map keys to input object
    #On a proper engine the controller would probably be its own class.
    controller = {'acc': keys[key.W], 'left': keys[key.A], 'right':keys[key.D], 'fire':keys[key.SPACE]}
    player.input(controller)
    batch = pyglet.graphics.Batch()
    if player.isFiring():
        bullet = Bullet(player.pos.getCopy(), player.angle)
        pyglet.clock.schedule(bullet.update)
        entities.append(bullet)
    #TODO: Score
    #TODO: Asteroid spawner
    #Loop over all the entities that are bullets
    for bullet in [e for e in entities if isinstance(e, Bullet)]:
        for asteroid in [e for e in entities if isinstance(e, Asteroid)]:
            if bullet.overlaps(asteroid.hit_radius, asteroid.pos.getCopy()):
                print("Overlap")
                asteroid.alive = False
                bullet.life = 0
    for e in entities:
        batch.add(*e.draw())
    #TODO: Lives
    for e in entities:
        if not e.isAlive():
            pyglet.clock.unschedule(e.update)
            entities[:] = [e for e in entities if e.isAlive()]
    batch.draw()

pyglet.app.run()
