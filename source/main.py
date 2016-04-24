import pyglet
from Entity import *
from HUD import HUD
from pyglet.window import key
WIDTH = 800
HEIGHT = 400

def add_entity(ent):
    entities.append(ent)
    pyglet.clock.schedule(ent.update)

def spawn_player():
    player = Player(Vect2(x=window.width/2, y=window.height/2))
    return player

window = pyglet.window.Window(WIDTH, HEIGHT)
#Keys holds a handler that keeps track of keyboard state, part of pyglet
keys = pyglet.window.key.KeyStateHandler()

targetNo = 3; #number of asteroids to spawn
window.push_handlers(keys)

hud = HUD()
entities = []

player = spawn_player()
add_entity(player)

@window.event
def on_draw():
    window.clear()
    player = [e for e in entities if isinstance(e, Player)][0]
    #map keys to input object
    #On a proper engine the controller would probably be its own class.
    controller = {'acc': keys[key.W], 'left': keys[key.A], 'right':keys[key.D], 'fire':keys[key.SPACE]}
    player.input(controller)
    batch = pyglet.graphics.Batch()
    if player.isFiring():
        add_entity(Bullet(player.pos.getCopy(), player.angle))
    asteroids = [e for e in entities if isinstance(e, Asteroid)]
    if len(asteroids) < targetNo:
        newAsteroid = Asteroid(3, Vect2(0,0))
        asteroids.append(newAsteroid)
        add_entity(newAsteroid)
    #Loop over all the entities that are bullets
    for asteroid in asteroids:
        if player.overlaps(asteroid.hit_radius, asteroid.pos.getCopy()):
            hud.kill()
            player.kill()
            player = spawn_player()
            add_entity(player)
#TODO Invincibility on respawn
#TODO Gameover/Gamestart behavior
#TODO Pause
    for bullet in [e for e in entities if isinstance(e, Bullet)]:
        for asteroid in asteroids:
            if bullet.overlaps(asteroid.hit_radius, asteroid.pos.getCopy()):
                asteroid.kill()
                if asteroid.size > 1:
                    #add two baby asteroids!
                    add_entity(Asteroid(asteroid.size-1,asteroid.pos.getCopy()))
                    add_entity(Asteroid(asteroid.size-1,asteroid.pos.getCopy()))
                #Remove bullet
                bullet.kill()
                #Log the points
                hud.hit()

    for e in entities:
        batch.add(*e.draw())
    for e in entities:
        if not e.isAlive():
            pyglet.clock.unschedule(e.update)
    for e in entities:
        if not e.isAlive():
            entities[:] = [e for e in entities if e.isAlive()]
    hud.drawHUD()
    batch.draw()
pyglet.app.run()
