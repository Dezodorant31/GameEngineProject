import pygame
from network.client import NetworkClient


# Основной класс игры
class Game:
    def __init__(self, width=800, height=600, server_ip="127.0.0.1", server_port=5555):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("GameEngineProject")
        self.clock = pygame.time.Clock()
        self.running = True

        self.network = NetworkClient(server_ip, server_port)
        self.network.connect()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
