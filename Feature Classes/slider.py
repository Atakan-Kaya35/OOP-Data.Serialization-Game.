import pygame
from button import Button
from utilities import Displayers
from variables import Colors as CL
from variables import Fonts as FT
from variables import Display_Vars as DV

class Slider:
    def __init__(self, height, xPos, yPos, player, screen, oponent, width = DV.DEFAULT_IMAGE_WIDTH / 90):
        """
        Initialize the Slider object with its properties.
        
        Args:
        - height (int): The height of the slider.
        - xPos (int): X-coordinate position of the slider.
        - yPos (int): Y-coordinate position of the slider.
        - player (Player): The player associated with the slider.
        - screen (pygame.Surface): The screen where the slider is displayed.
        - oponent (Player): The opponent player.
        - width (int, optional): The width of the slider. Default is 8.
        """
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.screen = screen
        self.oponent = oponent
        self.handleY = yPos + height
        self.handleDeviation = self.width * 1.5
        self.selectedAmount = 0
        self.player = player
        self.yesButton = Button(self.xPos + self.width / 2 - FT.small_font.size(DV.MAX_NUM)[0] / 2, 
                                self.yPos + self.height + 4 * self.width,
                                FT.small_font.size("Yes")[0], FT.small_font.size("Yes")[1],
                                "Yes", CL.green_color, FT.font)
        self.noButton = Button( self.xPos + self.width / 2 + FT.small_font.size(DV.MAX_NUM)[0] / 2, 
                                self.yPos + self.height + 4 * self.width,
                                FT.small_font.size("Yes")[0], FT.small_font.size("Yes")[1],
                                "No", CL.red_color, FT.font)
    
    def draw(self):
        """
        Draw the slider and its components on the screen.
        """
        # draw bar
        pygame.draw.rect(self.screen.surface, CL.red_color, (self.xPos, self.yPos, self.width, self.height))
        # Calculate and display handle length based on the selected amount
        handleLength = self.height * ((self.selectedAmount) / (self.player.balance + 1))
        pygame.draw.rect(self.screen.surface, CL.white_color, (self.xPos, self.yPos + self.height - handleLength, self.width, 
                                                    handleLength))
        # draw the value
        Displayers.display_changing_centered_message(self.screen, CL.white_color, CL.red_color, str(round(self.selectedAmount, 1)), DV.MAX_NUM,
                                 self.xPos + self.width / 2, self.yPos + self.height + self.width * 1.5, aFont = FT.small_font)

        """ pygame.draw.rect(self.screen, white_color, (self.xPos - self.width * 2, self.yPos + self.height + self.width, 38, 13))
        display_specific(str(self.selectedAmount), self.xPos - self.width * 2, self.yPos + self.height + self.width, preferredColor= red_color, aFont= small_font) """

        # Draw the 'Yes' and 'No' buttons on the screen
        self.yesButton.draw(self.screen)
        self.noButton.draw(self.screen)
        pygame.display.update()

    def update(self, event):
        """
        Update the slider based on the user's input event.
        
        Args:
        - event (pygame.Event): The event captured by Pygame.
        
        Returns:
        - int: The amount selected by the player.
        """

        mouseX, mouseY = pygame.mouse.get_pos()
        # check if the mouse has pressed on the slider
        if pygame.mouse.get_pressed()[0] and self.xPos - self.handleDeviation < mouseX < self.xPos + self.handleDeviation and self.yPos < mouseY < self.yPos + self.height:
            self.handleY = mouseY
            self.handleY = min(self.yPos + self.height, max(self.yPos, self.handleY))
            self.selectedAmount = round(self.player.balance * (self.height + self.yPos - self.handleY) / self.height, 1)
            self.draw()
        
        # Checks for button presses
        if self.noButton.handle_event(event):
            return -1
        
        # returns the entered slider amount as a bet
        if self.yesButton.handle_event(event):
            give = self.selectedAmount
            self.selectedAmount = 0
            self.draw()
            return give
        return 0