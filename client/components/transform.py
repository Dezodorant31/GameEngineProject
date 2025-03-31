from client.core.component import Component


class Transform(Component):
    """Компонент, отвечающий за положение, вращение и масштаб."""

    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
