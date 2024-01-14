import pygame
pygame.init()

import os
new_directory = "\\Users\\hp\\Desktop\\Coding\\Projects\\Poker\\pixelateds"
os.chdir(new_directory)

class Display_Vars:
    # Define constants for the game display
    DEFAULT_IMAGE_WIDTH = 720
    DEFAULT_IMAGE_HEIGHT = 720
    CARD_DIMENSION_BASE = 21
    CARD_WIDTH = CARD_DIMENSION_BASE * 5
    CARD_HEIGHT = CARD_DIMENSION_BASE * 7
    default_card_size = (CARD_WIDTH, CARD_HEIGHT)
    VERTICAL_GAP = int((DEFAULT_IMAGE_HEIGHT - CARD_HEIGHT * 2) / 3)
    HORIZONTAL_GAP = 10
    MAX_NUM = "10000"

class Colors:
    # Define color constants
    white_color = (255,255,255)
    red_color = (200, 20, 20)
    green_color = (20,200,20)
    black_color = (0,0,0)
    table_color = (17,90,61)

class Arrays:
    # Define the suits, ranks, and related dictionaries for the game
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    value_key = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
    position_key = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                "Ten": 10, "Jack": 11, "Queen": 12, "King": 13}
    pair_key = {1: .975, 2: .075, 3: .15, 4: .225, 5: .3, 6: .375, 7: .45, 8: .525, 9: .6,
                10: .675, 11: .75, 12: .825, 13: .9}

class Fonts:
    width = Display_Vars.DEFAULT_IMAGE_WIDTH
    font = pygame.font.Font("freesansbold.ttf", int(width / 25))
    small_font = pygame.font.Font("freesansbold.ttf", int(width / 50))
    big_font = pygame.font.Font("freesansbold.ttf", int(width / 10))


class Images:
    # Load and scale the background image for the game
    bg_img = pygame.image.load('Blackjack_table.jpg')
    bg_img = pygame.transform.scale(bg_img, (Display_Vars.DEFAULT_IMAGE_WIDTH, Display_Vars.DEFAULT_IMAGE_HEIGHT))
    joker = pygame.image.load('red_joker.png')
    joker = pygame.transform.scale(joker, Display_Vars.default_card_size)

