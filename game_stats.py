class GameStats():
    def __init__(self, game_settings):
        self.game_settings = game_settings

    def reset_stats(self):
        self.ship_left = self.game_settings.shit_limit