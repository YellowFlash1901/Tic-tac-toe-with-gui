#to quit the application (sys)
import sys
from turtle import width 
import pygame

from constants import *

#pygame SETUP

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("TIC TAC TOE AI By vardaan sathe")
screen.fill(BG_COLOR)  #Background color

#creating game object 

class Game:
    
    def __init__(self):
        self.show_lines()

    def show_lines(self):
        #VERTICAL
        #Format of line fuctoin is (screen , line color , starting position , ending position , width )
        pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,600), LINE_WIDTH)

def main():
    #object
    game = Game()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    Pygame.display.update() #updates the Pygame setup

main()