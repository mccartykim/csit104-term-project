import pyglet

class HUD(object):
    def __init__(self):
        #Constants
        self.HIT_POINTS = 100
        self.INIT_LIVES = 3
        self.WIDTH = 800
        self.points = 0
        self.lives = self.INIT_LIVES
    def drawHUD(self):
        pyglet.text.Label(str(self.points), x=5, y=5).draw()
        ship_chr = '\u0394'
        pyglet.text.Label(ship_chr * self.lives, x=self.WIDTH-5, y=5, anchor_x='right').draw()

    def hit(self):
        self.points+=self.HIT_POINTS
