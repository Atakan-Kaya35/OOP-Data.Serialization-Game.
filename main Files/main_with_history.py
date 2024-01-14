import pygame
import time
from screen import Screen
from table import Table
from deck import Deck
from player import Player
from slider import Slider
from coordinator import Coordinator
from variables import Display_Vars as DV
from variables import Images as IM
from variables import Colors as CL
from variables import Fonts as FT
from utilities import Displayers
from utilities import handleBet


screen = Screen()

# game specific variables
p1Balance = 100
p2Balance = 100
noWinner = True
entery_stake = 2

# initialize players and their sliders
player1 = Player(screen, 1, balance = p1Balance)
player2 = Player(screen, 2, balance = p2Balance)
p1Slider = Slider(DV.CARD_HEIGHT, player1.xPrint + 1.8 * DV.CARD_WIDTH, 
                    player1.yGap ,player1, screen, player2)
p2Slider = Slider(DV.CARD_HEIGHT, player2.xPrint - 0.2 * DV.CARD_WIDTH, 
                    player2.yGap ,player2, screen, player1)

coordinator = Coordinator(screen, player1, player2, p1Slider, p2Slider, "\\Users\\hp\\Desktop\\Coding\\Projects\\Poker\\Broken Down\\pixelateds")
coordinator.menu()

# every iteration of the loop is one hand of Poker
while noWinner:
    p1Slider.selectedAmount = 0
    p2Slider.selectedAmount = 0
    turnNo = 0
    screen.surface.blit(IM.bg_img, (0, 0))

    # new deck is needed for every new hand
    theDeck = Deck()
    theDeck.shuffle()

    # a new table object
    playMedium = Table(screen, theDeck)

    # standard poker rule of starting bet
    pot = 2 * entery_stake

    # deal players their cards
    player1.acquireCards(theDeck.all_cards.pop(), theDeck.all_cards.pop())
    player2.acquireCards(theDeck.all_cards.pop(), theDeck.all_cards.pop())

    p1Slider.draw()
    p2Slider.draw()

    # conrols wheter the player's cards are face up or down in each tick
    show_cards_of = [True] * 2

    # in game operations (bets, cards peeks, card draws)
    while turnNo < 4:
        # display the pot
        Displayers.display_centered_message(screen, CL.table_color, CL.white_color, str(round(pot,1)), DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT / 2)

        # display the cards at each turn
        player1.displayHand(show_cards_of[0])
        player2.displayHand(show_cards_of[1])
        pygame.display.update()

        # standard Pygame way of geting actions to happen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            # instant click activated events (showing cards, advancing turn)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    show_cards_of[0] = False
                elif event.key == pygame.K_RIGHT:
                    show_cards_of[1] = False
                
                if event.key == pygame.K_DOWN:
                    coordinator.menu()
                
                if event.key == pygame.K_UP:
                    turnNo += 1

            # relieving hold triggered functions (showing cards)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    show_cards_of[0] = True
                elif event.key == pygame.K_RIGHT:
                    show_cards_of[1] = True
        
        # controling what turn will be called, relevant for infor displayed on screen
        if turnNo == 1:
            playMedium.firstTurn()
        elif turnNo == 2:
            playMedium.secondTurn()
        elif turnNo == 3:
            playMedium.lastTurn()

        # there can be loop of bet-reraises, so it must be made sure the players agree on the amount
        prev1 = player1.balance
        prev2 = player2.balance

        # check's if any of the players sellected a value and pressed yes to submit, if so calls handleBet method
        # the agreed bet from the player desicions is assigned to "agreed" (0 is no bet, -1 is fold, >0 means game is on)
        agreed = 0
        p1Slider.draw()
        resp = p1Slider.update(event)
        if resp > 0:
            agreed, bet_maker = handleBet(resp, p1Slider, p2Slider)
        p2Slider.draw()
        resp = p2Slider.update(event)
        if resp > 0:
            agreed, bet_maker = handleBet(resp, p2Slider, p1Slider)

        winner = 0
        # if folded
        if agreed < 0:
            winner = bet_maker
            turnNo = 5
        
        # if bet on, money showed to the middle
        elif agreed > 0:
            turnNo += 1
            player1.changeBalance(-agreed)
            player2.changeBalance(-agreed)
            pot += 2 * agreed
        
        # if a player went all in it's time to wrap it up
        if player1.balance == 0:
            player1.all_in()
            turnNo = 5
        if player2.balance == 0:
            player2.all_in()
            turnNo = 5

        # tick mechanizm
        pygame.display.flip()
        pygame.time.Clock().tick(50)
    
    # touring turns in case all functions were not executed due to early exit (fold or all in)
    playMedium.firstTurn()
    playMedium.secondTurn()
    playMedium.lastTurn()
    
    # winning conditions checked
    p1Score = player1.conditionChecker(playMedium.tableCards)
    p2Score = player2.conditionChecker(playMedium.tableCards)

    # every info is displayed, extra all in sign created if happened
    player1.displayHand(False)
    player2.displayHand(False)
    if player1.balance == 0:
        player1.all_in()
    if player2.balance == 0:
        player2.all_in()
    
    Displayers.display_centered_message(screen, CL.table_color, CL.white_color, str(pot), DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT / 2)
    """ pygame.draw.rect(screen.surface, (17,90,61), (DEFAULT_IMAGE_WIDTH / 2.5, DEFAULT_IMAGE_HEIGHT / 2, 115, 50))
    display_specific(str(pot), DEFAULT_IMAGE_WIDTH / 2.5, DEFAULT_IMAGE_HEIGHT / 2) """
        
    print(p1Score, " ", p2Score)

    # if the game ended in a shootout, a winner is deemed
    if winner == 0:
        if p1Score > p2Score:
            message = 1
        elif p1Score < p2Score:
            message = 2
        else:
            if player1.cardTotal < player2.cardTotal:
                message = 2
            elif player1.cardTotal > player2.cardTotal:
                message = 1
            else:
                message = 0

    # if not (folded) the beter wins
    else:
        message = bet_maker

    # chips are pushed to the winner
    if message == 1:
        message = "Player 1 WON"
        player1.changeBalance(pot)
        pot = 0
    elif message == 2:
        message = "Player 2 WON"
        player2.changeBalance(pot)
        pot = 0

    # chips pushed back if draw (rare)
    else:
        message = "DRAW"
        player1.changeBalance(pot / 2)
        player2.changeBalance(pot / 2)
        pot = 0
    
    # wait for a key press to move on to the next hand
    stay = True
    while stay:
        Displayers.display_centered_message(screen, CL.table_color, CL.white_color, message, 
                                            DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT - FT.font.size(message)[1]/2)
        #Displayers.display_specific(screen, message, (DV.DEFAULT_IMAGE_WIDTH + DV.DEFAULT_IMAGE_HEIGHT) / 5, (3 * DV.VERTICAL_GAP + 2 * DV.CARD_HEIGHT) - 55)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                stay = False
    
    # entry fee deducted from players (done here since a player may not be able to start the next round at all)
    player1.changeBalance(-entery_stake)
    player2.changeBalance(-entery_stake)

    # checked if a player has won!
    if player1.balance < 0:
        Displayers.display_specific(screen, "PLAYER 2 WON, CONGRATS!", DV.DEFAULT_IMAGE_WIDTH / 4, DV.DEFAULT_IMAGE_HEIGHT / 2, preferredColor = CL.red_color)
        noWinner = False
        time.sleep(5)
    elif player2.balance < 0:
        Displayers.display_specific(screen, "PLAYER 1 WON, CONGRATS!", DV.DEFAULT_IMAGE_WIDTH / 4, DV.DEFAULT_IMAGE_HEIGHT / 2, preferredColor = CL.red_color)
        time.sleep(5)
        noWinner = False
    