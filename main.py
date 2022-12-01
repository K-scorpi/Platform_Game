import pygame, numpy, sys
from pygame import *
from block import *
from player import *


WIDTH = 1400
HEIGHT = 800
PLATFORM_WIDTH = 70
PLATFORM_HEIGHT = 70
BD_COLOR = "#FFEBCD" #000000   F0E68C  F0E68C

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
                
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIDTH / 2, -t+HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    #l = max(-(camera.width-WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы
            
    return Rect(l, t, w, h)

def main():
    pygame.init()
    
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen = pygame.display.set_mode()#для полного экрана удалить
    pygame.display.set_caption("Battle_Luric_3")
    bg = Surface((1920, 1080))
    clock = pygame.time.Clock()
    bg.fill(Color(BD_COLOR))

    player = Player(250, 1150)
    left = right = False
    up = False

    entities = pygame.sprite.Group()
    platforms = []
    entities.add(player)
    
    level = [
       "                                                                                        ",
	   "                                                                                        ",
	   "                                                                                        ",
	   "                                                                            p           ",
	   "                                                                     c  c   c           ",
       "           g   y   g                                              c                     ",
       "                    p                                          c                        ",
       "          ,,,,,,,,,,,                                       c                           ",
       "      -                               z                  c                              ",
       "     _+-                                   _         c                                  ",
       "   --   - -   ------------- c  c   c             c                                      ",
       "           --                             v   c                                         ",
       "                                      v                                                 ",
	   "                                 v                                                      ",
	   "                                    v   _                                               ",
       "                                                                       `  `             ",
       "                                      _z                             v......            ",
       "  h   m     u                       _                               v                   ",
       ".......   ....     m      m        zzz         m        u ffff     z   p                ",
       "-------        ////////////////   zzzzz       ssssbbbbssss-........         m    h      ",
       "-------                   ,,,,,,,,,    _  _       wwww              ///////////////     "]
    for i in range(len(level)):
        x = y = 0 # координаты
        for row in level: # вся строка
            for col in row: # каждый символ
                if col == "-":              
                    pf = Dirt(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == ".":
                    pf = Grass(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == ",":
                    pf = Gc(x, y)
                    entities.add(pf)
                    platforms.append(pf)    
                elif col == "/":
                    pf = Gr(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "z":
                    pf = Box(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "v":
                    pf = Chest(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "c":
                    pf = Cloud(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "+":
                    pf = Bonus(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "_":
                    pf = Plank(x, y)
                    entities.add(pf)
                    platforms.append(pf)    
                elif col == "y":
                    pf = Chai(x, y)
                    entities.add(pf)
                elif col == "g":
                    pf = Gelik(x, y)
                    entities.add(pf)
                elif col == "b":
                    pf = Bridge(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "s":
                    pf = Sand(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "w":
                    pf = Water(x, y)
                    entities.add(pf)
                elif col == "f":
                    pf = Fence(x, y)
                    entities.add(pf)
                elif col == "p":
                    pf = Finish(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                elif col == "h":
                    pf = Switch(x, y)
                    entities.add(pf)
                elif col == "`":
                    pf = G(x, y)
                    entities.add(pf)
                elif col == "m":
                    pf = M(x, y)
                    entities.add(pf)
                elif col == "u":
                    pf = Bush(x, y)
                    entities.add(pf)    
                x += PLATFORM_WIDTH 
            y += PLATFORM_HEIGHT   
            x = 0
        
        total_level_width  = len(level[0])*PLATFORM_WIDTH 
        total_level_height = len(level)*PLATFORM_HEIGHT        
        camera = Camera(camera_configure, total_level_width, total_level_height)

        font=pygame.font.Font(None,38) 
        text=font.render(("Найти ключ"), 10,(102,0,204))# выводим надпись
    
        while not player.winner:        
            clock.tick(60)
            screen.blit(text, (10,10))
            
            pygame.event.pump()        
            player.update(platforms)        
            for e in pygame.event.get(): # Обрабатываем события
                if e.type == QUIT:
                    raise SystemExit; "QUIT"
            camera.update(player)    
            for e in entities:
                screen.blit(e.image, camera.apply(e))       
            pygame.display.flip()                                           
            screen.blit(bg, (0,0))      # Каждую кадр НЕОБХОДИМО всё перерисовывать               
            
            key = pygame.key.get_pressed()        
            if key[pygame.K_ESCAPE]:        
                #sys.exit()
                main()
            
        for e in entities:
            screen.blit(e.image, camera.apply(e)) # еще раз все перерисовываем
            font=pygame.font.Font(None,58) 
            text=font.render(("Вы прошли игру"), 1,(0,0,0))# выводим надпись
            screen.blit(text, (60,100))
            pygame.display.update()
            time.wait(10000)
            sys.exit()
#sys.exit()            
pygame.quit()

if __name__ == "__main__":
    main()