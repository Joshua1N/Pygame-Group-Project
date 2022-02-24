import pygame, sys
from random import randint
from chest import Chest
from player import Player
from camera import CameraGroup
from door import Door


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

# Setup
camera_group = CameraGroup()
Player((640, 360), camera_group)
Door((100, 100), camera_group)

# Variables
bg = pygame.image.load('assets/Cave-Wall.png').convert_alpha()
bg = pygame.transform.scale(bg, (1920, 1080))

for i in range(20):
    random_x = randint(0, 1000)
    random_y = randint(0, 1000)
    Chest((random_x, random_y), camera_group)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0, 0))

    camera_group.update()
    camera_group.custom_draw()

    pygame.display.update()
