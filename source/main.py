#Tim McCarty
#CSIT-104 Final Project Entry Point

#Imported libraries and other modules in project.
#Pyglet is a slightly lower-level take on Python graphics than PyGame as I understand it.
import pyglet
from Entity import *
from HUD import HUD
from pyglet.window import key

#Target window size constant
WIDTH = 800
HEIGHT = 400
targetNo = 3; #number of asteroids to spawn

#function to simplify adding entities
def add_entity(ent):
    entities.append(ent)
    pyglet.clock.schedule(ent.update)

#function to spawn player
def spawn_player():
    player = Player(Vect2(x=window.width/2, y=window.height/2))
    return player

#Window object represents the game's window
window = pyglet.window.Window(WIDTH, HEIGHT)
#Keys holds a handler that keeps track of keyboard state, part of pyglet
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

hud = HUD()
entities = []

player = spawn_player()
add_entity(player)

exhaust = ParticleSpawner(Vect2(WIDTH//2, HEIGHT//2), 0, math.pi/4, .01, ParticleFactory(speed=20,color=(255,0,0)), True)
add_entity(exhaust)

@window.event
def on_draw():
    window.clear()
    player = [e for e in entities if isinstance(e, Player)][0]
    #map keys to input object
    #On a proper engine the controller would probably be its own class.
    #That level of abstraction makes it easier to use keyboards, mice, and other controllers the user may have
    controller = {'acc': keys[key.W], 'left': keys[key.A], 'right':keys[key.D], 'fire':keys[key.SPACE]}
    player.input(controller)
    exhaust.angle = (player.angle + math.pi)
    exhaust.pos = player.pos.getCopy()
    if controller['acc']:
        exhaust.active = True
    else:
        exhaust.active = False
    #Batches hold vertexes to feed the graphics card in bulk, which is more efficient than drawing
    #each item
    batch = pyglet.graphics.Batch()

    #Bullet Spawning
    if player.isFiring():
        add_entity(Bullet(player.pos.getCopy(), player.angle))

    #Asteroid Spawning
    asteroids = [e for e in entities if isinstance(e, Asteroid)]
    if len(asteroids) < targetNo:
        newAsteroid = Asteroid(3, Vect2(0,0))
        asteroids.append(newAsteroid)
        add_entity(newAsteroid)

    for asteroid in asteroids:
        if player.overlaps(asteroid.hit_radius, asteroid.pos.getCopy()):
            player.kill()
            #Check if player is actually dead, it may be in invuln period
            if (player.isAlive() != True and hud.has_lives()):
                player = spawn_player()
                hud.kill()
                add_entity(player)
                #TODO: Game over state

#TODO Gameover/Gamestart behavior
#TODO Pause
#TODO Consider Perler Noise for Asteroid shape
#TODO Sound

    #Process asteroid/bullet collisions
    for bullet in [e for e in entities if isinstance(e, Bullet)]:
        for asteroid in asteroids:
            if bullet.overlaps(asteroid.hit_radius, asteroid.pos.getCopy()):
                asteroid.kill()
                add_entity(AsteroidDebris(asteroid.pos.getCopy()))
                if asteroid.size > 1:
                    #add two baby asteroids!
                    add_entity(Asteroid(asteroid.size-1,asteroid.pos.getCopy()))
                    add_entity(Asteroid(asteroid.size-1,asteroid.pos.getCopy()))
                #Remove bullet
                bullet.kill()
                #Log the points
                hud.hit()

    #Batch graphics
    for e in entities:
        batch.add(*e.draw())

    #Remove dead objects from loop and entity list
    for e in entities:
        if not e.isAlive():
            pyglet.clock.unschedule(e.update)
    entities[:] = [e for e in entities if e.isAlive()]
    #Finally draw the frame
    hud.drawHUD()
    batch.draw()
pyglet.app.run()
