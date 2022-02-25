import pygame
from tiles import Tile
from rooms.map_one import tile_size


class Level:
    def __init__(self, level_data, surface):
        # Level Setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        # self.chests = pygame.sprite.Group()
        # self.camera_group = CameraGroup()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size, self.camera_group)
                    self.tiles.add(tile)

    def run(self):
        # Level Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()
        self.player.draw(self.display_surface)


''' # Chests
self.chests.update()
self.chests.draw(self.display_surface)'''
