import pyxel


SCREEN_WIDTH = 108
SCREEN_HEIGHT = 132


class Colors:
    bg = 0


class ColorSetter:
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


class Stick:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        self.__dragging()
        pyxel.line(self.x1, self.y1, self.x2, self.y2, (Colors.bg + 1) % 16)

    def __dragging(self):
        if self.x1 - 10 < pyxel.mouse_x and pyxel.mouse_x < self.x1 + 10 and \
           self.y1 - 10 < pyxel.mouse_y and pyxel.mouse_y < self.y1 + 10 and \
           pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            self.x1 = pyxel.mouse_x
            self.y1 = pyxel.mouse_y
            print(self.x1, self.y1)

        if self.x2 - 10 < pyxel.mouse_x and pyxel.mouse_x < self.x2 + 10 and \
           self.y2 - 10 < pyxel.mouse_y and pyxel.mouse_y < self.y2 + 10 and \
           pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            print(pyxel.mouse_x, pyxel.mouse_y)
            self.x2 = pyxel.mouse_x
            self.y2 = pyxel.mouse_y


class App:
    def __init__(self):
        pyxel.init(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
        )

        self.drawing_switcher = {
            "color_setter": False
        }

        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(Colors.bg)

        if self.drawing_switcher["color_setter"]:
            ColorSetter(x=(SCREEN_WIDTH - 44) // 2, y=(SCREEN_HEIGHT - 44) // 2).draw()

        Stick(44, 120, SCREEN_WIDTH - 44, 120).draw()

        self.__buttons_press_check()

    def __buttons_press_check(self):
        if pyxel.btnp(pyxel.KEY_C):
            if self.drawing_switcher["color_setter"]:
                self.drawing_switcher["color_setter"] = False
            else:
                self.__change_drawing_switcher("color_setter")

    def __change_drawing_switcher(self, to_switch):
        for key in self.drawing_switcher.keys():
            if key == to_switch:
                self.drawing_switcher[key] = True
                continue
            self.drawing_switcher[key] = False


if __name__ == "__main__":
    App()
