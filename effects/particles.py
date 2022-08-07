from math import atan2, sin, cos, pi, sqrt
from random import random, choice

import pyxel as px


WIN_WDT = 120
WIN_HGT = 120

BG_COL = 1
PARTICLE_COL = 8

DEBUG = True


class V2:
    _radian: float = pi / 180

    def __init__(self, *coords):
        if (len_coords := len(coords)) != 4:
            raise Exception(f'Should be pass 4 coords: x1, y1, x2, y2, but {len_coords} was given')
        self._coords = list(coords)

    @property
    def angle(self):
        return atan2(self._coords[3], self._coords[2])

    def get_random_point(self) -> tuple:
        normal = self.normal
        angle = self.angle
        return self._coords[0] + cos(angle) * random() * normal, \
               self._coords[1] + sin(angle) * random() * normal

    @property
    def normal(self):
        return sqrt(self._coords[2]**2 + self._coords[3]**2)

    def __getitem__(self, key):
        sign = -1 if key == 3 else 1
        return sign * self._coords[key]

    def __add__(self, angle):
        """angle - rotate vector on appropriate degrees in right"""
        angle = self.angle + angle * V2._radian
        normal = self.normal
        self._coords[2] = cos(angle) * normal
        self._coords[3] = sin(angle) * normal

    def __sub__(self, angle):
        """angle - rotate vector on appropriate degrees in right"""
        angle = self.angle - angle * V2._radian
        normal = self.normal
        self._coords[2] = cos(angle) * normal
        self._coords[3] = sin(angle) * normal


class Particles:
    def __init__(self):
        self.x = WIN_WDT // 2
        self.y = WIN_HGT // 4
        self.size = 2
        self.speed = 3

        self.particles = []

    def delete(self):
        if len(self.particles):
            self.particles.pop(0)

    def update(self):
        for particle in self.particles:
            if len(particle) != 5:
                angle = atan2(particle[1] - particle[3], particle[2] - particle[0])
                particle.append(angle)
            particle[0] += cos(particle[4]) * self.speed
            particle[1] += sin(particle[4]) * self.speed

    def draw(self):
        for particle in self.particles:
            px.rect(particle[0], particle[1], self.size, self.size, PARTICLE_COL)


def update(particles: Particles, vecs):
    particles.update()

    rotation = 15

    if px.btn(px.KEY_D):
        for vec in vecs:
            vec += rotation

    if px.btn(px.KEY_A):
        for vec in vecs:
            vec -= rotation

    if (px.btn(px.KEY_UP) or px.btn(px.KEY_W)) and px.frame_count % 3 == 0:
        line: V2 = choice(vecs[1:])
        particles.particles.append([*line.get_random_point(), vecs[0][0] + vecs[0][2], vecs[0][1] - vecs[0][3]])

    if px.frame_count % 4 == 0:
        particles.delete()


def draw(particles: Particles, vecs):
    particles.draw()

    if DEBUG:
        for vec in vecs:
            px.line(vec[0], vec[1], vec[0] + vec[2], vec[1] + vec[3], PARTICLE_COL)


def main():
    particles = Particles()
    vecs = V2(64, 64, 0, -20), V2(64, 64, 20, 0), V2(64, 64, -20, 0)
    args = (particles, vecs)

    while True:
        px.cls(BG_COL)
        px.text(0, 0, 'Press W or Up Arrow', PARTICLE_COL)

        update(*args)
        draw(*args)

        px.flip()


if __name__ == '__main__':
    px.init(WIN_WDT, WIN_HGT, title='Particles effect')
    main()
