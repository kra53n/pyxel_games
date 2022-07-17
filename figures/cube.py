import pyxel


SCREEN = {
    'wdt': 192,
    'hgt': 108,
    'bg': 3,
    'f': 1,
}


class Cube:
    def __init__(self):
        self.move = (20, 20, 20)
        self.size = 1

        self.vex = (
            ((0 * self.size + self.move[0],
              1 * self.size + self.move[1],
              0 * self.size + self.move[2]),

             (0 * self.size + self.move[0],
              1 * self.size + self.move[1],
              0 * self.size + self.move[2]),
            ),
        )


# class Camera:
#     def __init__(self):
#         # TODO: read https://stackoverflow.com/questions/724219/how-to-convert-a-3d-point-into-2d-perspective-projection
#         pass


class App:
    def __init__(self):
        pyxel.init(SCREEN['wdt'], SCREEN['hgth'], caption=SCREEN['caption'])
        pyxel.run(self.update, self.draw)

    def _update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def _draw(self):
        pyxel.cls(3)


if __main__ == '__name__':
    App()
