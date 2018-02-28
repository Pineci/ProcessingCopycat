from slipnet import slipnet, node, link

def setup():
    size(600, 600)
    colorMode(HSB)
    noStroke()
    l = link(1, 2, 3)
    s = slipnet()
    a = node('a', 1)
    b = node('b', 2)
    c = node('c', 3)
    s.addNode(a)
    s.addNode(b)
    s.addNode(c)
    s.addLink('a', 'b', link('test', 0, 10))
    print(s.getLink('a', 'b'))
    print(s)


def draw():
    fill(0x11000000)
    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)
    ellipse(mouseX, mouseY, 20, 20)