from math import pi, cos, sin,
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
        x_coords = [round(cos(self.step * i + self.rotate_pos) * self.w) + self.x
            for i in range(1, self.vers_num + 1)]
        y_coords = [round(sin(self.step * i + self.rotate_pos) * self.h) + self.y
            for i in range(1, self.vers_num + 1)]

        return zip(x_coords, y_coords)

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
        self.figure_width = figure_width
        self.figure_height = figure_height
        self.surface_width = surface_width
        self.surface_height = surface_height
        self.vers_num = vers_num
        self.col = col

        self._init_elements()

    def _init_elements(self):
        self.elements = []
        for x in range(
            self.figure_width + self.x,
            self.surface_width,
            self.figure_width*2
        ):
            for y in range(
                self.figure_height + self.y,
                self.surface_height,
                self.figure_height*2
            ):
                self.elements.append(Megagon(
                    x,
                    y,
                    self.figure_width,
                    self.figure_height,
                    self.vers_num,
                    self.col,
                ))

    def draw(self, elemname):
        [el.draw(elemname) for el in self.elements]


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
        [ptn.draw("lines") for ptn in self.patterns]


if __name__ == "__main__":
    App()