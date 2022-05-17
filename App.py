import sys
import pygame
from CHECKER.const import SCREEN_HEIGTH, SCREEN_WIDTH
from CHECKER.const import SQUARE_SIZE, BOARD_SIZE
from CHECKER.game import Game

pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pygame.display.set_caption('OUR GAME')

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] < BOARD_SIZE and pos[1] < BOARD_SIZE:
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)

        game.update()

    pygame.quit()
    sys.exit()
    
main()