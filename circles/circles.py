from random import randrange
from random import choice

import pyxel


SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

colors = [i for i in range(16)]
BG_COLOR = colors.pop(randrange(16))


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    global R

    draw_circ(120, 120)
    draw_circ()
    draw_circ(50, 50)

    R += 1

def draw_circ(x=SCREEN_WIDTH, y=SCREEN_HEIGHT):
    global R
    if (R < y) and (R < y):
        pyxel.circb(x // 2, y // 2, R, choice(colors))

if __name__ == "__main__":
    pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
    R = 0
    pyxel.cls(BG_COLOR)
    pyxel.run(update, draw)
