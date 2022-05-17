import sys
import pygame
from  CHECKER.const import BLACK, WHITE
from CHECKER.const import SCREEN_HEIGTH, SCREEN_WIDTH
from CHECKER.const import SQUARE_SIZE, BOARD_SIZE
from CHECKER.game import Game
from AI.MiniMax import minimax
from AI.AndOrSearch import And_Or_Search

pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pygame.display.set_caption('OUR GAME')

FPS = 60

def exit(run):
    run = False

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

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            # new_board = And_Or_Search(game)
            game.ai_move(new_board)

        if game.winner() != None:
            WINNER = game.winner()
            print(WINNER)
            exit(run)
        
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