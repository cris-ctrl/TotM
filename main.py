import pygame, sys
#becum
run = True
pygame.init()
clock = pygame.time.Clock()

#innit
player = pygame.Rect((100,110, 50, 50))
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#assets
icon = pygame.image.load("assets/logos/logo.png")
pygame.display.set_icon(icon)
bg=(50,50,50)
sprite_sheet = pygame.image.load("assets/char/mainsheet_tom.png").convert_alpha()        

#get image thing
def get_img(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0),((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image




#animation bruv
alist = []
aframes = 6
for x in range(aframes):
    alist.append(get_img(sprite_sheet,x, 24, 24, 2, (255,255,255)))
cooldown = 1000
lastt = pygame.time.get_ticks()
frame = 0



#main game loop
while run:
     screen.fill(bg)
     #playing animation yuh
     if pygame.time.get_ticks() >= lastt:
         frame += 1
         lastt = pygame.time.get_ticks()
         if frame >= len(alist):
             frame = 0

    
     screen.blit(alist[frame],(0,0))



     #event handling
     key = pygame.key.get_pressed()
     if key[pygame.K_a] == True: 
         player.move_ip(-1, 0)
     if key[pygame.K_d] == True: 
         player.move_ip(+1, 0)
     if key[pygame.K_s] == True: 
         player.move_ip(0, 1)
     if key[pygame.K_w] == True: 
         player.move_ip(0, -1)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
     pygame.display.update()
     clock.tick(30)
pygame.quit()