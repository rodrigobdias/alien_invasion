class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo."""

        # Configurações da tela
        self._screen_width = 1200
        self._screen_height = 800
        self._bg_color = (230, 230, 230)
        self._ship_speed_factor =1.5

    @property
    def screen_width(self):
        return self._screen_width

    @property
    def screen_height(self):
       return self._screen_height

    @property
    def bg_color(self):
       return self._bg_color

    @property
    def ship_speed_factor(self):
        return self._ship_speed_factor



