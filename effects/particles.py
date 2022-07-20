from random import randint, random
from math import atan2, sin, cos
import pyxel as px


WIN_WDT = 120
WIN_HGT = 120

BG_COL = 1
PARTICLE_COL = 8

DEBUG = False


class Particles:
    def __init__(self):
        self.x = WIN_WDT // 2
        self.y = WIN_HGT // 4
        self.size = 2
        self.rng_x = 24
        self.rng_y = 48
        self.w = 3
        self.h = 3
        self.speed = 3

        self._queue = []

    def add(self):
        x = randint(self.x - self.rng_x, self.x + self.rng_x)
        coords = [x, self.y]
        self._queue.append(coords)

    def delete(self):
        if len(self._queue):
            self._queue.pop(0)

    def update(self):
        for particle in self._queue:
            angle = atan2(self.y + self.rng_y, particle[0]) + random() / 1.4
            direction = -1 if self.x < particle[0] else 1
            particle[0] += direction * cos(angle) * self.speed
            particle[1] += sin(angle) * self.speed

            rng = 3
            if self.x - rng < particle[0] < self.x + rng:
                self._queue.pop(self._queue.index(particle))
    
    def draw(self):
        if DEBUG:
            px.line(self.x - self.rng_x, self.y, self.x + self.rng_x, self.y, PARTICLE_COL)
            px.line(self.x, self.y, self.x, self.y + self.rng_y, PARTICLE_COL)

        for particle in self._queue:
           px.rect(*particle, self.size, self.size, PARTICLE_COL)


def update(particles: Particles):
    particles.update()

    if (px.btn(px.KEY_UP) or px.btn(px.KEY_W)) and px.frame_count % 3 == 0:
        particles.add()

    if px.frame_count % 10 == 0:
        particles.delete()


def draw(particles: Particles):
    particles.draw()


def main():
    particles = Particles()
    args = (particles, )

    while True:
        px.cls(BG_COL)
        px.text(0, 0, 'Press W or Up Arrow', PARTICLE_COL)

        update(*args)
        draw(*args)

        px.flip()


if __name__ == '__main__':
    px.init(WIN_WDT, WIN_HGT, title='Particles effect')
    main()
