import pyglet
from Entity import *
from pyglet.window import key
window = pyglet.window.Window()
#Keys holds a handler that keeps track of keyboard state, part of pyglet
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)
#label = pyglet.text.Label('Hello world', font_name="Times New Roman", font_size=36, x = window.width//2, y = window.height//2, anchor_x='center', anchor_y='center')

player = Player(Vect2(x=window.width/2, y=window.height/2))
#player.input({'acc': True, 'left':True, 'right':False})
pyglet.clock.schedule(player.update)
@window.event
def on_draw():
    window.clear()
    #map keys to input object
    #On a proper engine the controller would probably be its own class.
    controller = {'acc': keys[key.W], 'left': keys[key.A], 'right':keys[key.D], 'fire':key.SPACE}
    player.input(controller)
    #label.draw()
    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, player.draw())
    #print(player.pos.x, " ", player.pos.y, player.angle)

pyglet.app.run()
