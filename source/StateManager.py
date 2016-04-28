# This class manages the game's state

import pyglet
from pyglet import clock
from Entity import Asteroid, AsteroidDebris, Player
from Entity import ParticleSpawner, ParticleFactory, Bullet
from HUD import HUD
from pyglet.window import key
from Vect2 import Vect2
import math

# Target window size constant
WIDTH = 800
HEIGHT = 400
targetNo = 3   # number of asteroids to spawn

class StateManager(object):
    def __init__(self):
        self.quit = False
        self._init_window()
        self._init_game()
        

    def _init_window(self):
# Window object represents the game's window
        self.window = pyglet.window.Window(WIDTH, HEIGHT)
# Keys holds a handler that keeps track of keyboard state, part of pyglet
        self.keys = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(self.keys)


    # Stage the game
    def _init_game(self):
        self.hud = HUD()
        self.entities = []
        self.spawn_player()
        self.exhaust = ParticleSpawner(
            self.player.pos.getCopy(),
            self.player.angle + math.pi,
            math.pi / 4, .01,
            ParticleFactory(speed=20, color=(255, 0, 0)),
            True)
        self.entities.append(self.exhaust)

    def spawn_player(self):
        self.player = Player(Vect2(x=self.window.width/2, y=self.window.height/2))
        self.entities.append(self.player)

    def game_loop(self, dt):
        #Clear frame before looping
        self.window.clear()

        #print(pyglet.gl.get_current_context())
        # On a proper engine the controller would probably be its own class.
        # That level of abstraction makes it easier to use keyboards, mice, and
        # other controllers the user may have
        controller = {
            'acc': self.keys[key.W],
            'left': self.keys[key.A],
            'right': self.keys[key.D],
            'fire': self.keys[key.SPACE],
            'quit': self.keys[key.ESCAPE]
        }
        self.quit = controller['quit']
        self.player.input(controller)
        #turn on thrust effect if ship is accelerating
        self.exhaust.active = controller['acc']
        self.exhaust.angle = (self.player.angle + math.pi)
        self.exhaust.pos = self.player.pos.getCopy()

        self.spawn_bullets()
        self.spawn_asteroids()
        self.detect_collisions()

        for e in self.entities:
            e.update(dt)

        #for e in self.entities:
        #    print(e)
        batch = pyglet.graphics.Batch()
        for e in self.entities:
            # batch.add expects a series of arguments
            # most easily delivered as a tuple.
            # * is the untuple argument.
            batch.add(*e.draw())

        # Filter out any dead objects
        self.entities[:] = [e for e in self.entities if e.isAlive()]
        # Draw objects to the frame
        batch.draw()
        self.hud.drawHUD()


    def spawn_bullets(self):
        if self.player.isFiring():
                self.entities.append(
                    Bullet(
                        self.player.pos.getCopy(), 
                        self.player.angle
                    )
                )


    def spawn_asteroids(self):
        # Asteroid Spawning
        asteroids = [e for e in self.entities if isinstance(e, Asteroid)]
        if len(asteroids) < targetNo:
                newAsteroid = Asteroid(3, Vect2(0, 0))
                self.entities.append(newAsteroid)

    def detect_collisions(self):

        asteroids = [e for e in self.entities if isinstance(e, Asteroid)]
        for asteroid in asteroids:
                if self.player.overlaps(asteroid.hit_radius, asteroid.pos.getCopy()):
                        self.player.kill()
                        # Check if player is actually dead, it may be in invuln
                        # period
                        if (self.player.isAlive() != True and self.hud.has_lives()):
                                self.spawn_player()
                                self.hud.kill()
                                # TODO: Game over state
        # Process asteroid/bullet collisions
        for bullet in [e for e in self.entities if isinstance(e, Bullet)]:
                for asteroid in asteroids:
                        if bullet.overlaps(
                                asteroid.hit_radius,
                                asteroid.pos.getCopy()):
                                asteroid.kill()
                                self.entities.append(
                                    AsteroidDebris(
                                        asteroid.pos.getCopy()))
                                if asteroid.size > 1:
                                        # add two baby asteroids!
                                        self.entities.append(
                                                   Asteroid(
                                                       asteroid.size - 1,
                                                       asteroid.pos.getCopy()))
                                        self.entities.append(
                                                   Asteroid(
                                                       asteroid.size - 1,
                                                       asteroid.pos.getCopy()))
                                # Remove bullet
                                bullet.kill()
                                # Log the points
                                self.hud.hit()
    def is_quit(self):
        return self.quit

    @self.window.event
    def on_close():
        close()
