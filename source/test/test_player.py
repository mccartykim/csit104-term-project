import pytest
from Entity import *
from Vect2 import *

def test_init():
    t = Player()
    assert t.pos.x == 0 and t.pos.y == 0

#TODO: Test input

#TODO: Test clamping velocity

def test_update():
    t = Player()
    t.acc = Vect2(1,0)
    t.update(1)
    assert t.acc.x == 0 and t.vel.x==1 and t.pos.x==1
