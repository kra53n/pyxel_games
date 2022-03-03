from random import randrange
from random import choice

import pyxel


SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

colors = [i for i in range(16)]
BG_COLOR = colors.pop(randrange(16))


def generate_center_circs(*center_circs, amount):
    center_circs = list(center_circs)
    avoid = center_circs[:]
    while amount != len(center_circs):
        x, y = randrange(0, SCREEN_WIDTH + 1), randrange(0, SCREEN_HEIGHT + 1)

        if len([[x2, y2] for x2, y2 in avoid if x == x2 and y == y2]) > 0:
            continue
        for x2, y2 in center_circs:
            if (abs(x2 - x) <= 20) or (abs(y2 - y) <= 20):
                avoid.append([x, y])
                continue
        center_circs.append([x, y])
    return center_circs

CENTER_CIRCS = generate_center_circs(
    [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2],
    [5, 5],
    amount=25,
)


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    global R

    draw_circs(CENTER_CIRCS)
    R += 1

def draw_circs(circs_center):
    for c in circs_center:
        draw_circ(c[0], c[1])

def draw_circ(x, y):
    global R
    if (0 < R) and (R < y):
        pyxel.circb(x, y, R, choice(colors))

if __name__ == "__main__":
    pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
    R = 0
    pyxel.cls(BG_COLOR)
    pyxel.run(update, draw)
