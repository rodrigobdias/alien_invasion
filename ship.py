import pygame


class Ship():

    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self._screen = screen

        # Carrega a imagem da espaçoname e obtém seu rect
        self._image = pygame.image.load('images/ship.bmp')
        self._rect = self._image.get_rect()
        self._screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self._rect.centerx = self._screen_rect.centerx
        self._rect.bottom = self._screen_rect.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self._screen.blit(self._image, self._rect)




