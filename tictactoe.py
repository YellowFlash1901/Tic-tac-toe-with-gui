#to quit the application (sys)
import sys
from turtle import width 
import pygame

from constants import *

#pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("TIC TAC TOE AI By vardaan sathe")


def main():
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()