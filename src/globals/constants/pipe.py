import pygame
import os

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("resources/imgs", "pipe.png")))

PIPE_GAP = 200
PIPE_VELOCITY = 5

PIPE_HEIGHT_MIN = 50
PIPE_HEIGHT_MAX = 450