import pygame, sys
#becum
run = True
pygame.init()
clock = pygame.time.Clock()

#innit
lastk = 5
x = 0
y = 0
px = 0
py = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TotM")

#assets
icon = pygame.image.load("assets/logos/logo_64.png")
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


#test walls:
map = []
map.append(pygame.Rect(500,40, 20, 300))
map.append(pygame.Rect(100,300, 500, 20))
map.append(pygame.Rect(150,40, 20, 160))

#animation bruv
alist = []
aframes = 6
for x in range(aframes):
    alist.append(get_img(sprite_sheet,x, 24, 24, 2, (255,255,255)))
cooldown = 70
lastt = pygame.time.get_ticks()
frame = 0



#main game loop
while run:  
     detec = pygame.Rect(x+4, y+6, 21 * 2, 21 * 2)
     coll = False
     for rect in map:
         if detec.colliderect(rect):
             coll = True
             break  
         else:
             coll = False
     if coll:
         print("collided")
     else:
         print("didnt collide")
     screen.fill(bg)
     #playing animation yuh
     if pygame.time.get_ticks() >= lastt + cooldown:
         frame += 1
         lastt = pygame.time.get_ticks()
         if frame >= len(alist):
             frame = 0
     
    #mr picasso boy (draws stuff)
     pygame.draw.rect(screen,(50,50,50),detec)
     screen.blit(alist[frame],(x,y))
     for ret in map:
         pygame.draw.rect(screen,(255,0,0),ret)

     #"snapping" movimentation system -> """path finder"""
     # 0 = up, 1 = down, 2 = left, 4 = right
    


     #event handling
     key = pygame.key.get_pressed()
     if key[pygame.K_a] == True: 
         x = x - 1
         lastk = 2
     if key[pygame.K_d] == True: 
         x += 1
     if key[pygame.K_s] == True: 
         y = y + 1
     if key[pygame.K_w] == True: 
         y = y - 1
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
     pygame.display.update()
     clock.tick(60)
pygame.quit()