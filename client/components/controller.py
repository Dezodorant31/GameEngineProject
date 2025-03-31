import pygame
from client.core.component import Component
from transform import Transform
from client.core.settings_manager import SettingsManager


class ControllerComponent(Component):
    """Компонент контроллера с привязками клавиш из настроек игры."""

    def __init__(self, controlled_object, speed=5):
        """
        :param controlled_object: объект, которым будет управлять контроллер
        :param speed: скорость передвижения объекта
        """
        super().__init__()
        self.controlled_object = controlled_object
        self.speed = speed
        self.settings = SettingsManager()
        self.load_key_bindings()

    def load_key_bindings(self):
        """Загружает привязку клавиш из настроек."""
        self.key_bindings = self.settings.get("key_bindings", {
            "move_left": pygame.K_LEFT,
            "move_right": pygame.K_RIGHT,
            "move_up": pygame.K_UP,
            "move_down": pygame.K_DOWN
        })

    def update(self):
        """Обрабатывает нажатия клавиш."""
        keys = pygame.key.get_pressed()
        transform = self.controlled_object.get_component(Transform)

        if transform:
            for action, key in self.key_bindings.items():
                if keys[key]:
                    self.execute_action(action, transform)

    def execute_action(self, action, transform):
        """Выполняет действие, связанное с клавишей."""
        if action == "move_left":
            transform.move(-self.speed, 0)
        elif action == "move_right":
            transform.move(self.speed, 0)
        elif action == "move_up":
            transform.move(0, -self.speed)
        elif action == "move_down":
            transform.move(0, self.speed)

    def change_key_binding(self, action, new_key):
        """Изменяет привязку клавиши к действию и сохраняет в настройки."""
        if action in self.key_bindings:
            self.key_bindings[action] = new_key
            self.settings.set("key_bindings", self.key_bindings)
            self.settings.save_settings()