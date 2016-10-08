import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game, settings,  and screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make ship
    ship = Ship(screen)

    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:
        gf.check_events(ship)
        gf.update_screen(game_settings, screen, ship)

run_game()