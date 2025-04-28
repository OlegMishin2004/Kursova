import pygame

import settings

import platforms

class Level():
    platform_list = None
    enemy_list = None
    background = None
    world_shift = 0
    level_limit = -1000


    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        screen.fill(settings.BLUE)
        screen.blit(self.background, (self.world_shift // 3,0))
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        self.background = pygame.image.load("background_03.png").convert()
        self.background.set_colorkey(settings.WHITE)
        self.level_limit = -2500

        level = [ [platforms.STONE_LEFT,700, 500],
                  [platforms.STONE_MIDDLE, 770, 500],
                  [platforms.STONE_RIGHT, 840, 500],
                  [platforms.STONE_LEFT, 1000, 400],
                  [platforms.STONE_MIDDLE, 1070, 400],
                  [platforms.STONE_RIGHT, 1140, 400],
                  [platforms.STONE_LEFT, 1200, 300],
                  [platforms.STONE_MIDDLE, 1270, 300],
                  [platforms.STONE_RIGHT, 1340, 300],
                  [platforms.SNOW_LEFT, 1320, 180],
                  [platforms.SNOW_MIDDLE, 1390, 180],
                  [platforms.SNOW_RIGHT, 1460, 180],
                ]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.SNOW_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_02(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        self.background = pygame.image.load("background_04.png").convert()
        self.background.set_colorkey(settings.WHITE)
        self.level_limit = -1000
     
        level = [ [platforms.STONE_LEFT,500, 550],
                  [platforms.STONE_MIDDLE, 570, 550],
                  [platforms.STONE_RIGHT, 640, 550],
                  [platforms.STONE_LEFT, 750, 480],
                  [platforms.STONE_MIDDLE, 820, 480],
                  [platforms.STONE_RIGHT, 890, 480],
                  [platforms.STONE_LEFT, 1050, 380],
                  [platforms.STONE_MIDDLE, 1120, 380],
                  [platforms.STONE_RIGHT, 1190, 380],
                  [platforms.STONE_LEFT, 1300, 500],
                  [platforms.STONE_MIDDLE, 1370, 500],
                  [platforms.STONE_RIGHT, 1440, 500],
                  [platforms.SNOW_LEFT, 1500, 350],
                  [platforms.SNOW_MIDDLE, 1570, 350],
                  [platforms.SNOW_RIGHT, 1640, 350],
                  [platforms.SNOW_LEFT, 1700, 200],
                  [platforms.SNOW_MIDDLE, 1770, 200],
                  [platforms.SNOW_RIGHT, 1840, 200],
                ]   
     
        
        
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
             
    