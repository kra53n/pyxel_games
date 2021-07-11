import pyxel


class Element:
    def __init__(self, x, y, col, move_step, screen_h, screen_w):
        self.x = x
        self.y = y
        self.col = col
        self.move_step = move_step
        self.screen_h = screen_h
        self.screen_w = screen_w

    @property
    def begin(self):
        return self.y


class Stick(Element):
    def __init__(self, x, y, w, h, col, move_step, screen_h, screen_w):
        super().__init__(x, y, col, move_step, screen_h, screen_w)

        self.w = w
        self.h = h

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.col)

    @property
    def end(self):
        return self.y + self.h
    
    def up(self):
        if self.y > 0:
            self.y = self.y - self.move_step

    def down(self):
        if self.y + self.h < self.screen_h:
            self.y = self.y + self.move_step


class Ball(Element):
    def __init__(self, x, y, col, move_step, screen_h, screen_w, r):
        super().__init__(x, y, col, move_step, screen_h, screen_w)

        self.r = r
        self.move_x = -self.move_step
        self.move_y = self.move_step

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.col)
        self.move()

    def move(self):
        self.x += self.move_x

    def change_x_direction(self):
        if self.move_x > 0:
            self.move_x = -self.move_x
            return
        self.move_x = abs(self.move_x)
