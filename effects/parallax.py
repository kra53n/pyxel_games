import pyxel as px


WDT = 256
HGT = 256


class Block:
    def __init__(self, x, y, w, h, col, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.speed = speed

        self.x_scroll = None
        self.y_scroll = None

    def update(self, x, y):
        self.x_scroll = x / self.speed
        self.y_scroll = y / self.speed

    def draw(self):
        px.rect(self.x + self.x_scroll, self.y + self.y_scroll, self.w, self.h, self.col)


class Player:
    def __init__(self, x, y, w, h, col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col

        self._speed_movement = 7

        self._vel = 0
        self._acc = 0

        self._acc_speed = 0.5
        self._max_hgt = HGT - 100
        self._is_jumping = False
        self._is_falling = False
    
    def _jump(self):
        if not self._is_falling:
            self._is_jumping = True

    def _update_gravi(self):
        if self._is_jumping:
            self._acc -= self._acc_speed
        if self._is_falling:
            self._acc += self._acc_speed

        self._vel += self._acc
        self.y += self._vel

        if self.y + self.h > HGT:
            self.y = HGT - self.h
            self._vel = 0
            self._acc = 0
            self._is_falling = False

        if self.y < self._max_hgt:
            self._acc = 0
            self._vel = 0
            self._is_jumping, self._is_falling = self._is_falling, self._is_jumping
            self.y = self._max_hgt

    def update(self):
        self._update_gravi()

        if px.btn(px.KEY_SPACE):
            self._jump()
        if px.btn(px.KEY_A):
            self.x -= self._speed_movement
        if px.btn(px.KEY_D):
            self.x += self._speed_movement

    def draw(self):
        px.rect(self.x, self.y, self.w, self.h, self.col)


class App:
    def __init__(self):
        px.init(WDT, HGT)

        col = 5
        self.blocks = (
            Block(1, 140, 120, 230, col, 43),
            Block(123, 130, 120, 230, col, 43),
            Block(23, 180, 100, 230, col + 1, 12),
            Block(136, 190, 80, 230, col + 1, 12),
        )
        self.player = Player(12, HGT, 25, 30, 3)

        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        self.player.update()

        for block in self.blocks:
            block.update(self.player.x, -self.player.y)

    def draw(self):
        px.cls(1)

        for block in self.blocks:
            block.draw()

        self.player.draw()


if __name__ == '__main__':
    App()
