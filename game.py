##########################################################################
# A game named as 'Evade' developed using Python' pygame library.
##########################################################################

import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")

block_color = (53, 115, 255)
car_width = 50
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Evade')
clock = pygame.time.Clock()

carImg = pygame.image.load('save_car.png')

game_icon = pygame.image.load('car.png')
pygame.display.set_icon(game_icon)

pause = False


def blocks_dodged(count):
    """Updates the interface with the number of blocks dodged.

    Parameters
    ----------
    count : int
        Represents number of blocks dodged.

    Returns
    -------
    None

    """
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged:" + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def blocks(
        block_x_position,
        block_y_position,
        block_width,
        block_height,
        color):
    """Draws the block

    Parameters
    ----------
    block_x_position : int
        x coordinate of the block
    block_y_position : int
        y coordinate of the block
    block_width : int
        width of the block
    block_height : int
        height of the block
    color : tuple
        color of the block

    Returns
    -------
    None

    """
    pygame.draw.rect(
        gameDisplay, color, [
            block_x_position, block_y_position, block_width, block_height])


def car(x, y):
    """Presents the car image at respective coordinate.

    Parameters
    ----------
    x : int
        x-coordinate of the car
    y : int
        y-coordinate of the car

    Returns
    -------
        None

    """
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    """Return text objects

    Parameters
    ----------
    text : str
        Text to be written
    font : str
        Font of the text to be written
    Returns
    -------
    obj :
        text surface object
    obj :
        text surface rectangle
    """
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    """Brings forward an interface which revels you have crashed the car into
       the brick.Stops the music and presents you with options to continue or quit
       the game.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()

    large_text = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You crashed", large_text)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    """Makes interactive button.

    Parameters
    ----------
    msg : str
      Message to be displayed on the button
    x : int
      x coordinate to form the button
    y : int
      y coordinate to form the button
    w : int
      width of the button
    h : int
      height of the button
    ic : tuple
      Color of the button when mouse is not hovering over the button.
    ac : tuple
      Color of the button when mouse is hovering over the button.
    action : method
        Respective method to be invoked

    Returns
    -------
    None

    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    """Quits the game

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    pygame.quit()
    quit()


def unpause():
    """Unpauses the game

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    """Pauses the game and presents options to continue / quit.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    pygame.mixer.music.pause()
    large_text = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", large_text)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    """Forms the first interface of the game, clicking
       'GO' button will start the game and clicking 'Quit' button
       will quit the game.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        large_text = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("evasion", large_text)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO", 150, 450, 100, 50, green, bright_green, game_loop)
        button("QUIT", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    """Most important method of the game.
       Plays the music and decides how much car is to be moved when we click
       left or right arrows.Decides, if the brick is dodged or if we have met the
       crash condition.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    global pause
    pygame.mixer.music.load("jazz.wav")
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.85)
    x_change = 0
    dodged = 0

    block_start_yposition = -600
    block_speed = 6
    block_width = 50
    block_height = 50
    block_start_xposition = random.uniform(0, display_width - block_width)

    blockCount = 1

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        blocks(
            block_start_xposition,
            block_start_yposition,
            block_width,
            block_height,
            block_color)
        block_start_yposition = block_start_yposition + block_speed
        car(x, y)
        blocks_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if block_start_yposition > display_height:
            block_start_yposition = -50
            dodged = dodged + 1
            # here we are increasing speed and width
            block_speed = random.uniform(8, 12)
            block_width = random.uniform(50, 150)
            block_start_xposition = random.uniform(
                0, display_width - block_width)

        if y < block_start_yposition + block_height:
            print('y crossover {0}'.format(y))
            print('block_start_yposition {0}'.format(block_start_yposition))
            print(x)

            crash_condition = x > block_start_xposition and x < block_start_xposition + block_width or x + \
                car_width > block_start_xposition and x + car_width < block_start_xposition + block_width

            if crash_condition:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(100)


game_intro()
game_loop()
pygame.quit()
quit()
