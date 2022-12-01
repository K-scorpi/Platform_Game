from main import *
from pygame import *
import os

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
        
class Finish(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        super().__init__("blocks/key_yellow.png", startx, starty)
    
    def update(self):    
        pass
    
class Switch(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        super().__init__("blocks/hill_long.png", startx, starty)

class Box(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))       
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)       
        super().__init__("blocks/crate.png", startx, starty)

class Chest(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))       
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)       
        super().__init__("blocks/box.png", startx, starty)

class Cloud(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))       
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)       
        super().__init__("blocks/cloud_1.png", startx, starty)
        
class Bonus(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))       
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)       
        super().__init__("blocks/bonus.png", startx, starty)        
        
class Dirt(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))       
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)        
        super().__init__("blocks/ground_dirt.png", startx, starty)

class Grass(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))       
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)        
        super().__init__("blocks/ground.png", startx, starty)

class Gc(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)        
        super().__init__("blocks/ground_rock.png", startx, starty)
        
class Gr(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)       
        super().__init__("blocks/ground_cave.png", startx, starty)
        
class Plank(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)        
        super().__init__("blocks/plank.png", startx, starty)
        
class Gelik(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)        
        super().__init__("blocks/cloud_2.png", startx, starty)
        
class Chai(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))        
        super().__init__("blocks/chai.png", startx, starty)        

class Gelik(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))  
        super().__init__("blocks/g63.png", startx, starty)

class Sand(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)       
        super().__init__("blocks/ground_sand.png", startx, starty)

class Bridge(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(startx, starty, PLATFORM_WIDTH, PLATFORM_HEIGHT)       
        super().__init__("blocks/bridge.png", startx, starty)

class Water(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))  
        super().__init__("blocks/water.png", startx, starty)
        
class G(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))  
        super().__init__("blocks/grass.png", startx, starty)
        
class M(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))  
        super().__init__("blocks/shroom.png", startx, starty)
        
class Bush(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))  
        super().__init__("blocks/bush.png", startx, starty) 
 
class Fence(Sprite):
    def __init__(self, startx, starty):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))  
        super().__init__("blocks/fence.png", startx, starty)        