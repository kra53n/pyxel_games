import pyxel


SCREEN = {
    "wdt": 108,
    "hgt": 108,
}


class Graphic:
    def __init__(self, formula: str, clr: int):
        self.formula = formula
        self.clr = clr

    def draw(self):
        for x in range(SCREEN["hgt"] * 10):
            print(x, eval(self.formula))
            pyxel.pset(x, -eval(self.formula) / 10, self.clr)

class App:
    def __init__(self):
        pyxel.init(SCREEN["hgt"], SCREEN["wdt"])

        self.parabola = Graphic("-x^2", 13)

        pyxel.run(self._update, self._draw)

    def _update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def _draw(self):
        pyxel.cls(0)
        self.parabola.draw()

if __name__ == "__main__":
    App()
