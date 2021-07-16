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

    @property
    def left_side(self):
        return self.x


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

    @property
    def right_side(self):
        return self.x + self.w


class StickEnemy(Stick):
    pass


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
        self.y += self.move_y

    def change_x_direction(self):
        if self.move_x > 0:
            self.move_x = -self.move_x
            return
        self.move_x = abs(self.move_x)

    def change_y_direction(self):
        if self.move_y > 0:
            self.move_y = -self.move_y
            return
        self.move_y = abs(self.move_y)

    def return_to_center(self):
        self.x = self.screen_w // 2
        self.y = self.screen_h // 2


class Text:
    def __init__(self, screen_h, screen_w):
        self.screen_h = screen_h
        self.screen_w = screen_w


class GameStatus(Text):
    def __init__(self, screen_h, screen_w):
        super().__init__(screen_h, screen_w)
    
    def lost(self):
        pyxel.text(0, 0, "Game lost", pyxel.frame_count // 10 % 16)


class Score(Text):
    def __init__(self, screen_h, screen_w, col):
        super().__init__(screen_h, screen_w)

        self.col = col
        self.player = 0
        self.enemy = 0

    def draw(self):
        pyxel.text(
            self.__x_coord(),
            0,
            f"{self.player}:{self.enemy}",
            self.col
        )

    def __width(self):
        """
        Define width of text
            1 digit takes 4 pixels
            1 colons takes 3 pixelx
        """
        digits = len(str(self.player)) + len(str(self.enemy))
        return (digits * 4) + 3

    def __x_coord(self):
        """
        Define x coord for spawning text in the middle
        """
        return (self.screen_w - self.__width()) // 2
