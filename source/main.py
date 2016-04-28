# Tim McCarty
# CSIT-104 Final Project Entry Point

# Imported libraries and other modules in project.
# Pyglet is a slightly lower-level take on Python graphics than PyGame as
# I understand it.
import pyglet
from pyglet import clock
from Entity import *
from HUD import HUD
from pyglet.window import key
from StateManager import StateManager

quit = False
state = StateManager()

while (not quit):
        dt = clock.tick()
        state.window.switch_to()
        state.window.dispatch_events()
        state.loop(dt)
        quit = state.is_quit()
        state.window.flip()
# TODO Consider Perler Noise for Asteroid shape
# TODO Sound
