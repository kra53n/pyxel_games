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
        filename = '16bit editor.png'
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


class Color:
    def __init__(self):
        self._col = 0
        self._cols = [self._col]
        self._last_kbd_input = px.frame_count
        self._delay = 8

    def _get_key(self):
        for key in range(px.KEY_0, px.KEY_9 + 1):
            if px.btnp(key):
                return key
        return

    def _set_col(self, key):
        frames = px.frame_count

        self._cols.append(key - px.KEY_0)

        if frames - self._last_kbd_input <= self._delay:
            if len(self._cols) > 1:
                self._col = self._cols.pop() + self._cols.pop() * 10
                if self._col > 15:
                    self._col //= 10
        else:
            if len(self._cols):
                self._col = self._cols[-1]
            self._last_kbd_input = frames
            self._cols = self._cols[-2:]

    def get_col(self):
        return self._col

    def update(self):
        key = self._get_key()
        if not key:
            return
        self._set_col(key)


class Editor:
    def __init__(self):
        px.init(SCREEN_W, SCREEN_H, title=SCREEN_TITLE)

        self.img = Image()
        self.col = Color()

        px.run(self.update, self.draw)

    def update(self):
        self.col.update()
        self.img.update(col=self.col.get_col())

    def draw(self):
        self.img.draw()
        px.pset(px.mouse_x, px.mouse_y, self.col.get_col())


if __name__ == '__main__':
    Editor()
