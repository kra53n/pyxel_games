from math import pi, cos, sin
import pyxel


SCREEN = {
    "width": 120,
    "height": 120,
    "bg": 11,
    "fg": 7,
    "caption": "megagon",
}


class Megagon:
    def __init__(self, x, y, w, h, vers_num, fg=SCREEN["fg"]):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vers_num = vers_num
        self.step = 2 * pi / self.vers_num
        self.rotate_pos = 0
        self.rotate_step = pi / 20
        self.fg = fg

    def _coords(self):
        return (
            (round(cos(self.step * vert + self.rotate_pos) * self.w) + self.x,
             round(sin(self.step * vert + self.rotate_pos) * self.h) + self.y)
            for vert in range(1, self.vers_num + 1)
        )

    def _draw_pixels(self):
        for point in self._coords():
            pyxel.pset(point[0], point[1], self.fg)

    def _draw_lines(self):
        coords = tuple(self._coords())
        for i in range(self.vers_num):
            pyxel.line(
                coords[i][0],
                coords[i][1],
                coords[(i+1) % self.vers_num][0],
                coords[(i+1) % self.vers_num][1],
                self.fg,
            )

    def draw(self, elemname):
        elems = {
            "lines": self._draw_lines,
            "pixels": self._draw_pixels,
        }
        elems[elemname]()
        self.rotate_pos -= self.rotate_step


class MegagonsPattern:
    def __init__(
        self,
        x,
        y,
        figure_width: int,
        figure_height: int,
        vers_num: int,
        surface_width=SCREEN["width"],
        surface_height=SCREEN["height"],
        col=SCREEN["fg"]
    ):
        self.x = x
        self.y = y
        self.fig_wdt = figure_width
        self.fig_hgt = figure_height
        self.srf_wdt = surface_width
        self.srf_hgt = surface_height
        self.vers_num = vers_num
        self.col = col

        self._init_elements()

    def _init_elements(self):
        self.elements = []
        for x in range(self.fig_wdt + self.x, self.srf_wdt, self.fig_wdt*2):
            for y in range(self.fig_hgt + self.y, self.srf_hgt, self.fig_hgt*2):
                self.elements.append(
                    Megagon(x, y, self.fig_wdt, self.fig_hgt, self.vers_num, self.col))

    def draw(self, elemname):
        for el in self.elements:
            el.draw(elemname)


class App:
    def __init__(self):
        pyxel.init(SCREEN["width"], SCREEN["height"],
            caption=SCREEN["caption"].capitalize()
        )

        size = min(SCREEN["width"], SCREEN["height"]) // 12
        verts_num = 4
        self.patterns = [
            MegagonsPattern(0, 0, size, size, verts_num),
            MegagonsPattern(1, 3, size, size, verts_num, col=8),
            MegagonsPattern(-3, -1, size, size, verts_num, col=15),
        ]

        pyxel.run(self._update, self._draw)

    def _update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def _draw(self):
        pyxel.cls(SCREEN["bg"])
        # in draw method may be possible using "lines" and "pixels"
        for ptn in self.patterns:
            ptn.draw("lines")


if __name__ == "__main__":
    App()
