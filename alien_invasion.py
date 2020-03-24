import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # inicializa o jogo e cria um objeto para a tela
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

if __name__ == '__main__':
    run_game()





