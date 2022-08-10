import pyxel

import constants
import maps
import character


class App:
    def __init__(self):
        pyxel.init(
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            title=constants.SCREEN_TITLE,
            fps=constants.SCREEN_FPS,
        )

        self.ch = character.Character(40, 40)

        pyxel.load(constants.RESOURCE_FILE)
        pyxel.tilemap(0)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        maps.draw_start()
        #self.ch.left_side()
        self.ch.right_side()


App()
