if __name__ == '__main__':
import random

class Board:
    FREE_CELL = 99
    BOARD_SIZE = 10
    SHEAP = 33
    def __init__(self):
        self.shoots = set()
        self.board = {}
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                self.board[(i,j)] = self.FREE_CELL
        print(self.board)

    def fill_boats(self):
        self.set_place(self.ger_sheap_place(4), '4')
        self.set_place(self.ger_sheap_place(2), '1')
        self.set_place(self.ger_sheap_place(3), '4')
        self.set_place(self.ger_sheap_place(1), '2')
        self.set_place(self.ger_sheap_place(1), '4')
        self.set_place(self.ger_sheap_place(2), '1')
        self.set_place(self.ger_sheap_place(1), '2')
        self.set_place(self.ger_sheap_place(3), '3')
        self.set_place(self.ger_sheap_place(2), '1')
        self.set_place(self.ger_sheap_place(4), '2')

    def set_place(self, coords, symbol):
        for coord in coords:
            self.board[coord] = symbol

    def ger_sheap_place(self, boat_size):
        while True:
            i1 = random.randint(0, self.BOARD_SIZE - 1)
            j1 = random.randint(0, self.BOARD_SIZE - 1)
            if self.board[(i1, j1)] != self.FREE_CELL:
                continue
            direction = random.randint(0, 1)
            # 0 = x
            # 1 = y
            sheap_coord = []
            for i in boat_size():
                check_coord = (i1, j1 + i) if direction == 0 else (i1 +i, ji)
                if self.can_set(*check_coord):
                    sheap_coord.append(check_coord)

            if len(sheap_coord) == boat_size:
                return sheap_coord

    def in_board(self, x, y):
        return 0 <= x < self.BOARD_SIZE and 0 <= y < self.BOARD_SIZE

    def can_set(self, x , y):
        if self.board[(x, y)] != self.FREE_CELL:
            return False
        delta = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]
        for xd, yd in delta:
            if not (not self.in_board(x+xd, y +yd)) or (self.in_board(x +xd, y+yd)) and  self.board[(x+xd, y+yd)] == self.FREE_CELL:
                return False
        return True

    def display_board(self):
        for i in range(self.BOARD_SIZE):
            print()
            for j in range(self.BOARD_SIZE):
                if self.board[(i, j)] == self.FREE_CELL:
                    print('#', end='')
                else:
                    print(self.board[(i, j)], end='')

    def miss_check(self, coords):
        if coords in self.board:
            if self.board[coords] == self.FREE_CELL and self.board[coords] != '$':
                self.board[coords] = '$'
                return True
            return False

    def random_coords(self):
        coords = random.choice(self.board.keys)
        if coords not in self.shoots:
            self.shoots.add(coords)

b_1 = Board()
b_2 = Board()
b_1.fill_boats()
b_2.fill_boats()

b_1.display_board()
print('\n' + '-'*100)
b_2.display_board()

