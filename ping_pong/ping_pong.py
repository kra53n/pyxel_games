import pyxel


SCREEN_WIDTH = 192
SCREEN_HEIGHT = 108
SCREEN_CAPTION = "PyxelPingPong | PPP"
SCREEN_SCALE = 1
SCREEN_FPS = 60

STICK_WIDTH = 3
STICK_HEIGHT = 9
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

    def draw_stick(self, x, y):
        pass


if __name__ == "__main__":
    App()
