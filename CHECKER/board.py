# Tạo bàn cờ ở đây
import pygame
from .const import WHITE, BLACK, BROWSE, GOLD
from .const import ROWS, COLS
from .const import BOARD_SIZE, SQUARE_SIZE

class Board():
    def __init__(self):
        self.board = []
        self.selected = None
        self.white = self.black = 12
        self.white_king = self.black_king = 0
        
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
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BROWSE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        self.addLabel(win, 'CHECKER GAME', 50, 880, 50, bold=True)
                
    def create_board(self):
        pass