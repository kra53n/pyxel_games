import pyxel

import constants


class App:
    def __init__(self):
        pyxel.init(
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            caption=constants.SCREEN_TITLE,
            fps=constants.SCREEN_FPS,
            scale=constants.SCREEN_SCALE,
        )

        pyxel.run(self.update, self.draw)

    def update(self):
        pass
    
    def draw(self):
        pass


App()
