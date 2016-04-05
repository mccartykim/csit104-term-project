import pyglet
from Entity import *
window = pyglet.window.Window()

label = pyglet.text.Label('Hello world', font_name="Times New Roman", font_size=36, x = window.width//2, y = window.height//2, anchor_x='center', anchor_y='center')

player = Player()
player.input({'acc': True, 'left':True, 'right':False})
pyglet.clock.schedule(player.update)
@window.event
def on_draw():
    window.clear()
    player.input({'acc': True, 'left':False, 'right':False})
    label.draw()
    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, player.draw())
    #print(player.pos.x, " ", player.pos.y, player.angle)

pyglet.app.run()
