import pygame
import os

WIN_WIDTH = 500
WIN_HEIGHT = 800

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("resources/imgs", "bg.png")))

font_inited = False
if not font_inited:
    pygame.font.init()
    font_inited = True

SCORE_MSG = "Score: "
GEN_MSG = "Gen: "
STAT_FONT = pygame.font.SysFont("comicsans", 50) 
STAT_FONT_COLOR = (255, 255, 255)
STAT_WIDTH_NORM = 10
STAT_HEIGHT = 10
GEN_MSG_X = 10
GEN_MSG_Y = 10

CLOCK_DEFAULT_TICK = 30

BIRD_DEFAULT_X = 230
BIRD_DEFAULT_Y = 350
BASE_DEFAULT_Y = 730
PIPE_DEFAULT_X = 600

BIRD_BASE_COLLIDE_HEIGHT = 730