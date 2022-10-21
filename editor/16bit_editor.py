import pyxel as px
import png


SCREEN_W = 16
SCREEN_H = 16
SCREEN_TITLE = '16bit editor'


img = [[0] * SCREEN_W for _ in range(SCREEN_H)]


one_of_btns = lambda *keys: any(map(lambda k: px.btnp(k), keys))
all_of_btns = lambda *keys: all(map(lambda k: px.btnp(k), keys))


def load_palette() -> list:
    return [(h // 256**2, h // 256 % 256, h % 256) for h in px.colors]


class Editor:
    def __init__(self):
        px.init(SCREEN_W, SCREEN_H, title=SCREEN_TITLE)

        self.cur_col = 0
        self.last_cur_col_update = px.frame_count

        px.run(self.update, self.draw)

    def save_img(self):
        filename = f'{(SCREEN_W + SCREEN_H) // 2}_bit editor.png'
        f = open(filename, 'wb')
        w = png.Writer(SCREEN_W, SCREEN_H, palette=load_palette())
        w.write(f, img)
        f.close()

    def update(self):
        for key in range(px.KEY_1, px.KEY_9 + 1):
            if px.btnp(key):
                self.cur_col = key - px.KEY_1

        if px.btn(px.MOUSE_BUTTON_LEFT):
            img[px.mouse_x][px.mouse_y] = self.cur_col

        if px.btnp(px.KEY_C):
            for x in range(SCREEN_W):
                for y in range(SCREEN_H):
                    img[x][y] = self.cur_col

        if px.btnp(px.KEY_S):
            self.save_img()

    def draw_img(self):
        for x, row in enumerate(img):
            for y, _ in enumerate(row):
                px.pset(x, y, img[x][y])

    def draw(self):
        self.draw_img()
        px.pset(px.mouse_x, px.mouse_y, self.cur_col)


if __name__ == '__main__':
    Editor()
