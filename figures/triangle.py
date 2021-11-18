from sys import exit
import pyxel


screen = {
    "wdt": 160,
    "hgt": 90,
    "bg": 11,
}


class Tri:
    def __init__(self, coords=None, col=3, r=2, col_r=7):
        self.coords = coords
        if not self.coords:
            self.coords = {
                "x1": 10, "y1": 10,
                "x2": 30, "y2": 20,
                "x3": 40, "y3": 20,
            }
        self.col = col
        self.r = r
        self.col_r = col_r
        self.coords_iter = range(1, len(self.coords) // 2 + 1)

    def _draw_tri(self):
        pyxel.line(self.coords["x1"], self.coords["y1"],
            self.coords["x2"], self.coords["y2"], self.col)
        pyxel.line(self.coords["x2"], self.coords["y2"],
            self.coords["x3"], self.coords["y3"], self.col)
        pyxel.line(self.coords["x3"], self.coords["y3"],
            self.coords["x1"], self.coords["y1"], self.col)

    def _draw_circs_about_vertexes(self):
        for i in self.coords_iter:
            pyxel.circb(
                self.coords[f"x{i}"], self.coords[f"y{i}"], self.r, self.col_r)

    def _draw_chevy(self):
        pyxel.line(
            self.coords["x1"],
            self.coords["y1"],
            (self.coords["x3"] + self.coords["x2"]) // 2,
            (self.coords["y3"] + self.coords["y2"]) // 2,
            self.col,
        )
        pyxel.line(
            self.coords["x2"],
            self.coords["y2"],
            (self.coords["x1"] + self.coords["x3"]) // 2,
            (self.coords["y1"] + self.coords["y3"]) // 2,
            self.col,
        )
        pyxel.line(
            self.coords["x3"],
            self.coords["y3"],
            (self.coords["x1"] + self.coords["x2"]) // 2,
            (self.coords["y1"] + self.coords["y2"]) // 2,
            self.col,
        )

    def _update(self):
        for i in self.coords_iter:
            x, y = self.coords[f"x{i}"], self.coords[f"y{i}"]
            if x - self.r <= pyxel.mouse_x <= x + self.r and \
               y - self.r <= pyxel.mouse_y <= y + self.r and \
               pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                self.coords[f"x{i}"] = pyxel.mouse_x
                self.coords[f"y{i}"] = pyxel.mouse_y

    def draw(self):
        self._update()
        self._draw_tri()
        #self._draw_chevy()
        self._draw_circs_about_vertexes()


class App:
    def __init__(self):
        pyxel.init(screen["wdt"], screen["hgt"])

        pyxel.mouse(True)
        self.tr1 = Tri()

        pyxel.run(self._update, self._draw)

    def _update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def _draw(self):
        pyxel.cls(screen["bg"])
        self.tr1.draw()


if __name__ == "__main__":
    App()
