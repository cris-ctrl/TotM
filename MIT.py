import pygame, sys
wall = []
wall.append(pygame.Rect(500,40, 20, 300))
wall.append(pygame.Rect(100,300, 500, 20))
wall.append(pygame.Rect(150,40, 20, 160))


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