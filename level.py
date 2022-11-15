import pygame
from tiles import Tile
from settings import tile_size, width
from player import Player

class Level:
    def __init__(self, level_data,surface):
        self.display_surface = surface
        self.setup(level_data)
        self.world_shift = 0
    
    def setup(self, layout):
        self.tiles= pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_i, row in enumerate(layout):
            for col_i, col in enumerate(row):
                x = col_i * tile_size
                y = row_i * tile_size
                if col == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    player_s= Player((x,y))
                    self.player.add(player_s)

    def scroll_x(self):
        player= self.player.sprite
        palyerx = player.rect.centerx
        directionx = player.directon.x

        if palyerx < width/4 and directionx < 0:
            self.world_shift = 8
            player.speed = 0
        elif palyerx > width - (width/4) and directionx >0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collison(self):
        player = self.player.sprite
        player.rect.x += player.directon.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.directon.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.directon.x > 0:
                    player.rect.right = sprite.rect.left
    
    def vertical_movement_collison(self):
        player = self.player.sprite
        player.ApplyGravitiy()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.directon.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.directon.y = 0
                elif player.directon.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.directon.y = 0
                
    def run(self):
        #map
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        #player
        self.player.update()
        self.horizontal_movement_collison()
        self.vertical_movement_collison()
        self.player.draw(self.display_surface)