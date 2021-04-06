import pygame

from settings import Settings
from pablo import Pablo
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.screen_width, game_settings.screen_height)
    pygame.display.set_caption("Example Game")


    pablo = Pablo(screen)

    while True:
        gf.check_events()
        gf.update_screen(game_settings, screen, pablo)

run_game()