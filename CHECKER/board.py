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
        self.white_king = self.black_king = 0
        self.white_score = self.black_score = 0
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
        self.addLabel(win, 'White scores: ' + str(self.white_score), 25, 900, 250, bold=True)
        self.addLabel(win, 'White kings: ' + str(self.white_king), 25, 900, 300, bold=True, color=BROWSE)
        self.addLabel(win, 'Black scores: ' + str(self.black_score), 25, 900, 450, bold=True)
        self.addLabel(win, 'Black kings: ' + str(self.black_king), 25, 900, 500, bold=True, color=BROWSE)
                
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
                    piece.draw(win)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS or col == COLS:
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