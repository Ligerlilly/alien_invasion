import sys

import pygame

from bullet import Bullet
from alien import Alien

def fire_bullet(game_settings, screen, ship, bullets):
    """Fire bullet if limit not reached"""
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)





def check_key_down_events(event, game_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_key_up_events(event, ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)

def update_bullets(bullets):
    """Update the position and get rid of old bullets"""
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_of_aliens(game_settings, alien_width):
    available_space_x = game_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_of_rows(game_settings, ship_height, alien_height):
    """Determine the number of reow of aliens that fit on the screen"""
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_of_rows = int(available_space_y / (2 * alien_height))

    
    return number_of_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    # Create an alien and place it in the row
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.x
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect. x = alien.x
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens to draw
    # Spacing between each alien is equal to one alien width
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_of_aliens(game_settings, alien.rect.width)
    num_rows = get_number_of_rows(game_settings, ship.rect.height, alien.rect.height )
   
    # Create rows of aliens
    for row_number in range(num_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)

def change_fleet_direction(game_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def check_fleet_edges(game_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def update_aliens(game_settings, aliens):
    """Check if the fleet is at an edge, and then update the aliens position in the fleet"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()

def update_screen(game_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(game_settings.bg_color)
    # Redraw all bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()
