import pygame
import random
from pygame.locals import *
import os
import math


window_dimensions = [800, 600]
pygame.init()
fenetre = pygame.display.set_mode((window_dimensions[0], window_dimensions[1]), pygame.RESIZABLE)
pygame.display.set_caption("Telegame Editor")

def saveToFile(filename, mapConfig):
    f = open(filename, "w+")
    for l in mapConfig:
        for t in l:
            f.write()
            f.write(" ")
        f.write("\n")
    f.close()

