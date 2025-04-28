import pygame
from platformersprite import SpriteSheet

STONE_LEFT = (145, 432, 70, 72)
STONE_MIDDLE = (70, 432, 70, 72)
STONE_RIGHT = (141, 288, 70, 72)
SNOW_LEFT = (290, 0, 70, 70)
SNOW_MIDDLE = (140, 792, 70, 70)
SNOW_RIGHT = (210, 792, 70, 70)


class Platform(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("tiles.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None


    def update(self):
        self.rect.x += self.change_x

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right
        
        self.rect.y += self.change_y

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
        
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1