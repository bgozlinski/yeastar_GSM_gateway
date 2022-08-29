import socket
from time import sleep


class Yeastar:
    BUFFER_SIZE = 1024
    LoggedIn = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host: str, port: int, username: str, secret: str):
        self.host = host
        self.port = port
        self.username = username
        self.secret = secret

    def connect_to_yeastar(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        data = self.s.recv(self.BUFFER_SIZE)
        print(data.decode())
        if data.decode().__contains__("Asterisk"):
            data = self.send_command(f"Action: login\r\nUsername: {self.username}\r\nSecret: {self.secret}\r\n\r\n".encode(), 3)
            if data.decode().__contains__("Success"):
                self.LoggedIn = True
            if data.decode().__contains__('Error'):
                self.s.close()

    def send_command(self, message: bytes, timeout: int):
        self.s.send(message)
        sleep(timeout)
        data = self.s.recv(self.BUFFER_SIZE)
        print(data.decode())
        return data

    def close(self):
        self.s.close()
