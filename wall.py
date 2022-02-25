import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/Cave-Wall.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1920, 1080))
        self.rect = self.image.get_rect(topleft=pos)
