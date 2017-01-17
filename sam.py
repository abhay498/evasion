import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Evade')
clock = pygame.time.Clock()

carImg = pygame.image.load('reds.png')

game_icon = pygame.image.load('car.png')
pygame.display.set_icon(game_icon)

car_width = 73

pause = False

##def button(msg,x,y,w,h,ic,ac):
##    mouse = pygame.mouse.get_pos()
##    click = pygame.mouse.get_pressed()
##    print(click)
##    #print(mouse)
##    if x + w > mouse[0] > x and y + h > mouse[1] > y:
##        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
##        if click[0] == 1 and action != None:
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
##    else:
##        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
##
##    smallText = pygame.font.Font("freesansbold.ttf",20)
##    textSurf, textRect = text_objects(msg,smallText)
##    textRect.center = ( (x + (w/2)),y + (h/2))
##    gameDisplay.blit(textSurface,textRect)
##    
##    pygame.draw.rect(gameDisplay,red,(550,450,100,50))

def game_intro():
    intro = True
##    while intro:
##        for event in pygame.event.get():
##            #print(event)
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
                
    gameDisplay.fill(white)
##    large_text = pygame.font.Font('freesansbold.ttf',30)
##    TextSurf, TextRect = text_objects("evasion",large_text)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf,TextRect)

##    button("GO!",150,450,100,50,green,bright_green,"go")
##    button("QUIT!",150,450,100,50,red,bright_red,"quit")
    
    pygame.display.update()
    clock.tick(15)

game_intro()
pygame.quit()
quit()
