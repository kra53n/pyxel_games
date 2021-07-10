import pyxel

from screen_resolution import get_monitor_resolution


SCREEN_WIDTH, SCREEN_HEIGHT = [i // 10 for i in get_monitor_resolution()]
SCREEN_CAPTION = "PyxelPingPong | PPP"
SCREEN_SCALE = 1
SCREEN_FPS = 60

STICK_WIDTH = 2
STICK_HEIGHT = 30
STICK_MARGIN = 3

COLOR_STICK_PLAYER = 8
COOR_STICK_ENEMY = 8

KEY_START = pyxel.KEY_ENTER


class App:
    def __init__(self):
        pyxel.init(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            caption=SCREEN_CAPTION,
            scale=SCREEN_SCALE,
            fps=SCREEN_FPS,
            quit_key=pyxel.KEY_Q,
            fullscreen=True,
        )

        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass

    def draw(self):
        pyxel.cls(1)
        self.draw_stick(STICK_MARGIN, 0)
        self.draw_stick(SCREEN_WIDTH - STICK_MARGIN - STICK_WIDTH, 0)

    def draw_stick(self, x, y, color=COLOR_STICK_PLAYER):
        pyxel.rect(x, y, STICK_WIDTH, STICK_HEIGHT, color)


if __name__ == "__main__":
    App()
