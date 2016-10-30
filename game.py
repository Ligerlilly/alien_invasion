import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Initialize game, settings,  and screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make ship,  a group to store bullets in, and alien group
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()


    # Set the background color
    bg_color = (230, 230, 230)

    # Make an Alien fleet
    gf.create_fleet(game_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(game_settings, aliens)

        gf.update_screen(game_settings, screen, ship, aliens, bullets)
        
run_game()
