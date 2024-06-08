import pygame
import os

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("resources/imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("resources/imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("resources/imgs", "bird3.png")))
]

BIRD_MAX_ROTATION = 25
BIRD_ROTATION_VELOCITY = 20
BIRD_MAX_HEIGHT_FOT_ROTATION = 50

BIRD_ANIMATION_TIME_1 = 5
BIRD_ANIMATION_TIME_2 = 10
BIRD_ANIMATION_TIME_3 = 15
BIRD_ANIMATION_TIME_4 = 20

BIRD_JUMP_VELOCITY = -10.5
BIRD_MOVE_ACCELERATION = 1.5
BIRD_MAX_DISTANCE = 16
BIRD_NORM_DISTANCE = 2
BIRD_ACC_BASE = 2

BIRD_THRESHOLD_TILT_1 = -90
BIRD_THRESHOLD_TILT_2 = -80