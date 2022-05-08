import sys
import pygame
from CHECKER.const import SCREEN_HEIGTH, SCREEN_WIDTH
from CHECKER.const import SQUARE_SIZE
from CHECKER.board import Board

pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pygame.display.set_caption('CỜ ĐAM')

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    
    while run:
        clock.tick(FPS)
        board.draw_board(WIN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    # thao tác chuột ở đây
                pass
        
        pygame.display.update()
        
    pygame.quit()
    sys.exit()
    
main()