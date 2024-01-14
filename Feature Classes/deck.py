import pygame
from card import Card
import random
from variables import Arrays as AR


class Deck:
    def __init__(self):
        self.all_cards = []

        # Create a deck of cards
        for l in AR.suits:
            for i in AR.ranks:
                created = Card(l, i)
                self.all_cards.append(created)

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.all_cards)

    def __str__(self):
        # Display all cards in the deck
        for i in range(len(self.all_cards)):
            print(self.all_cards[i])
        return " "