import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/Door.png')
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect(topleft=pos)
