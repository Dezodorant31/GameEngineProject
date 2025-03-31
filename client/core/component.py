class Component:
    """Базовый класс для всех компонентов."""

    def __init__(self):
        self.owner = None  # Игровой объект, которому принадлежит компонент

    def update(self):
        """Обновление компонента (вызывается каждый кадр)."""
        pass