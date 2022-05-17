import pygame
from .const import WHITE, BLACK, GREEN
from .const import SQUARE_SIZE
from .board import Board
from copy import deepcopy

def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)

class Game():
    def __init__(self, win):
        self._init()
        self.win = win
        self.initial = self.board

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

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()