import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Evade')
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
quit()

###
