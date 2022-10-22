from dataclasses import dataclass

import pyxel as px
import png


SCREEN_W = 16
SCREEN_H = 16
SCREEN_TITLE = '16bit editor'


one_of_btns = lambda *keys: any(map(lambda k: px.btnp(k), keys))
all_of_btns = lambda *keys: all(map(lambda k: px.btnp(k), keys))


def load_palette() -> list:
    return [(h // 256**2, h // 256 % 256, h % 256) for h in px.colors]


@dataclass
class HistoryElem:
    x: int = 0
    y: int = 0
    prv_col: int = 0
    nxt_col: int = 0

    def __iter__(self):
        elems = self.x, self.y, self.prv_col, self.nxt_col
        for elem in elems:
            yield elem

    def __eq__(self, other):
        if type(other) != HistoryElem:
            return
        return all((self.x == other.x,
                    self.y == other.y,
                    self.prv_col == other.prv_col,
                    self.nxt_col == other.nxt_col))


class History:
    def __init__(self):
        self._stack = []
        self._idx = 0

    def add(self, x: int, y: int, img: int, col: int):
        elem = HistoryElem(x, y, img[y][x], col)
        print(self._stack)
        if elem in self._stack:
            return
        self._idx += 1
        self._stack = self._stack[:self._idx]
        self._stack.append(elem)

    def undo(self, img: list):
        if self._idx > 0:
            self._idx -= 1
            x, y, col, _ = self._stack[self._idx]
            img[y][x] = col

    def recover(self, img: list):
        if self._idx < len(self._stack) - 1:
            self._idx += 1
            x, y, _, col = self._stack[self._idx]
            img[y][x] = col

class Image:
    def __init__(self):
        self._w = SCREEN_W
        self._h = SCREEN_H
        self._pixels = [[0] * self._w for _ in range(self._h)]
        self._history = History()

    def save(self):
        filename = f'{(SCREEN_W + SCREEN_H) // 2}_bit editor.png'
        f = open(filename, 'wb')
        w = png.Writer(SCREEN_W, SCREEN_H, palette=load_palette())
        w.write(f, self._pixels)
        f.close()

    def _clear(self, col):
        for x in range(self._w):
            for y in range(self._h):
                self._pixels[y][x] = col

    def update(self, **kw):
        assert 'col' in kw, 'should pass col as argument for update method'
        col = kw['col']

        if px.btn(px.MOUSE_BUTTON_LEFT):
            self._history.add(px.mouse_x, px.mouse_y, self._pixels, col)
            self._pixels[px.mouse_y][px.mouse_x] = col
        if px.btnp(px.KEY_C):
            self._clear(col)
        if px.btnp(px.KEY_S):
            self.save()

        if px.btnp(px.KEY_Z):
            self._history.undo(self._pixels)
        if px.btnp(px.KEY_X):
            self._history.recover(self._pixels)

    def draw(self):
        for x in range(self._w):
            for y in range(self._h):
                px.pset(x, y, self._pixels[y][x])


class Editor:
    def __init__(self):
        px.init(SCREEN_W, SCREEN_H, title=SCREEN_TITLE)

        self.img = Image()
        self.cur_col = 0
        self.last_cur_col_update = px.frame_count

        px.run(self.update, self.draw)

    def update(self):
        for key in range(px.KEY_1, px.KEY_9 + 1):
            if px.btnp(key):
                self.cur_col = key - px.KEY_1
        self.img.update(col=self.cur_col)

    def draw(self):
        self.img.draw()
        px.pset(px.mouse_x, px.mouse_y, self.cur_col)


if __name__ == '__main__':
    Editor()
