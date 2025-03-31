import json


class SettingsManager:
    """Класс управления системными настройками игры."""

    def __init__(self, settings_file="settings.json"):
        self.settings_file = settings_file
        self.settings = {
            "resolution": (800, 600),
            "language": "en",
            "fullscreen": False,
            "key_bindings": {
                "move_left": 1073741904,  # pygame.K_LEFT
                "move_right": 1073741903,  # pygame.K_RIGHT
                "move_up": 1073741906,  # pygame.K_UP
                "move_down": 1073741905  # pygame.K_DOWN
            }
        }
        self.load_settings()

    def load_settings(self):
        try:
            with open(self.settings_file, "r") as file:
                self.settings.update(json.load(file))
        except FileNotFoundError:
            self.save_settings()

    def save_settings(self):
        with open(self.settings_file, "w") as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()
