from random import choice
import pyxel


CHANGE_RADIUS = [3, 3, 4, 5, 6, 7, 8, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3]

colors = [i for i in range(16)]
bg_color = colors.pop(0)
color_ball = choice(colors)


def update():
    pass

def draw(x, y, dx, dy, r):
    global change_radius, color_ball

    if x + r + 1 >= 192 or x - r <= 0:
        dx = change_diration(dx)
        change_radius = True
    if y + r + 1 >= 108 or y - r <= 0:
        dy = change_diration(dy)
        change_radius = True

    pyxel.circb(x, y, r, color_ball)

    return dx, dy

def change_diration(n):
    global color_ball

    cb = choice(colors)
    while cb == color_ball:
        cb = choice(colors)
    color_ball = cb

    cb = choice(colors)
    if n > 0:
        return -n
    return abs(n)


if __name__ == "__main__":
    global change_radius

    pyxel.init(192, 108, quit_key=pyxel.KEY_Q)
    x, y = 10, 10
    dx, dy = 1, 1
    r = 3
    change_radius = False
    radii = CHANGE_RADIUS[:]

    while True:
        if change_radius:
            if not radii:
                radii = CHANGE_RADIUS[:]
                change_radius = False
            r = radii.pop(0)

        pyxel.cls(bg_color)

        dx, dy = draw(x, y, dx, dy, r)
        x += dx; y += dy

        pyxel.flip()
