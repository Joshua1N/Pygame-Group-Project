import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/Stone-Block.png')
        #self.image.fill('white')
        self.rect = self.image.get_rect(topleft=pos)
