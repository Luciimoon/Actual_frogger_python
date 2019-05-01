import pygame, sys
from pygame.locals import*
from Person import *
from Wall import *
from Wall2 import *
from Anvil import *
import random
import time

# Creates a screen that is 800 x 600
pygame.init()
screen = pygame.display.set_mode((800, 600))

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Every 100 milliseconds check if a key is still pressed down
# Allows user to hold down the key to move
pygame.key.set_repeat(60, 60)

# create a person at position (40,40
guy = Person(350, 550)
theWall = Wall(150, 150)
theWall2 = Wall2(0,150)
theAnvil = Anvil(50, 500)

# A list that keeps track of the areas of screen that have changed
changedRecs = []

# draw the starting screen
WHITE = (0,90,40)
BLACK = (0, 0, 0)
red = (250, 0, 0)
screen.fill(WHITE)
theWall.draw(screen)
theWall2.draw(screen)
theAnvil.draw(screen)
pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

while True:
    # draw the scene
    screen.fill(WHITE)
    theWall.draw(screen)
    theWall2.draw(screen)
    theAnvil.draw(screen)
    guy.draw(screen)

    # adds the current position of guy to the areas that have been changed
    changedRecs.append(guy.getRec())

    # update only the changed areas of the screen
    pygame.display.update(changedRecs)

    # check all events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            # add the old position of guy to the areas of guy that have been changed
            changedRecs.append(guy.getRec())
            # move according to the key pressed. If it hits the wall, move the opposite direction
            #if event.key == K_UP:
               # guy.moveUp()
                #if guy.collide(theWall):
                   # guy.moveDown()

            #elif event.key == K_DOWN:
               # guy.moveDown()
                #if guy.collide(theWall):
                    #guy.moveUp()

            if event.key == K_LEFT:
                guy.moveLeft()
                if guy.collide(theWall):
                    guy = Person(750, 550)
                elif guy.collide(theWall2):
                    guy.guy = Person(750, 550)

            elif event.key == K_RIGHT:
                guy.moveRight()
                if guy.collide(theWall):
                    guy = Person(0, 550)
                elif guy.collide(theWall2):
                    guy = Person(0, 550)

            if guy.collide(theAnvil):
                message_display('You Died')


