import pyxel
from screen_resolution import get_monitor_resolution

from elements import Stick, StickEnemy, Ball, Score, GameStatus


SCREEN_WIDTH, SCREEN_HEIGHT = [i // 10 for i in get_monitor_resolution()]
SCREEN_CAPTION = "PyxelPingPong | PPP"
SCREEN_FPS = 60

STICK_WIDTH = 2
STICK_HEIGHT = 30
STICK_MARGIN = 3
STICK_MOVE_STEP = 1

BALL_RADIUS = 1
BALL_SPEED = 0.8

COLOR_STICK_PLAYER = 8
COLOR_STICK_ENEMY = 8
COLOR_BALL = 7

KEY_START = pyxel.KEY_RETURN


class App:
    def __init__(self):
        pyxel.init(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title=SCREEN_CAPTION,
            fps=SCREEN_FPS,
            quit_key=pyxel.KEY_Q,
        )
        pyxel.fullscreen(True)

        pyxel.load("assets/my_resource.pyxres", sound=True)
        pyxel.playm(0, loop=True)

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

        self.stick_enemy = StickEnemy(
            x=SCREEN_WIDTH - STICK_MARGIN - STICK_WIDTH,
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

        self.score = Score(
            screen_h=SCREEN_HEIGHT,
            screen_w=SCREEN_WIDTH,
            col=8,
        )

        self.game = GameStatus(
            screen_h=SCREEN_HEIGHT,
            screen_w=SCREEN_WIDTH,
        )

        self.run = False

        pyxel.run(self.update, self.draw)
    
    def update(self):
       self.game_reload()

    def draw(self):
        pyxel.cls(1)
        self.stick_player.draw()
        self.stick_enemy.draw(self.ball.x, self.ball.y, self.ball.move_x)
        self.score.draw()

        self.ball.draw(self.run)
        self.move_stick()

        self.change_ball_direction()

    def move_stick(self):
        if pyxel.btn(pyxel.KEY_W):
            self.stick_player.up(self.run)
        if pyxel.btn(pyxel.KEY_S):
            self.stick_player.down(self.run)

    def change_ball_direction(self):
        if (
            # player stick rebound
            (self.ball.x - BALL_RADIUS <= self.stick_player.right_side
            and (self.stick_player.begin < self.ball.y + BALL_RADIUS
                 and self.stick_player.end > self.ball.y - BALL_RADIUS))
            # enemy stick rebound
            or (self.ball.x + (BALL_RADIUS * 2) >= self.stick_enemy.left_side
            and (self.stick_enemy.begin < self.ball.y + BALL_RADIUS
                 and self.stick_enemy.end > self.ball.y - BALL_RADIUS))
        ):
            self.ball.change_x_direction()
            self.ball.increase_speed()

        # player scored
        scored = 'player' if SCREEN_WIDTH <= self.ball.x + (BALL_RADIUS * 2) else ''
        scored = 'enemy' if 0 >= self.ball.x - BALL_RADIUS else scored
        if scored:
            pyxel.play(1, 2 if 'player' else 1)
            self.ball.change_x_direction()
            exec(f'self.score.{scored} += 1')
            self.ball.return_to_center()
            self.ball.give_normal_speed()
            self.run = False

        # rebound from top
        if (
            self.ball.y - BALL_RADIUS <= 0
            or self.ball.y + BALL_RADIUS >= SCREEN_HEIGHT
        ):
            self.ball.change_y_direction()
            self.ball.increase_speed()

    def game_reload(self):
        if pyxel.btnp(pyxel.KEY_SPACE) or self.run:
            self.run = True

            
if __name__ == "__main__":
    App()
