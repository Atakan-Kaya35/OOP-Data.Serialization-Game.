import pygame 
import os
import pandas as pd
from variables import Display_Vars as DV
from variables import Colors as CL
from variables import Fonts as FT
from variables import Images as IM
from utilities import Displayers
from button import Button


class Coordinator:
    def __init__(self, screen, player1, player2, p1slider, p2slider, new_directory):
        os.chdir(new_directory)
        self.sheet = pd.read_csv("!Poker_Saves.csv")
        self.screen = screen
        self.player1 = player1
        self.player2 = player2
        self.p1slider = p1slider
        self.p2slider = p2slider
        self.next_column = self.sheet.iloc[0,0]
        self.last_played = self.sheet.iloc[0,1]
        self.total_saves = self.sheet.iloc[0,2]
        sections = DV.DEFAULT_IMAGE_HEIGHT / 55
        y = 2 * sections
        y += 20 * sections
        self.buttonWidth = 3 * DV.DEFAULT_IMAGE_WIDTH / 5
        self.buttonHeight = 4 * sections
        self.play_button = Button(DV.DEFAULT_IMAGE_WIDTH / 2, y, 
                             self.buttonWidth, self.buttonHeight,
                             "Play", CL.green_color, FT.font, action = self.move_on)
        y += 10 * sections
        self.save_button = Button(DV.DEFAULT_IMAGE_WIDTH / 2, y, 
                             self.buttonWidth, self.buttonHeight,
                             "Save", CL.red_color, FT.font, action=self.save_pregress)
        y += 10 * sections
        self.history_button = Button(DV.DEFAULT_IMAGE_WIDTH / 2, y, 
                             self.buttonWidth, self.buttonHeight,
                             "History", CL.black_color, FT.font, self.history_menu)
    
    def menu(self):
        self.screen.surface.blit(IM.bg_img, (0, 0))
        sections = DV.DEFAULT_IMAGE_HEIGHT / 55
        y = 7 * sections
        Displayers.display_centered_message(self.screen, CL.white_color, CL.black_color,
                                 "P   O   K   E   R", DV.DEFAULT_IMAGE_WIDTH / 2, y, aFont=FT.big_font)
        self.play_button.draw(self.screen)
        self.save_button.draw(self.screen)
        self.history_button.draw(self.screen)
        pygame.display.update()

        desicion_made = [False] * 3

        while True not in desicion_made:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                desicion_made[0] = self.play_button.handle_event(event)
                desicion_made[1] = self.save_button.handle_event(event)
                desicion_made[2] = self.history_button.handle_event(event)
    
    def save_pregress(self):
        self.screen.surface.blit(IM.bg_img, (0, 0))
        # 3 e böl save i oku onu göster, 
        text = f"Player 1 has {self.sheet.iloc[0, 1]}$, Player 2 has {(self.sheet.iloc[1, 1])}$"
        Displayers.display_centered_constantBox_message(self.screen, (20,40,20), CL.white_color, text, 
                                             DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT * 1 / 4,
                                             self.buttonWidth, self.buttonHeight, aFont=FT.small_font)
        text = f"Player 1 has {self.sheet.iloc[0, 2]}$, Player 2 has {(self.sheet.iloc[1, 2])}$"
        Displayers.display_centered_constantBox_message(self.screen, (20,40,20), CL.white_color, text, 
                                             DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT * 2 / 4,
                                             self.buttonWidth, self.buttonHeight, aFont=FT.small_font)
        text = f"Player 1 has {self.sheet.iloc[0, 3]}$, Player 2 has {(self.sheet.iloc[1, 3])}$"
        Displayers.display_centered_constantBox_message(self.screen, (20,40,20), CL.white_color, text, 
                                             DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT * 3 / 4,
                                             self.buttonWidth, self.buttonHeight, aFont=FT.small_font)
        pygame.display.update()
        column = 0
        while column == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    _, mouseY = pygame.mouse.get_pos()
                    if mouseY < DV.DEFAULT_IMAGE_HEIGHT / 3:
                        column = 1
                    elif mouseY < 2 * DV.DEFAULT_IMAGE_HEIGHT / 3:
                        column = 2
                    elif mouseY < DV.DEFAULT_IMAGE_HEIGHT:
                        column = 3

        self.sheet.iloc[0, column] = round(self.player1.balance, 1)
        self.sheet.iloc[1, column] = round(self.player2.balance, 1)
        self.sheet.iloc[3, column] = round(self.p1slider.selectedAmount, 1)
        self.sheet.iloc[4, column] = round(self.p2slider.selectedAmount, 1)
        self.sheet.to_csv('!Poker_Saves.csv', index=False)
        self.screen.surface.blit(IM.bg_img, (0, 0))


    def history_menu(self):
        self.screen.surface.blit(IM.bg_img, (0, 0))
        # 3 e böl save i oku onu göster, 
        text = f"Player 1 has {self.sheet.iloc[0, 1]}$, Player 2 has {(self.sheet.iloc[1, 1])}$"
        Displayers.display_centered_constantBox_message(self.screen, (20,40,20), CL.white_color, text, 
                                             DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT * 1 / 4,
                                             self.buttonWidth, self.buttonHeight, aFont=FT.small_font)
        text = f"Player 1 has {self.sheet.iloc[0, 2]}$, Player 2 has {(self.sheet.iloc[1, 2])}$"
        Displayers.display_centered_constantBox_message(self.screen, (20,40,20), CL.white_color, text, 
                                             DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT * 2 / 4,
                                             self.buttonWidth, self.buttonHeight, aFont=FT.small_font)
        text = f"Player 1 has {self.sheet.iloc[0, 3]}$, Player 2 has {(self.sheet.iloc[1, 3])}$"
        Displayers.display_centered_constantBox_message(self.screen, (20,40,20), CL.white_color, text, 
                                             DV.DEFAULT_IMAGE_WIDTH / 2, DV.DEFAULT_IMAGE_HEIGHT * 3 / 4,
                                             self.buttonWidth, self.buttonHeight, aFont=FT.small_font)
        pygame.display.update()
        column = 0
        while column == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    _, mouseY = pygame.mouse.get_pos()
                    if mouseY < DV.DEFAULT_IMAGE_HEIGHT / 3:
                        column = 1
                    elif mouseY < 2 * DV.DEFAULT_IMAGE_HEIGHT / 3:
                        column = 2
                    elif mouseY < DV.DEFAULT_IMAGE_HEIGHT:
                        column = 3


        self.player1.balance = self.sheet.iloc[0, column]
        self.player2.balance = self.sheet.iloc[1, column]
        self.p1slider.selectedAmount = self.sheet.iloc[3, column]
        self.p2slider.selectedAmount = self.sheet.iloc[4, column]
        self.screen.surface.blit(IM.bg_img, (0, 0))


    def move_on(self):
        pass