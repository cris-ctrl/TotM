import pygame
from MIT import *  

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# init
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
bg = (50, 50, 50)
cooldown = 70

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TotM")

# Load assets
icon = pygame.image.load("assets/logos/logo_64.png")
pygame.display.set_icon(icon)
sprite_sheet = pygame.image.load("assets/char/mainsheet_tom.png").convert_alpha()

#Image extractor from spritesheet
def get_img(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

#rotate tool
def rotate(frame, angle):
    rotated = [pygame.transform.rotate(alist[frame], angle)]
    return rotated

# Load animation frames
alist = [get_img(sprite_sheet, x, 24, 24, 2, (255, 255, 255)) for x in range(6)]

# Initial variables
run = True
x, y = 0, 0
frame = 0
lastt = pygame.time.get_ticks()

# Main game loop
while run:
    dx, dy = 0, 0
    detec = pygame.Rect(x + 4, y + 6, 21 * 2, 21 * 2)
    moved = False

    # Event handling
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        dx = -1
        moved = True
    if key[pygame.K_d]:
        dx = 1
        moved = True
    if key[pygame.K_s]:
        dy = 1
        moved = True
    if key[pygame.K_w]:
        dy = -1
        moved = True

    # Snapping movement system
    if moved:
        while not any(detec.colliderect(rect) for rect in wall):
            detec.x += dx
            detec.y += dy
        detec.x -= dx
        detec.y -= dy
        x, y = detec.x - 4, detec.y - 6

    screen.fill(bg)

    if pygame.time.get_ticks() >= lastt + cooldown:
         frame += 1
         lastt = pygame.time.get_ticks()
         if frame >= len(alist):
             frame = 0
    # Draw everything
    pygame.draw.rect(screen, (255, 255, 255), detec)
    screen.blit((alist[frame]), (x, y))
    for rect in wall:  # wall should be imported from MIT
        pygame.draw.rect(screen, (255, 0, 0), rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()



