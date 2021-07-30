import pyxel


SCREEN_WIDTH = 108
SCREEN_HEIGHT = 132


class Colors:
    bg = 0


class Modes:
    def __init__(self, x=0, y=0, num_of_rows=4, distance=4):
        self.size = 8
        self.x = x
        self.y = y
        self.num_of_rows = num_of_rows
        self.distance = distance

    def draw(self):
        colors = range(16)
        x = self.x
        y = self.y

        for column in colors:
            pyxel.rectb(
                x, y, self.size, 
                self.size, (Colors.bg + 1) % 16
            )
            pyxel.rect(
                x + 1, y + 1, self.size - 2,
                self.size - 2, colors[column]
            )

            self.__touch(x, y, colors[column])

            x += self.size + self.distance
            if (column + 1) % self.num_of_rows == 0:
                x = self.x
                y += self.size + self.distance

    def __touch(self, x, y, color):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and \
           x < pyxel.mouse_x and pyxel.mouse_x < x + self.size and \
           y < pyxel.mouse_y and pyxel.mouse_y < y + self.size:
            Colors.bg = color

    @property
    def width(self):
        return (self.size + self.distance) * self.num_of_rows - self.distance


class App:
    def __init__(self):
        pyxel.init(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
        )

        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(Colors.bg)
        Modes().draw()


if __name__ == "__main__":
    App()
