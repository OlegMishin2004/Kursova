import pygame
import settings
from platforms import MovingPlatform
from platformersprite import SpriteSheet



class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []

    direction = "R"

    level = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        sprite_sheet = SpriteSheet("character.png")
        image = sprite_sheet.get_image(306, 456, 102, 152)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 456, 102, 152)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(102, 456, 102, 152)
        self.walking_frames_r.append(image) 
        image = sprite_sheet.get_image(204, 456, 102, 152)
        self.walking_frames_r.append(image)    



        image = sprite_sheet.get_image(306, 456, 102, 152)   
        image = pygame.transform.flip(image, True, False)  
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 456, 102, 152)   
        image = pygame.transform.flip(image, True, False)  
        self.walking_frames_l.append(image)  
        image = sprite_sheet.get_image(102, 456, 102, 152)   
        image = pygame.transform.flip(image, True, False)  
        self.walking_frames_l.append(image)   
        image = sprite_sheet.get_image(204, 456, 102, 152) 
        image = pygame.transform.flip(image, True, False)  
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]   

        self.rect = self.image.get_rect()

    def update(self):
        self.calc_grav()

        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]   
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame] 


        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) 
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right


        self.rect.y += self.change_y
        
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
    

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
        
        if self.rect.y >= settings.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = settings.SCREEN_HEIGHT - self.rect.height

    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= settings.SCREEN_HEIGHT:
            self.change_y = -10
    
    def go_left(self):
        self.change_x = -6
        self.direction = "L"
    
    def go_right(self):
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        self.change_x = 0
                 


