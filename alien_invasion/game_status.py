
class GameStatus():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_status()

    def reset_status(self):
        self.ship_left = self.ai_settings.ship_limit