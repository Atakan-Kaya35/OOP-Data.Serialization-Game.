import pygame
from variables import Display_Vars as DV

class Table:
    def __init__(self, screen, theDeck):
        self.tableCards = []
        # with this line the game can automatically decide the position of the 
        # cards that the table opens through the equation "(image size) = 4(card gaps) + 5(cards) + 2(buffers)"
        self.buffer = ((DV.DEFAULT_IMAGE_WIDTH - 4 * DV.HORIZONTAL_GAP - 5 * DV.CARD_WIDTH) / 2)
        self.yGap = DV.VERTICAL_GAP
        self.firsts = [True] * 3
        self.theDeck = theDeck
        self.screen = screen
    
    def firstTurn(self):
        # check if the step was executed before
        if self.firsts[0]:
            # Deal the first three cards from the deck
            card1 = self.theDeck.all_cards.pop()
            card2 = self.theDeck.all_cards.pop()
            card3 = self.theDeck.all_cards.pop()

            # Add cards to the table and display them
            self.tableCards.extend([card1, card2, card3])
            pygame.display.update()

            # Display the cards on the screen
            self.screen.surface.blit(card1.appearance, (self.buffer, self.yGap))
            self.buffer += DV.CARD_WIDTH + DV.HORIZONTAL_GAP
            self.screen.surface.blit(card2.appearance, (self.buffer, self.yGap))
            self.buffer += DV.CARD_WIDTH + DV.HORIZONTAL_GAP
            self.screen.surface.blit(card3.appearance, (self.buffer, self.yGap))
            self.buffer += DV.CARD_WIDTH + DV.HORIZONTAL_GAP
            pygame.display.update()

            # Lock up the step
            self.firsts[0] = False

    def secondTurn(self):
        # check if the step was executed before
        if self.firsts[1]:
            # Deal the fourth card from the deck
            card = self.theDeck.all_cards.pop()

            # Add the card to the table and display it
            self.tableCards.append(card)
            self.screen.surface.blit(card.appearance, (self.buffer, self.yGap))
            self.buffer += DV.CARD_WIDTH + DV.HORIZONTAL_GAP
            pygame.display.update()

            # Lock up the step
            self.firsts[1] = False

        
    def lastTurn(self):
        # check if the step was executed before
        if self.firsts[2]:
            # Deal the fifth card from the deck
            card = self.theDeck.all_cards.pop()

            # Add the card to the table and display it
            self.tableCards.append(card)
            self.screen.surface.blit(card.appearance, (self.buffer, self.yGap))
            pygame.display.update()

            # Lock up the step
            self.firsts[2] = False