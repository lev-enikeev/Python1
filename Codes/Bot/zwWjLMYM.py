from typing import Tuple

import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('привет мир')

black = (0, 0, 0)
white = (225, 225, 225)
red = (225, 0, 0)
green = (0, 225, 0)
blue = (0, 0, 225)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('привет мир!', True, white, blue)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centerx = windowSurface.get_rect().centery
windowSurface.fill(white)

pygame.draw.polygon(windowSurface, green, ((146, 0), (291, 106), (236, 227), (56, 227), (0, 106)))
pygame.draw.line(windowSurface, blue, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, blue, (120, 60), (60, 120), 4)
pygame.draw.line(windowSurface, blue, (60, 120), (120, 120), 4)

pygame.draw.circle(windowSurface, red, (300, 50), 20, 0)
pygame.draw.ellipse(windowSurface, red, (300, 250, 40, 80), 1)
pygame.draw.rect(windowSurface,red,(textRect.left-20,textRect.top-20,textRect.width+40,textRect.height+40))

pixArray = pygame.PixelArray(windowSurface)
pixArray[480][300] = black
del pixArray

windowSurface.blit(text, textRect)
pygame.display.update()
э
