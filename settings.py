class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo."""

        # Configurações da tela
        self._screen_width:int = 1200
        self._screen_height:int = 800
        self._bg_color:tuple = (230, 230, 230)
        self._ship_speed_factor:float = 1.5

        # Configurações dos projéteis
        self.bullet_speed_factor:int = 1
        self.bullet_width:int = 3
        self.bullet_height:int = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed:int = 3

    @property
    def screen_width(self)->int:
        return self._screen_width

    @property
    def screen_height(self)->int:
       return self._screen_height

    @property
    def bg_color(self)->tuple:
       return self._bg_color

    @property
    def ship_speed_factor(self)->float:
        return self._ship_speed_factor



