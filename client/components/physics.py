from client.core.component import Component
from transform import Transform


class PhysicsComponent(Component):
    """Компонент, отвечающий за физику объекта."""

    def __init__(self, gravity=0.5, friction=0.1):
        super().__init__()
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = gravity
        self.friction = friction

    def update(self):
        """Обновление позиции объекта с учётом гравитации и трения."""
        transform = self.owner.get_component(Transform)
        if transform:
            self.velocity_y += self.gravity  # Применяем гравитацию
            transform.x += self.velocity_x
            transform.y += self.velocity_y

            # Применяем трение
            self.velocity_x *= (1 - self.friction)