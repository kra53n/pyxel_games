import pyxel
from screen_resolution import get_monitor_resolution

from elements import Stick
from elements import Ball


SCREEN_WIDTH, SCREEN_HEIGHT = [i // 10 for i in get_monitor_resolution()]
SCREEN_CAPTION = "PyxelPingPong | PPP"
SCREEN_SCALE = 1
SCREEN_FPS = 60

STICK_WIDTH = 2
STICK_HEIGHT = 30
STICK_MARGIN = 3
STICK_MOVE_STEP = 1

BALL_RADIUS = 1
BALL_SPEED = 0.5

COLOR_STICK_PLAYER = 8
COLOR_STICK_ENEMY = 8
COLOR_BALL = 7

KEY_START = pyxel.KEY_ENTER


class App:
    def __init__(self):
        pyxel.init(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            caption=SCREEN_CAPTION,
            scale=SCREEN_SCALE,
            fps=SCREEN_FPS,
            quit_key=pyxel.KEY_Q,
            fullscreen=True,
        )

        self.stick_player = Stick(
            x=STICK_MARGIN,
            y=(SCREEN_HEIGHT - STICK_HEIGHT) // 2,
            w=STICK_WIDTH,
            h=STICK_HEIGHT,
            col=COLOR_STICK_PLAYER,
            move_step=STICK_MOVE_STEP,
            screen_h=SCREEN_HEIGHT,
            screen_w=SCREEN_WIDTH,
        )
        
        self.ball = Ball(
            x=SCREEN_WIDTH // 2,
            y=SCREEN_HEIGHT // 2,
            r=BALL_RADIUS,
            col=COLOR_BALL,
            move_step=BALL_SPEED,
            screen_h=SCREEN_HEIGHT,
            screen_w=SCREEN_WIDTH,
        )

        pyxel.run(self.update, self.draw)
    
    def update(self):
        pass

    def draw(self):
        pyxel.cls(1)
        self.stick_player.draw()
        self.ball.draw()

        self.move_stick()
        self.change_ball_direction()

    def move_stick(self):
        if pyxel.btn(pyxel.KEY_W):
            self.stick_player.up()
        if pyxel.btn(pyxel.KEY_S):
            self.stick_player.down()

    def change_ball_direction(self):
        if (self.ball.x <= STICK_MARGIN + STICK_WIDTH + BALL_RADIUS) and \
           ((self.stick_player.begin < self.ball.y + BALL_RADIUS) and \
           (self.stick_player.end > self.ball.y - BALL_RADIUS)):
            self.ball.change_x_direction()


if __name__ == "__main__":
    App()
