import socket, threading, json


# Основной класс сервера
class GameServer:
    def __init__(self, host="0.0.0.0", port=5555):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.lock = threading.Lock()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Сервер запущен на {self.host}:{self.port}")

        while True:
            conn, addr = self.server_socket.accept()
            print(f"Новое подключение: {addr}")
            self.clients[conn] = {} # Заглушка для игрока
            threading.Thread(target=self.handle_client, args=(conn, )).start()

    def handle_client(self, conn):
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break

                player_data = json.loads(data)
                with self.lock:
                    self.clients[conn] = player_data

                self.broadcast_positions()
            except:
                break

        print("Отключение клиента")
        with self.lock:
            del self.clients[conn]
        conn.close()

    def broadcast_positions(self):
        positions = json.dumps(self.clients)

        with self.lock:
            for conn in list(self.clients.keys()):
                try:
                    conn.send(positions.encode())
                except:
                    conn.close()
                    del self.clients[conn]
