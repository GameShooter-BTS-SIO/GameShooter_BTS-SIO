
import pygame
pygame.init()
(largeur, hauteur) = (500, 800)
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Game Shooter')
pygame.display.update()
running = True
x=150
y=60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, (200,128,50), pygame.Rect(150, 60, 90, 90))
    pygame.draw.rect(screen, (200,128,50), pygame.Rect(250, 60, 90, 90))
    pygame.draw.rect(screen, (200,128,50), pygame.Rect(200, 150, 90, 300))
    pygame.display.flip()
    size = (50, 50)
    radius = 25
    pygame.draw.circle(size, (255, 0, 0), pygame.surface(radius, radius) )
