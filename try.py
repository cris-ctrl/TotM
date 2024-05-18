#This is a "trow away file" used to test concepts and code blocks (likely kindly made for me from chat gpt lmfaooo)before implementing it on the full code.
#most likely will be empty if im not working with anything complex atm

import pygame, sys

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Constants
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

# Helper function to get image from sprite sheet
def get_img(sheet, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

# Create walls
wall = [pygame.Rect(500, 40, 20, 300), pygame.Rect(100, 300, 500, 20), pygame.Rect(150, 40, 20, 160)]

# Load animation frames
alist = [get_img(sprite_sheet, x, 24, 24, 2, (255, 255, 255)) for x in range(6)]

# Initial variables
run = True
x, y = 0, 0
frame = 0
lastt = pygame.time.get_ticks()

# Main game loop
while run:
    detec = pygame.Rect(x, y, 24 * 2, 24 * 2)
    key = pygame.key.get_pressed()
    direction = None
    
    if key[pygame.K_w]: direction = (0, -1)
    elif key[pygame.K_s]: direction = (0, 1)
    elif key[pygame.K_a]: direction = (-1, 0)
    elif key[pygame.K_d]: direction = (1, 0)
    
    if direction:
        dx, dy = direction
        
        
        while not any(detec.colliderect(rect) for rect in wall):
            detec.x += dx
            detec.y += dy
        
        detec.x -= dx
        detec.y -= dy
        x, y = detec.x, detec.y
    
    screen.fill(bg)
    
    # Animate sprite
    if pygame.time.get_ticks() >= lastt + cooldown:
        frame = (frame + 1) % len(alist)
        lastt = pygame.time.get_ticks()
    
    # Draw everything
    pygame.draw.rect(screen, (255, 255, 255), detec)
    screen.blit(alist[frame], (x, y))
    for rect in wall:
        pygame.draw.rect(screen, (255, 0, 0), rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
