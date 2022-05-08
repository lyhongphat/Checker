# Định nghĩa quân cờ ở đây
import pygame
from .const import WHITE, BLACK, GREY
from .const import CROWN
from .const import SQUARE_SIZE

class Piece():
    PADDING = 15
    OUTLINE = 3
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        # King có thể đi lùi
        # Ta cho có 2 màu quân là trắng và đen
        # Quân bên phía ta là màu đen, 
            # quân đen thì đi lên, nên tọa đồ giảm, suy ra direction = -1
            # ngược lại thì quân trắng đi xuống, nên direction = 1
        if self.color == WHITE:
            self.direction = -1
        elif self.color == BLACK:
            self.direction = 1
        self.x = 0
        self.y = 0
        self.calculate_position()
        
    def calculate_position(self):
        """Tính ra vị trí của quân cờ trên bàn cờ, vị trí của quân cờ nằm giữa ô vuông cờ
        """        
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2
    
    def make_king(self):
        self.king = True
        
    def draw(self, win):
        '''
        Vẽ quân cờ ra màn hình
        Ta vẽ 2 vòng tròn lớn và nhỏ, cùng màu là self.color
        Mỗi vòng trong có 1 vòng tròn có r lớn hơn self.OUTLINE đơn vị màu xám để làm viền
        '''
        largeRadius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), largeRadius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), largeRadius)
        
        smallRadius = largeRadius-7
        pygame.draw.circle(win, GREY, (self.x, self.y), smallRadius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), smallRadius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
        
    def __repr__(self):
        # giá trị trả về của biến
        return(str(self.color))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()