import pygame
from MIT import *  

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()




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



