from client.core.component import Component
from transform import Transform
import json


class NetworkComponent(Component):
    """Компонент для синхронизации объекта по сети."""

    def __init__(self, network_client, sync_rate=10):
        super().__init__()
        self.network_client = network_client
        self.sync_rate = sync_rate
        self.sync_counter = 0

    def update(self):
        """Синхронизация объекта с сервером."""
        if self.sync_counter % self.sync_rate == 0:
            transform = self.owner.get_component(Transform)
            if transform:
                data = {
                    "x": transform.x,
                    "y": transform.y
                }
                self.network_client.send_data(json.dumps(data))
        self.sync_counter += 1