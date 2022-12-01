import os
from pygame import *
from main import *
import block

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [startx, starty]
    def update(self):
        pass
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("skin/p_front.png", startx, starty)
        self.stand_image = self.image
        self.jump_image = pygame.image.load("skin/p_jump.png")
        self.bg = pygame.image.load('skin/bg.png')

        self.walk_cycle = [pygame.image.load(f"skin/p1_walk{i:0>2}.png") for i in range(1,12)]
        self.animation_index = 0
        self.facing_left = False

        self.speed = 5
        self.jumpspeed = 19
        self.vsp = 0
        self.gravity = 1
        self.min_jumpspeed = 5
        self.prev_key = pygame.key.get_pressed()
        self.winner = False
        

    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def jump_animation(self):
        self.image = self.jump_image
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, platforms):
        hsp = 0
        onground = self.check_collision(0, 1, platforms)
        # check hot keys
        key = pygame.key.get_pressed()
        if (key[pygame.K_a] or key[pygame.K_LEFT]): 
            self.facing_left = True
            self.walk_animation()
            hsp = -self.speed
        elif (key[pygame.K_d] or key[pygame.K_RIGHT]):
            self.facing_left = False
            self.walk_animation()
            hsp = self.speed
        else:
            self.image = self.stand_image

        if (key[pygame.K_w] or key[pygame.K_UP]) and onground:
            self.vsp = -self.jumpspeed

        # jumping
        if (self.prev_key[pygame.K_w] or self.prev_key[pygame.K_UP]) and not (key[pygame.K_w] or key[pygame.K_UP]):
            if self.vsp < -self.min_jumpspeed:
                self.vsp = -self.min_jumpspeed

        self.prev_key = key

        # gravity
        if self.vsp < 10 and not onground:  
            self.jump_animation()
            self.vsp += self.gravity

        if onground and self.vsp > 0:
            self.vsp = 0

        # moves
        self.move(hsp, self.vsp, platforms)
                
        
        
    def move(self, x, y, platforms):
        dx = x
        dy = y

        while self.check_collision(0, dy, platforms):
            dy -= numpy.sign(dy)

        while self.check_collision(dx, dy, platforms):
            dx -= numpy.sign(dx)

        self.rect.move_ip([dx, dy])

    def check_collision(self, x, y, grounds):
           
        self.rect.move_ip([x, y])
        collide = pygame.sprite.spritecollideany(self, grounds)
        for p in grounds:
            if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком                
                if isinstance(p, block.Finish):
                    #pygame.quit()
                    self.winner = True # победили!!!                   
        self.rect.move_ip([-x, -y])        
        return collide 