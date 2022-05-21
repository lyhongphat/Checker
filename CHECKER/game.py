import pygame

from .const import WHITE, BLACK, GREEN
from .const import SQUARE_SIZE
from .board import Board
from .board import addLabel
from AI.Algorithm import get_all_moves

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

        addLabel(self.win, 'CHECKER GAME', 50, 880, 50, bold=True)
        pygame.draw.rect(self.win, GREEN, (800, 650, 500, 500))

        addLabel(self.win, 'Turn: ', 50, 850, 700, bold=True, italic=True)
        if self.turn == WHITE:
            pygame.draw.rect(self.win, WHITE, (1000, 705, 200, 50))
        elif self.turn == BLACK:
            pygame.draw.rect(self.win, BLACK, (1000, 705, 200, 50))

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
            pygame.draw.circle(self.win,
                               GREEN,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                row * SQUARE_SIZE + SQUARE_SIZE // 2),
                               15)

    def winner(self):
        '''
        Bên cạnh trường hợp ăn hết quân để thắng
        thì ta còn 1 trường hợp nữa là hết đường đi
        mặc dù khâu tính toán chậm hơn
        :return:
        '''
        if not which_valid_move(self.board, WHITE):
            return BLACK
        elif not which_valid_move(self.board, BLACK):
            return WHITE
        return None

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()

def which_valid_move(thisBoard, color):
    moves = []
    for piece in thisBoard.get_all_pieces(color):
        valid_moves = thisBoard.get_valid_moves(piece)
        moves.append(valid_moves)
    return moves