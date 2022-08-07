import pyxel as px


class App:
    def __init__(self):
        px.init(256, 256)
        self.circs = [
            # x  y   r   c
            [12, 12, 60, 3],
            [140, 140, 80, 4],
        ]
        self.active = 0

        px.run(self.update, self.draw)

    def update_circs(self):
        circ = self.circs[self.active]
        speed = 3

        if px.btn(px.KEY_A):
            circ[0] -= speed
        if px.btn(px.KEY_D):
            circ[0] += speed
        if px.btn(px.KEY_W):
            circ[1] -= speed
        if px.btn(px.KEY_S):
            circ[1] += speed

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btnp(px.KEY_SPACE) or px.btnp(px.KEY_RETURN):
            self.active = (self.active + 1) % len(self.circs)

        self.update_circs()
        self.collided()

    def collided(self):
        circ1 = self.circs[0]
        circ2 = self.circs[1]

        x = circ2[0] - circ1[0]
        y = circ2[1] - circ1[1]
        r = circ2[2] + circ1[2]
        return x*x + y*y < r*r

    def draw(self):
        px.cls(0)

        for circ in self.circs:
            px.circb(*circ)

        message = 'Collided' if self.collided() else 'Not collided'
        message += '\nWASD to move current circle'
        message += '\nEnter or Space to change circle'
        px.text(0, 0, message, 3)


if __name__ == '__main__':
    App()
