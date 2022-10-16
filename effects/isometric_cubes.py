"""
Put vec.py from https://github.com/kra53n/pyvec to the dir of this file
"""

from math import sin, cos

import pyxel as px

from vec import Vec2


SOURCE_FILE = 'isometric_cubes.pyxres'

CUBE_W = 16
CUBE_H = 17


def load_palette():
    cols = (0x7f85b1, 0x6d5089, 0x492045, 0x713547,
            0xb14b54, 0xf08477, 0xf9a9ab, 0xf9ddab)
    for i, col in enumerate(cols):
        px.colors[i] = col


def run_editor():
    import pyxel.editor
    load_palette()
    pyxel.editor.App(SOURCE_FILE)


class Vec:
    def __init__(self, x: int = 0, y: int = 0, angle: int = 0, ln: int = 0):
        self._x = x
        self._y = y
        self._angle = angle
        self._ln = ln

    def _check_args(self):
        if (self._x or self._y) and (self._angle and self._ln) and self._ln:
            raise Exception('Vec should have x, y or angle, len or len as args')

            
class Cube:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def draw(self):
        px.blt(self.x, self.y, 0, 0, 0, CUBE_W, CUBE_H, 2)


class Ground:
    def __init__(self, x: int = 120, y: int = 100, w: int = 12, h: int = 12):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cubes = []

        self.xvec = Vec2(x=7, y=3)
        self.yvec = self.xvec
        self.yvec += 70 * 2

        self._construct_ground()

    def _construct_ground(self):
        yvec = Vec2()
        for _ in range(self.h):
            xvec = Vec2()
            for _ in range(self.w):
                self.cubes.append(Cube(self.x + int(xvec.x + yvec.x),
                                       self.y + int(xvec.y + yvec.y)))
                xvec += self.xvec
            yvec += self.yvec

    def draw(self):
        for cube in self.cubes:
            cube.draw()


class App:
    def __init__(self):
        px.init(256, 256, title='isometric cubes')
        px.mouse(True)
        load_palette()
        px.load(SOURCE_FILE)

        self.effects = (self.effect_1, self.effect_2, self.effect_3,
                        self.effect_4, self.effect_4, self.effect_5,
                        self.effect_6)
        self.ground = Ground()

        px.run(self.update, self.draw)

    def effect_1(self):
        cubes = self.ground.cubes
        cube = 0
        direction = 1 if cubes[-1].y + CUBE_H < 256 else -350
        for x in range(1, self.ground.w + 1):
            for y in range(1, self.ground.h + 1):
                cubes[cube].y += direction * x*y / 500
                cube += 1

    def effect_2(self):
        cubes = self.ground.cubes
        cube = 0
        direction = 1 if cubes[-1].y > 0 else -650
        for x in range(1, self.ground.w + 1):
            for y in range(1, self.ground.h + 1):
                cubes[cube].y -= direction * x*y / 500
                cube += 1

    def effect_3(self):
        cubes = self.ground.cubes
        cube = 0
        for x in range(1, self.ground.w + 1):
            for y in range(1, self.ground.h + 1):
                cubes[cube].y += sin(x*y)
                cube += 1

    def effect_4(self):
        cubes = self.ground.cubes
        cube = 0
        for x in range(1, self.ground.w + 1):
            for y in range(1, self.ground.h + 1):
                cubes[cube].y += cos(x*y)
                cube += 1

    def effect_5(self):
        cubes = self.ground.cubes
        cube = 0
        for x in range(1, self.ground.w + 1):
            for y in range(1, self.ground.h + 1):
                cubes[cube].y += cos(x) * sin(y)
                cube += 1

    def effect_6(self):
        cubes = self.ground.cubes
        cube = 0
        for x in range(1, self.ground.w + 1):
            for y in range(1, self.ground.h + 1):
                cubes[cube].y += sin(x) * cos(y)
                cube += 1

    def update(self):
        if True:
            self.effects[0]()

    def draw(self):
        px.cls(2)
        self.ground.draw()


if __name__ == '__main__':
    from sys import argv

    if '-e' in argv:
        run_editor()
    App()
