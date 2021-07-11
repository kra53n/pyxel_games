import pyxel


class Element:
    def __init__(self, col, move_step, screen_h, screen_w):
        self.col = col
        self.move_step = move_step
        self.screen_h = screen_h
        self.screen_w = screen_w

    @property
    def begin(self):
        return self.x


class Stick(Element):
    def __init__(self, x, y, w, h, col, move_step, screen_h, screen_w):
        super().__init__(col, move_step, screen_h, screen_w)

        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.col)

    @property
    def end(self):
        return self.x + self.h
    
    def up(self):
        if self.y > 0:
            self.y = self.y - self.move_step

    def down(self):
        if self.y + self.h < self.screen_h:
            self.y = self.y + self.move_step


class Ball(Element):
    def __init__(self, r,):
        super().__init__(col, move_step, screen_h, screen_w)

    def draw(self):
        pyxel.circ(self.x, self.y,)
