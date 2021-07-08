import pyxel


class Character:
    def __init__(self, x, y, colkey=0):
        self.x = x
        self.y = y
        self.colkey = colkey

    def left_side(self, width=8, height=5):
        pyxel.blt(self.x, self.y, 0, 8, 3, width, height, self.colkey)

    def right_side(self, width=8, height=5):
        pyxel.blt(self.x, self.y, 0, 16, 3, width, height, self.colkey)
