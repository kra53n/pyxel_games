import pyxel


def update():
    pass

def draw(x, y, dx, dy):
    if x == 192 or x == 0:
        dx = change_diration(dx)
    if y == 108 or y == 0:
        dy = change_diration(dy)
    pyxel.circb(x, y, 3, 5)
    print(x, y, dx, dy)
    return dx, dy

def change_diration(n):
    if n > 0:
        return -n
    return abs(n)


if __name__ == "__main__":
    pyxel.init(192, 108)
    x, y = 3, 3
    dx, dy = 3, 3

    while True:
        pyxel.cls(0)

        dx, dy = draw(x, y, dx, dy)
        x += dx; y += dy

        pyxel.flip()
