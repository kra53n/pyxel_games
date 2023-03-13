import pyxel as px


KEYS = tuple(k for k in dir(px) if sum(map(lambda s: s in k, ('KEY', 'MOUSE', 'GAMEPAD'))))


class App:
    def __init__(self):
        px.init(128, 20, title='whatkey')
        px.run(lambda: None, self.draw)

    def draw(self):
        for k in KEYS:
            if px.btn(eval(f'px.{k}')):
                px.cls(0)
                px.text(0, 0, k, 7)


if __name__ == '__main__':
    App()
