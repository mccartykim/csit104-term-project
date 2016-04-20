import pyglet
from Entity import *
from pyglet.window import key
WIDTH = 800
HEIGHT = 400

def addEntity(ent):
    entities.append(ent)
    pyglet.clock.schedule(ent.update)

window = pyglet.window.Window(WIDTH, HEIGHT)
#Keys holds a handler that keeps track of keyboard state, part of pyglet
keys = pyglet.window.key.KeyStateHandler()
targetNo = 3; #number of asteroids to spawn
window.push_handlers(keys)

entities = []

player = Player(Vect2(x=window.width/2, y=window.height/2))
addEntity(player)

@window.event
def on_draw():
    window.clear()
    #map keys to input object
    #On a proper engine the controller would probably be its own class.
    controller = {'acc': keys[key.W], 'left': keys[key.A], 'right':keys[key.D], 'fire':keys[key.SPACE]}
    player.input(controller)
    batch = pyglet.graphics.Batch()
    if player.isFiring():
        addEntity(Bullet(player.pos.getCopy(), player.angle))
    #TODO: Score
    asteroids = [e for e in entities if isinstance(e, Asteroid)]
    if len(asteroids) < targetNo:
        nAsteroid = Asteroid(3, Vect2(0,0))
        asteroids.append(nAsteroid)
        addEntity(nAsteroid)
    #Loop over all the entities that are bullets
    for bullet in [e for e in entities if isinstance(e, Bullet)]:
        for asteroid in asteroids:
            if bullet.overlaps(asteroid.hit_radius, asteroid.pos.getCopy()):
                asteroid.alive = False
                if asteroid.size > 1:
                    #add two baby asteroids!
                    addEntity(Asteroid(asteroid.size-1,asteroid.pos.getCopy()))
                    addEntity(Asteroid(asteroid.size-1,asteroid.pos.getCopy()))
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
