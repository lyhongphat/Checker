# Tạo bàn cờ ở đây
import pygame
from .const import WHITE, BLACK, BROWSE, GOLD
from .const import ROWS, COLS
from .const import BOARD_SIZE, SQUARE_SIZE
from .piece import Piece

class Board():
    def __init__(self):
        self.board = []
        self.white = self.black = 12
        self.white_score = self.black_score = 0
        self.white_king = self.black_king = 0
        self.create_board()
        
    def addLabel(self, WIN, text, size, x, y, bold = False, italic = False, color = WHITE):
        """_summary_
        Args:
            WIN (window): màn hình để in label
            text (string): Label được hiển thị ra màn hình
            size (int): kích thước label
            x (int): Tọa độ xuất hiện theo chiều ngang
            y (int): Tọa độ xuất hiện theo chiều dọc
            bold (bool, optional): In đậm hay không. Mặc định là không.
            italic (bool, optional): In nghiêng hay không. Mặc định là không
            color (tuple of color from CHECKER.const, optional): Màu của Label. Mặc định là màu trắng
        """    
        myfont = pygame.font.SysFont(name = "Console", size = size, bold = bold, italic = italic)
        thisLabel = myfont.render(text, True, color)
        WIN.blit(thisLabel, (x, y))
        
    def draw_board(self, win):
        """
        Vẽ bàn cờ trắng đen và vài thứ khác lên màn hình
        Args:
            win (_type_): màn hình được chọn để in trong pygame
        """        
        win.fill(BLACK)
        pygame.draw.rect(win, GOLD, (0, 0, BOARD_SIZE, BOARD_SIZE))
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BROWSE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        self.addLabel(win, 'CHECKER GAME', 50, 880, 50, bold=True)
                
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (col % 2) == ((row + 1) % 2):
                    # Hàng chẵn thì điền ở cột lẻ, hàng lẻ thì điền ở cột chẵn
                    if row <= 2:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row >= 5:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    self.calc_score()
                    piece.draw(win)
        self.addLabel(win, 'White score: ' + str(self.white_score), 25, 900, 250, bold=True)
        self.addLabel(win, 'White kings: ' + str(self.white_king), 25, 900, 300, bold=True, color=BROWSE)
        self.addLabel(win, 'Black score: ' + str(self.black_score), 25, 900, 450, bold=True)
        self.addLabel(win, 'Black king: ' + str(self.black_king), 25, 900, 500, bold=True, color=BROWSE)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_king += 1
            elif piece.color == BLACK:
                self.black_king += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def winner(self):
        if self.black <= 0:
            return BLACK
        elif self.white <= 0:
            return WHITE
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # Ta cho có 2 màu quân là trắng và đen
        # Quân bên phía ta là màu đen,
        # quân đen thì đi lên, nên tọa đồ giảm
        # ngược lại thì quân trắng đi xuống
        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    if piece.king:
                        self.white_king -= 1
                    self.white -= 1
                else:
                    if piece.king:
                        self.black_king -= 1
                    self.black -= 1

    def calc_score(self):
        self.white_score = self.white - self.black
        self.black_score = self.black - self.white
        return self.black_score