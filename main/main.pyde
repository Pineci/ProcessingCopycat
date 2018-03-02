from slipnet import *
from slipnetInitialize import *

def setup():
    size(600, 600)
    colorMode(HSB)
    noStroke()
    l = link(1, 2, 3)
    """s = slipnet()
    a = node('a', 1)
    b = node('b', 2)
    c = node('c', 3)
    d = node('d', 4)
    e = node('e', 5)
    f = node('f', 6)
    s.addNode(a)
    s.addNode(b)
    s.addNode(c)
    s.addNode(d)
    s.addNode(e)
    s.addNode(f)
    s.addLink('a', 'b', link('1', 0, 10))
    s.addLink('a', 'c', link('2', 0, 10))
    s.addLink('a', 'f', link('3', 0, 10))
    s.addLink('f', 'a', link('4', 0, 10))
    s.addLink('b', 'd', link('5', 0, 10))
    s.addLink('e', 'f', link('6', 0, 10))
    s.addLink('d', 'f', link('7', 0, 10))
    print(s.getLink('a', 'b'))
    print(s.getLinkTo('f'))"""
    print(s)


def draw():
    fill(0x11000000)
    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)
    ellipse(mouseX, mouseY, 20, 20)