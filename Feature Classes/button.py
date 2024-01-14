import pygame
from utilities import Displayers
from variables import Colors as CL
from variables import Fonts as FT

class Button:
    def __init__(self, x, y, width, height, text, boxColor, font, action = None):
        """
        Initialize the Button object with its properties.
        
        Args:
        - x (int): X-coordinate position of the button.
        - y (int): Y-coordinate position of the button.
        - width (int): Width of the button.
        - height (int): Height of the button.
        - text (str): Text displayed on the button.
        - color (tuple): RGB color tuple for the button background color.
        - font (pygame.Font): Font style for the button text.
        """
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.width = width
        self.height = height
        self.boxColor = boxColor
        self.font = font
        self.text = text
        self.action = action

    def draw(self, screen):
        """
        Draw the button on the specified screen.
        
        Args:
        - screen (pygame.Surface): The screen where the button is displayed.
        """
        Displayers.display_centered_constantBox_message(screen, self.boxColor, CL.white_color, 
                                             self.text, self.x, self.y, self.width, self.height, aFont = FT.small_font)
    
    def handle_event(self, event):
        """
        Check if the button has been clicked based on the Pygame event.
        
        Args:
        - event (pygame.Event): The event captured by Pygame.
        
        Returns:
        - bool: True if the button is clicked, False otherwise.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                    if self.action is not None:
                        self.action()
                    return True
                
        return False