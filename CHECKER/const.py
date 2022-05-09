import pygame

SCREEN_HEIGTH = 800
SCREEN_WIDTH = 1300

ROWS, COLS = 8, 8

BOARD_SIZE = 800
SQUARE_SIZE = BOARD_SIZE//COLS

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (135,135,135)
GOLD = (255,255,204)
BROWSE = (194, 171, 87)
GREEN = (0,255,0)

START = pygame.image.load('assets/start_button.png')
CROWN = pygame.transform.scale(pygame.image.load("assets/crown_BaW.png"),(40,20))
STUPID_ONICHAN = pygame.image.load("assets/baka.png")