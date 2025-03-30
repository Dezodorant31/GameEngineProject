import socket, json


# класс сетевого клиента игры
class NetworkClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            print("Подключение к серверу")
        except ConnectionRefusedError:
            print("Ошибка подключения к серверу")

    def send_data(self, data):
        try:
            self.client_socket.send(json.dumps(data).encode())
        except:
            pass

    def receive_data(self):
        try:
            return json.loads(self.client_socket.recv(1024).decode())
        except:
            return None
