import pygame
from variables import Colors as CL
from variables import Fonts as FT

def handleBet(amount, beter, betee):
    responce = 0
    # Check if the betted amount bets the betee All-in and acts accordingly
    if amount < betee.player.balance:
        # requests a reponce from the betee, helps by pre-moving its slider to the right amount
        betee.selectedAmount = amount
        while 0 <= responce < amount:
            betee.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                responce = betee.update(event)

    else:
        # requests a reponce from the betee, helps by pre-moving its slider to the right amount
        betee.selectedAmount = betee.player.balance
        betee.draw()
        while 0 <= responce < betee.player.balance: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                responce = betee.update(event)
    
    # -1 means fold, elif signals a re-raise, else means the bet is accepted
    if responce == -1:
        return -1, beter.player.index
    elif responce > amount:
        return handleBet(responce, betee, beter)
    else:
        return responce, beter.player.index
    
class Displayers:
    def display_specific(screen, message, x, y, aFont = FT.font, preferredColor = CL.white_color):
        # display any text wherever wanted 
        messsage = aFont.render(str(message), True, preferredColor)
        screen.surface.blit(messsage, (x, y))
        pygame.display.update()



    def display_centered_message(screen, box_color, text_color, message, x, y, aFont = FT.font):
        text_width, text_height = aFont.size(message)

        # calculate box top-left cords
        y_start = y - text_height / 2
        x_start = x - text_width / 2

        # make the rectangle and text
        pygame.draw.rect(screen.surface, box_color, (x_start, y_start, text_width, text_height))
        Displayers.display_specific(screen, message, x_start, y_start, aFont, preferredColor=text_color)

        pygame.display.update()

    def display_centered_constantBox_message(screen, box_color, text_color, message, x, y, boxWidth, boxHeight, aFont = FT.font):
        text_width, text_height = aFont.size(message)

        # calculate box top-left cords
        y_start_box = y - boxHeight / 2
        x_start_box = x - boxWidth / 2

        y_start_text = y - text_height / 2
        x_start_text = x - text_width / 2

        # make the rectangle and text
        pygame.draw.rect(screen.surface, box_color, (x_start_box, y_start_box, boxWidth, boxHeight))
        Displayers.display_specific(screen, message, x_start_text, y_start_text, aFont, preferredColor=text_color)

        pygame.display.update()

    def display_changing_centered_message(screen, box_color, text_color, message, maxText, x, y, aFont = FT.font):
        max_text_width, max_text_height = aFont.size(maxText)
        text_width, text_height = aFont.size(message)

        # calculate box and writing top-left cords
        y_start = y - text_height / 2
        x_start = x - text_width / 2
        max_y_start = y - max_text_height / 2
        max_x_start = x - max_text_width / 2

        # make the rectangle and text
        pygame.draw.rect(screen.surface, box_color, (max_x_start, max_y_start, max_text_width, max_text_height))
        Displayers.display_specific(screen, message, x_start, y_start, aFont, preferredColor=text_color)

        pygame.display.update()
