import pygame, sys
from rooms.map_one import *
from level import Level
from camera import CameraGroup

pygame.init()
vec = pygame.math.Vector2


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.level = Level(level_map, self.screen)
        self.running = True
        self.state = 'playing'

        self.load()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.screen = pygame.display.set_mode((screen_width, screen_height))
                # Camera
                self.camera_group.update()
                self.camera_group.custom_draw()
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'help':
                # How to play page here
                pass
            else:
                self.running = False
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    ############### HELPER FUNCTIONS ###############

    def draw_text(self, words, screen, pos, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0] / 2
        pos[1] = pos[1] - text_size[1] / 2
        screen.blit(text, pos)

    def load(self):
        '''self.background = pygame.image.load('assets/BACKGROUND.jpg').convert_alpha()
        self.background = pygame.transform.scale(self.background, (1920, 1080)).convert_alpha()
        self.start_button = pygame.image.load('assets/start.png').convert_alpha()
        self.start_button_rect = self.start_button.get_rect(topleft=(680, 400))
        self.start_button = pygame.transform.scale(self.start_button, (400, 75)).convert_alpha()
        self.exit_button = pygame.image.load('assets/quit.png').convert_alpha()
        self.exit_button = pygame.transform.scale(self.exit_button, (400, 75)).convert_alpha()
        self.exit_button_rect = self.exit_button.get_rect(topleft=(680, 600))'''
        '''self.howtoplay_button = pygame.image.load('assets/information.png').convert_alpha()
        self.howtoplay_button = pygame.transform.scale(self.howtoplay_button, (500, 100)).convert_alpha()
        self.howtoplay_button_rect = self.howtoplay_button.get_rect(center=(650, 800))'''
        pass

    ############### INTRO FUNCTIONS ###############

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                '''if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'playing'
                # elif self.howtoplay_button_rect.collidepoint(pygame.mouse.get_pos()):
                    # self.state = 'help'
                if self.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()'''

    def start_update(self):
        pass

    def start_draw(self):
        '''self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.start_button, (680, 400))
        self.screen.blit(self.exit_button, (680, 600))'''
        # self.screen.blit(self.howtoplay_button, (650, 800))

        pass

    ############### PLAYING FUNCTIONS ###############

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Events while Playing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'start'

    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.fill('light blue')
        self.level.run()
        pygame.display.update()
