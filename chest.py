import pygame


class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/2D Pixel Dungeon Asset Pack/items and trap_animation/box_1/box_1_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=pos)
