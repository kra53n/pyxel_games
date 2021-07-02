import pyxel


WINDOW_WIDTH = 150
WINDOW_HEIGHT = 150

WINDOW_BACKGROUND_COLOR = 1
FIELD_COLOR = 11


class TicTacToeEngine:
    def __init__(self, step=1):
        # NOTE: 1 - X; 0 - O
        self.field = [None for i in range(9)]
        self.step = step

    def game_end(self):
        if None not in self.field:
            return True
        return False
    
    def game_win(self):
        if self.field[0] == self.field[1] == self.field[2] or \
           self.field[3] == self.field[4] == self.field[5] or \
           self.field[6] == self.field[7] == self.field[8] or \
           self.field[0] == self.field[3] == self.field[6] or \
           self.field[1] == self.field[4] == self.field[7] or \
           self.field[2] == self.field[8] == self.field[8] or \
           self.field[0] == self.field[4] == self.field[8] or \
           self.field[2] == self.field[4] == self.field[6]:
               return True
        return False


class TicTacToeDraw:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
        pyxel.mouse(True)
        
        self.to_draw = []

        # TODO: delete this
        self.last_pos = None

        pyxel.run(self.update, self.draw)

    def update(self):
        # TODO: delete this
        if self.last_pos != self.help_find_position():
            print(f"x: {pyxel.mouse_x}\ty: {pyxel.mouse_y}")
        self.last_pos = self.help_find_position()

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(WINDOW_BACKGROUND_COLOR)
        self.draw_text_name_of_game()
        self.draw_field(FIELD_COLOR)

        self.to_draw = []

        # TODO: delete this
        #self.draw_tic(57, 18, FIELD_COLOR)
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.spawn_figure()
            #print(self.define_square(pyxel.mouse_x, pyxel.mouse_y))
    
    def draw_text_name_of_game(self):
        pyxel.text(53, 7, "Tic-Tac-Toe", pyxel.frame_count // 3 % 16)

    def draw_field(self, color):
        pyxel.line(56, 18, 56, 132, color)
        pyxel.line(94, 18, 94, 132, color)
        pyxel.line(18, 56, 132, 56, color)
        pyxel.line(18, 94, 132, 94, color)

    def draw_tac(self, x, y, color):
        # tac - X
        pyxel.line(x + 8, y + 8, x + 30, y + 30, color)
        pyxel.line(x + 30, y + 8, x + 8, y + 30, color)

    def draw_tic(self, x, y, color):
        # tic - O
        pyxel.circb(x + 19, y + 19, 15, color)

    # TODO: delete this
    def help_find_position(self):
        #return pyxel.mouse_x, pyxel.mouse_y
        pass

    def spawn_figure(self):
        square = self.define_square(pyxel.mouse_x, pyxel.mouse_y)
        if square != None:
            field_number, x, y = square
            self.draw_tac(x, y, FIELD_COLOR)

    def define_square(self, x, y, x_begin=18, y_begin=18, x_move=38, y_move=38):
        x_pos, y_pos = x_begin, y_begin
        for sq in range(9):
            if (sq % 3 == 0) and (sq != 0):
                x_pos = x_begin
                y_pos += y_move
            if (x > x_pos and x < x_pos + x_move) and (y > y_pos and y < y_pos + y_move):
                return sq, x_pos, y_pos
            x_pos += x_move
        return None


if __name__ == "__main__":
    TicTacToeDraw()
