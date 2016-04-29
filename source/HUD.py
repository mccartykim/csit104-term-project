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
        # Create a label for current score
        pyglet.text.Label(str(self.points), x=5, y=5).draw()
        # This is a codepoint for the unicode Delta character, which looks like the ship.
        ship_chr = '\u0394'
        pyglet.text.Label(ship_chr * self.lives, x=self.WIDTH-5, y=5, anchor_x='right').draw()

# Log when the player scores a hit
    def hit(self):
        self.points+=self.HIT_POINTS

# Log when the player loses a life
    def kill(self):
        self.lives -=1

# Check if the player has another life
    def has_lives(self):
        return (self.lives > 0)

# Log if the player gains a life (say through a powerup)
    def get_life(self):
        self.lives += 1
