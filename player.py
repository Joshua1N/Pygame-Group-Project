import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__()
        self.image = pygame.image.load(
            'assets/priest3_v1_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0



    def update(self):
        self.get_input()
        self.rect.center += self.direction * self.speed
