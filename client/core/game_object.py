from component import Component


class GameObject:
    """Базовый класс для всех игровых объектов"""

    def __init__(self):
        self.components = {}
        self.event_listeners = {}

    def add_component(self, component: Component):
        """Добавляет компонент к объекту"""
        self.components[component.__class__.__name__] = component
        component.owner = self

    def get_component(self, component_class):
        """Возвращает компонент по классу."""
        return self.components.get(component_class.__name__)

    def handle_event(self, event_name, data=None):
        """Обрабатывает события."""
        if event_name in self.event_listeners:
            for callback in self.event_listeners[event_name]:
                callback(data)

    def register_event_listener(self, event_name, callback):
        """Регистрирует обработчик событий."""
        if event_name not in self.event_listeners:
            self.event_listeners[event_name] = []
        self.event_listeners[event_name].append(callback)

    def update(self):
        """Обновляет все компоненты."""
        for component in self.components.values():
            component.update()
