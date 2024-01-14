import pygame
from utilities import Displayers
from variables import Display_Vars as DV
from variables import Colors as CL
from variables import Arrays as AR
from variables import Fonts as FT
from variables import Images as IM

class Player:
    def __init__(self, screen, indexOfPlayer, balance = 1000):
        # Initialize player attributes
        self.index = indexOfPlayer
        self.cardsInHand = []
        self.balance = balance
        self.cardTotal = 0
        self.screen = screen

        # "(image size) = 2(card gaps) + 4(cards) + 2(card / 2 [standard]) + (handBuffer)"
        # "handStarterBuffer = (image_size) - 2.5 (card) - (card gap)"
        self.handStarterBuffer = DV.DEFAULT_IMAGE_WIDTH - 2.5 * DV.CARD_WIDTH - 1 * DV.HORIZONTAL_GAP
        self.yGap = 2 * DV.VERTICAL_GAP + DV.CARD_HEIGHT
        self.xPrint = (DV.CARD_WIDTH / 2 + (self.index - 1) * self.handStarterBuffer)

    def acquireCards(self, card1, card2):
        self.cardsInHand = [card1, card2]
        # tyebreaker for when there is a pait or two pairs on poth players, 
        # can be put at the end of return statements for the condition checker
        self.cardTotal = AR.pair_key[max(card1.position, card2.position)] + AR.pair_key[min(card1.position, card2.position)] / 1000

    def displayHand(self, isHidden):
        # Define the x positions for displaying the cards
        x_positions = [self.xPrint, 
                       ((self.index - 1) * self.handStarterBuffer) + DV.CARD_WIDTH + DV.HORIZONTAL_GAP]
        
        # Display cards based on whether they should be hidden or not
        if isHidden:
            self.screen.surface.blit(IM.joker, (x_positions[0], self.yGap))
            self.screen.surface.blit(IM.joker, (x_positions[1], self.yGap))
        else:
            self.screen.surface.blit(self.cardsInHand[0].appearance, (x_positions[0], self.yGap))
            self.screen.surface.blit(self.cardsInHand[1].appearance, (x_positions[1], self.yGap))

        # Display cards based on whether they should be hidden or not
        Displayers.display_changing_centered_message(self.screen, CL.white_color, CL.black_color,
                                          str(round(self.balance, 1)), DV.MAX_NUM, x_positions[0] + DV.CARD_WIDTH * .7, self.yGap + DV.CARD_HEIGHT * 1.1, aFont=FT.small_font)
        
        pygame.display.update()
    
    def conditionChecker(self, tableCards):
        # Combine the player's hand and table cards
        possibleFive = tableCards + self.cardsInHand

        # make two maps of cards: one for numbers, one for suits
        suitsMap = [0] * 4
        valuesMap = [0] * 13
        
        # Populate the suits and values maps
        for card in possibleFive:
            if "Hearts" == card.suit:
                suitsMap[0] += 1
            elif "Diamonds" == card.suit:
                suitsMap[1] += 1
            elif "Spades" == card.suit:
                suitsMap[2] += 1
            else:
                suitsMap[3] += 1
            
            valuesMap[card.position - 1] += 1
            
        # best to worst win conditions will be checked and assigned when found
        if 5 in suitsMap:
            i = -4
            counter = 0
            possible = False
            while i < len(valuesMap) - 3:
                if valuesMap[i] > 0:
                    counter += 1
                else:
                    counter = 0
                
                if counter == 5:
                    possible = True
                    break
                i += 1
            
            if possible:
                if i == 0:
                    return 10
                
                else:
                    return 9
            
        if 4 in valuesMap:
            return 8
        
        if 3 in valuesMap:
            if 2 in valuesMap:
                return 7
            
        if 5 in suitsMap:
            return 6
        
        counter = 0
        i = 0
        while i < len(valuesMap):
            if valuesMap[i] > 0:
                counter += 1
            else:
                counter = 0
            
            if counter == 5:
                
                return 5

            i += 1
        
        if 3 in valuesMap:
            return 4
        if 2 in valuesMap:
            if valuesMap[0] == 2:
                extra = 1
            else:
                extra = len(valuesMap) - valuesMap[::-1].index(2)

            valuesMap[valuesMap.index(2)] = 0
            if 2 in valuesMap:
                
                return 3 + AR.pair_key[extra]
            else:
                
                return 2 + AR.pair_key[extra]
            
        if valuesMap[0] > 0:
            return 1 
        
        return 0
    
    def changeBalance(self, change):
        self.balance += change

    def all_in(self):
        Displayers.display_specific(self.screen, "ALL-IN", self.xPrint, self.yGap + DV.CARD_HEIGHT / 3, preferredColor = (0,0,255))
    
    def __str__(self):
        return "Player has: " + str(self.cardsInHand[0]) + " , " + str(self.cardsInHand[1])
         