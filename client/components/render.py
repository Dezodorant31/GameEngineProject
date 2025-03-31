import pygame
from client.core.component import Component
from transform import Transform


class RenderComponent(Component):
    """Компонент, отвечающий за рендеринг спрайтов."""

    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def update(self):
        """Обновление позиции спрайта перед отрисовкой."""
        transform = self.owner.get_component(Transform)
        if transform:
            self.rect.topleft = (transform.x, transform.y)

    def render(self, screen):
        """Отрисовка объекта на экране."""
        screen.blit(self.image, self.rect)