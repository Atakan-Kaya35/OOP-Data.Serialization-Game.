import pygame
from variables import Arrays as AR
from variables import Display_Vars as DV
import os
new_directory = "\\Users\\hp\\Desktop\\Coding\\Projects\\Poker\\Broken Down\\pixelateds"
os.chdir(new_directory)

class Card:
    def __init__(self, suit, rank):
        # Initialize card attributes
        self.rank = rank
        self.suit = suit
        self.value = AR.value_key[rank]
        self.position = AR.position_key[rank]
        self.name = self.rank + " of " + self.suit
        
        # Determine the card name based on rank and suit
        if self.rank not in ["Ace", "King", "Queen", "Jack"]:
            self.card_name = str(self.value) + "_of_" + self.suit
        elif self.rank in ["Ace", "King", "Queen", "Jack"]:
            self.card_name = self.rank.lower() + "_of_" + self.suit.lower()

        # Load and scale the card image
        new_directory = "\\Users\\hp\\Desktop\\Coding\\Projects\\Poker\\Broken Down\\pixelateds"
        os.chdir(new_directory)
        self.appearance = pygame.image.load(f'{self.card_name}.png')
        self.appearance = pygame.transform.scale(self.appearance, DV.default_card_size)

    def __str__(self):
        return self.name