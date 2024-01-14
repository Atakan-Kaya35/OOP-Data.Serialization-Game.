import pygame
from variables import Display_Vars as DV

class Screen():
    def __init__(self):
        #self.background = pygame.image.load('blackjack_icon.png')
        #pygame.display.set_icon(self.background)
        pygame.display.set_caption("Poker")
        self.surface = pygame.display.set_mode((DV.DEFAULT_IMAGE_WIDTH, DV.DEFAULT_IMAGE_HEIGHT))