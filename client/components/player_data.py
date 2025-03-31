from client.core.component import Component

class PlayerDataComponent(Component):
    """Компонент, хранящий произвольные данные об игроке."""

    def __init__(self, **kwargs):
        """
        Позволяет задавать любые данные игрока через ключевые аргументы.
        Пример: PlayerDataComponent(name="Player1", score=0, team="Red")
        """
        super().__init__()
        self.data = kwargs  # Храним любые данные в словаре

    def get(self, key, default=None):
        """Получает значение по ключу, если ключа нет – возвращает default."""
        return self.data.get(key, default)

    def set(self, key, value):
        """Устанавливает или обновляет значение по ключу."""
        self.data[key] = value

    def remove(self, key):
        """Удаляет значение по ключу (если оно есть)."""
        if key in self.data:
            del self.data[key]