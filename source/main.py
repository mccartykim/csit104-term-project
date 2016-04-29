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

# If true, program will save a series of PNG images for FFMPEG or similar
# To create videos, and use frame as a variable to index the files.
RECORD = False
frame = 0
# Flag to change for gamequitting event
quit = False
state = StateManager()

# Clock is a pyglet object that controls framerate
clock.set_fps_limit(30)
while (not quit):
        dt = clock.tick()
        state.window.switch_to()
        state.window.dispatch_events()
        state.loop(dt)
        quit = state.is_quit()
        state.window.flip()
        if RECORD:
            # This long snippet just takes a copy of the frame buffer, and dumps it to a file.
            # With software like ffmpeg, I can stitch these stills together to recreate the game.
            # Source: Pyglet's documentation
            pyglet.image.get_buffer_manager().get_color_buffer().save("video/frame{:05}.png".format(frame))
            frame+= 1
