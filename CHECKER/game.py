import pygame
from .const import WHITE, BLACK, GREEN
from .const import SQUARE_SIZE
from .board import Board

class Game():
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        """
        Hàm khởi tạo lại game từ đầu
        mình phải tạo thêm 1 hàm _init private để có tính bảo mật
        tránh sự tác động của người dùng lên ứng dụng
        :return:
        """
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        """
        Chọn 1 quân cờ nào đó
        Nếu chọn được thì trả về True và ngược lại
        """

        if self.selected:
            '''Nếu đã chọn 1 quân cờ nào đó rồi 
            thì đây là chọn nước vị trí mới
            cho quân cờ đó'''
            result = self._move(row, col)
            if not result:
                '''
                Nếu di chuyển được thì...
                '''
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and ((row, col) in self.valid_moves):
            '''
            Nếu đã chọn 1 quân để di chuyển rồi
            và vị trí chọn (row, col) là trống
            và vị trí chọn (row, col) nằm trong bước đi cho phép
            
            thì cho phép di chuyển
            '''
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def winner(self):
        return self.board.winner()