import pygame
from .const import WHITE, BLACK
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
        self.turn = WHITE
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        pass

    def move(self, row, col):
        pass